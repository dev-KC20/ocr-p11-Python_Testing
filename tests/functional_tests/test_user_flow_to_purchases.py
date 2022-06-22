# tests\functional_tests\test_python_org_search.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constants


def get_by_id_and_return(driver, searched_id):
    elem = driver.find_element(By.ID, searched_id)
    return elem


def get_account(club_account):
    if club_account[18:].isdigit():
        club_points = int(club_account[18:])
    else:
        club_points = 0
    return club_points


def test_user_makes_happily_flow_from_loggin_to_purchase():
    """
    GIVEN a Flask application configured for testing and a club's secretary
    requested to book 1 place at a competition
    THEN the hereunder flow will be achieved
    """

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)  # to ensure element on the page before finding it

    driver.get("http://127.0.0.1:5000")

    expected = constants.SELENIUM_SITE_TITLE
    assert expected in driver.title

    user_email = "admin@irontemple.com"
    element = get_by_id_and_return(driver, "club-email")
    element.clear()
    element.send_keys(user_email)
    element.send_keys(Keys.RETURN)
    element.submit()
    WebDriverWait(driver, 10).until(EC.title_contains(constants.SELENIUM_WELCOME_TITLE))
    expected = constants.SELENIUM_SITE_LOGGED_IN + user_email
    assert expected in driver.page_source
    club_account = get_by_id_and_return(driver, "account").text
    # Points available: 4
    current_club_point = get_account(club_account)
    places_to_book = 1
    element = get_by_id_and_return(driver, "competition")
    element.click()
    WebDriverWait(driver, 10).until(EC.title_contains(constants.SELENIUM_BOOKING_TITLE_LEFT))
    expected_summary = "Competitions:"

    element = get_by_id_and_return(driver, "Spring Festival")
    element.clear()
    element.send_keys(places_to_book)
    element.send_keys(Keys.RETURN)
    element.submit()
    WebDriverWait(driver, 10).until(EC.title_contains(constants.SELENIUM_WELCOME_TITLE))

    club_account = get_by_id_and_return(driver, "account").text
    # Points available: 1?
    new_club_point = get_account(club_account)
    assert new_club_point == current_club_point - (places_to_book * constants.PLACE_PRICE)
    driver.quit()
    # driver.close()
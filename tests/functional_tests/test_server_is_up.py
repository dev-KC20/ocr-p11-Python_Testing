from selenium import webdriver

import constants


def test_site_is_up_and_running():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:5000")
    expected = constants.SELENIUM_SITE_TITLE
    assert expected in driver.title

    driver.quit()

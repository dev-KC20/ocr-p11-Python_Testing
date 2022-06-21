# tests\functional_tests\test_python_org_search.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import constants

def test_site_is_up_and_running():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:5000")
    expected = constants.SELENIUM_SITE_TITLE
    assert expected in driver.title


    # elem = driver.find_element(By.NAME, "q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    driver.close()
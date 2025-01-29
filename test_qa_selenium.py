import pytest
import libarchive
import pydot
import cartopy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_table_search(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    assert "Expected Result" in driver.page_source

    search_box = driver.find_element(By.XPATH, "//td[text()='New York']")
    search_box.clear()
    search_box.send_keys("New York")

    driver.implicitly_wait(2)

    visible_rows = driver.find_elements(By.XPATH,"//[@id='example_info']")

    assert len(visible_rows) == 5, f"Test Failed: Expected 5 results, but found {len(visible_rows)}."

    if __name__ == "__main__":
        pytest.main(["-v", "qa_selenium_test.py"])


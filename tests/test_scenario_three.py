from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_page():
    # initialize the web driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # navigate to the search page
    driver.get("http://127.0.0.1:5000/")

    # locate the search input element
    search_input = driver.find_element(by=By.ID,value="tbx_identifier")

    # enter a search query
    search_input.send_keys("VIKO1988M")

    # locate the search button element
    search_button = driver.find_element(by=By.CLASS_NAME,value="search-btn")

    # click the search button
    search_button.click()

    # wait for the search results page to load
    driver.implicitly_wait(10)

    # assert that the search results page is displayed
    assert "Search Results" in driver.title

    # close the browser window
    driver.close()

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

def teardown_function(function):
    driver.quit()

def test_validproduct():
    driver.find_element(By.NAME, value="search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

def test_invalidproduct():
    driver.find_element(By.NAME, value="search").send_keys("Honda")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    excepted_text = "There is no product that matches the search criteria."
    actual_text=driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
    assert actual_text == excepted_text

def test_noproduct():
    driver.find_element(By.NAME, value="search").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    excepted_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(excepted_text)
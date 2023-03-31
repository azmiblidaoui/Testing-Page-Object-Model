import pytest
from selenium import webdriver
from utilities.test_data import TestData
@pytest.fixture(params=["chrome","firefox"])
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param =="firefox":
        driver =webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
    request.cls.driver = driver
    print("Browser:",request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("close Driver")
    driver.close()
        
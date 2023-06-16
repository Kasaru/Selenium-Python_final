import time
import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(30)
    print("\nquit browser..")
    browser.quit()
@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    print(f"\nstart browser for test with language = {language}")
    return language

import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def driver():
    browser = webdriver.Chrome() #Создаем объект содержащий браузер
    browser.set_window_size(1920,1080)
    yield browser #Код ниже будет воспроизводиться в конце теста
    browser.quit() #Закрываем браузер
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення обʼєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"/Users/juliaseniukgmail.com/Desktop/python_basics_prometeus/QA_auto/" + "chromedriver")
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адрІесу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
  
    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
    
    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    
    # Закриваємо браузер
    driver.close()

@pytest.mark.ui
def test_check_capslock_in_password_field():
    # Створення обʼєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"/Users/juliaseniukgmail.com/Desktop/python_basics_prometeus/QA_auto/" + "chromedriver")
    )

    # відкриваємо сторінку https://makeup.com.ua/ua/
    driver.get("https://makeup.com.ua/ua/")

    # Знаходимо поле, в яке будемо вводити правильну поштову адресу
    login_elem = driver.find_element(By.ID, "login")

    # Вводимо правильну поштову адрІесу
    login_elem.send_keys("juliaseniuk@gmail.com")

    # Закриваємо браузер
    driver.close()


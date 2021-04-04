from selenium import webdriver
import time
import random
import string

# Функция генерации произвольной строки с заданной длиной
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

# Функция автоматической регистрации
def main():
    driver = webdriver.Chrome()
    driver.get("https://timeweb.com/ru/")
    driver.find_element_by_css_selector('a.link.d').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_css_selector("a.login-btn.login-btn_secondary").click()
    driver.switch_to.window(driver.window_handles[2])
    full_names_list = driver.find_elements_by_xpath("//input[@type='text'][@name='full_name'][@class='suggestions-input']")
    for full_name in full_names_list:
        try:
            full_name.click()
            full_name.send_keys(generate_random_string(7))
        except:
            pass
    emails_list = driver.find_elements_by_xpath("//input[@type='text'][@name='email'][@class='suggestions-input']")
    for email in emails_list:
        try:
            email.click()
            email.send_keys(generate_random_string(7) + "@mail.ru")
        except:
            pass
    driver.find_element_by_css_selector("div.hosting-items__button.js-send-hosting-form.mt10").click()
    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    main()
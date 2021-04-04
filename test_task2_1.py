from selenium import webdriver
import time


# Функция "вытягивания" полей
def main():
    driver = webdriver.Chrome()
    driver.get("https://timeweb.com/ru/")
    driver.find_element_by_css_selector("a.link.d").click()
    driver.switch_to.window(driver.window_handles[1])
    login_textbox = driver.find_element_by_id("loginform-username")
    login_textbox.click()
    login_textbox.send_keys("ca47364")
    password_textbox = driver.find_element_by_id("loginform-password")
    password_textbox.click()
    password_textbox.send_keys("MuSg1Slo3ia2")
    log_btn = driver.find_element_by_name("login-button")
    log_btn.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    uptime_html = driver.find_element_by_css_selector("div#up-time-info")
    uptime_text = uptime_html.text[8:]
    price_per_mn_with_days_html = driver.find_elements_by_css_selector("p.cpS-h-XS")
    price_per_mn_text = price_per_mn_with_days_html[2].text
    days_left_text = price_per_mn_with_days_html[3].text
    time.sleep(10)
    driver.quit()
    return uptime_text, price_per_mn_text, days_left_text


if __name__ == "__main__":
    main()





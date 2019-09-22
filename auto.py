from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")

signin_link.click()

login_box = browser.find_element_by_id("login_field")
login_box.send_keys("noasuqare")
password_box = browser.find_element_by_id("password")
password_box.send_keys("Wori2019")
password_box.submit()

browser.quit()

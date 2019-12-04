
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # жму кнопку "I want to go on a magical journey!"
    browser.find_element_by_tag_name("button").click()
    
    # принимаю confirm
    browser.switch_to.alert.accept()
    
    # вывожу результат в поле "answer"
    browser.find_element_by_id("answer").send_keys(str((calc(browser.find_element_by_id("input_value").text))))
    
    # жму на кноку "Submit"
    browser.find_element_by_tag_name("button").click()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 12)

    button = browser.find_element_by_id("book")
    #жду цену $100 в <h5 id="price">..</h5>
    status = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    browser.find_element_by_id("answer").send_keys(str(calc(browser.find_element_by_id("input_value").text)))
    
    # жму на кноку "solve"
    browser.find_element_by_id("solve").click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()



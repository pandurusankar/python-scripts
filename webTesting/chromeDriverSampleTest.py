#Setup
# pip install webdriver_manager
# pip install selenium


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_opt)
driver.maximize_window()
driver.get("http://www.github.com/")
print(driver.title)
#add double () to expected condition, because it expected tuple value
WebDriverWait(driver, 10).until(cond.element_to_be_clickable((By.XPATH, "//a[@href='/login']")))
btn_login = driver.find_element_by_xpath("//a[@href='/login']")
btn_login.click()
WebDriverWait(driver, 10).until(cond.element_to_be_clickable((By.ID, "login_field"))).send_keys("pandurusankar@yahoo.com")
driver.find_element_by_id("password").send_keys("password")
driver.find_element_by_name("commit").click();
WebDriverWait(driver, 10).until(cond.element_to_be_clickable((By.XPATH, "//a[@href='/new']")))
driver.quit()
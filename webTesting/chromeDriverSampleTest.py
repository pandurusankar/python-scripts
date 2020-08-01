#Setup
# pip install webdriver_manager
# pip install selenium


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_opt)
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()
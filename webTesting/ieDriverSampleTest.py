#Setup
# pip install webdriver_manager
# pip install selenium

from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver

driver = webdriver.Ie(executable_path=IEDriverManager().install())
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()
#Setup
# pip install webdriver_manager
# pip install selenium

from webdriver_manager.microsoft import EdgeDriverManager
from selenium import webdriver

driver = webdriver.Edge(executable_path=EdgeDriverManager().install())
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()
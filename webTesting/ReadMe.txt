#Selenium Tip's

There are various strategies to locate elements in a page.
----------------------------------------------------------
driver.find_element_by_name("")
driver.find_element_by_xpath("")
driver.find_element_by_id("")
driver.find_element_by_css_selector("")
driver.find_element_by_link_text("")
driver.find_element_by_tag_name("")
driver.find_element_by_partial_link_text("")
driver.find_element_by_class_name("")


driver.find_elementS_by_name("")
driver.find_elementS_by_xpath("")
driver.find_elementS_by_id("")
driver.find_elementS_by_css_selector("")
driver.find_elementS_by_link_text("")
driver.find_elementS_by_tag_name("")
driver.find_elementS_by_partial_link_text("")
driver.find_elementS_by_class_name("")


from selenium.webdriver.common.by import By
driver.find_element(By.NAME, "")

These are the attributes available for By class:
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\WebDriver\chromedriver.exe")
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

newregistrantbtn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
newregistrantbtn.click()

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.send_keys("Lana")

lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.send_keys("Ivanova")

email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

email_input = driver.find_element_by_id("input-email")
email_input.send_keys("ivanova@gmail.com")


telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.send_keys("111 111 1111")

#Returning Customer
#Locate email and password
#enter password and click Login

loginpagebtn = driver.find_element_by_xpath("//a[contains(text(),'login page')]")
loginpagebtn.click()

email_address_field = driver.find_element_by_xpath("//input[@id='input-email']")
password_field = driver.find_element_by_xpath("//input[@id='input-password']")
password_input = driver.find_element_by_id("input-password")
password_input.send_keys("123123123")
loginbtn = driver.find_element_by_xpath("//input[@value='Login']")
loginbtn.click()
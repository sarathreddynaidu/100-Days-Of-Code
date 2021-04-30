from selenium import webdriver

chrome_driver_path = "C:/Users/sarat/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit = driver.find_element_by_css_selector("button")

f_name.send_keys("Sarath")
l_name.send_keys("Naidu")
email.send_keys("s.n@g.com")
submit.click()

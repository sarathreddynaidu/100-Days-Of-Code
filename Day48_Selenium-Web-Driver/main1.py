from selenium import webdriver

chrome_driver_path = "C:/Users/sarat/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

events_dates = driver.find_elements_by_css_selector(".event-widget time")
events_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(events_dates)):
    events[n] = {
        "time": events_dates[n].text,
        "name": events_names[n].text
    }

print(events)

driver.quit()

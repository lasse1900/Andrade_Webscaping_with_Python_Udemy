from selenium import webdriver

website = "https://www.adamchoi.co.uk/overs/detailed"
path = 'C:/bin/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)
driver.maximize_window()

#got_it_button = driver.find_element("//a[@href='Got it!']")
got_it_button = driver.find_element("a[@class='cc_btn cc_btn_accept_all']")
got_it_button.click()
all_matches_button = driver.find_element('//label[@analytics-event="All matches"]')
all_matches_button.click()


driver.quit()


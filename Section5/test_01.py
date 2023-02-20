from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
url = "https://scrapeme.live/shop/" 
options = webdriver.ChromeOptions() #newly added 
options.headless = True #newly added 
# with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: #modified 
# 	driver.get(url)
	
# ... 
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
	# ... 
	print("Page URL:", driver.current_url)
	print("Page Title:", driver.title)
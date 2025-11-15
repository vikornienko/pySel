from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=".\\wdrs\\geckodriver.exe")
options = webdriver.FirefoxOptions()

driver_firefox = webdriver.Firefox(service=service, options=options)
driver_chrome = webdriver.Chrome()
driver_edge = webdriver.Edge()

driver_firefox.get("https://ya.ru")
driver_chrome.get("https://google.com")
driver_edge.get("https://bing.com")

print(driver_firefox.title)
print(driver_chrome.title)
print(driver_edge.title)

driver_firefox.quit()
driver_chrome.quit()
driver_edge.quit()

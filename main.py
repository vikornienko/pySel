from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=".\\wdrs\\geckodriver.exe")
options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://ya.ru")

print(driver.title)
driver.quit()

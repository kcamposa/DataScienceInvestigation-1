from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = r'C:\Users\kev_d\Downloads\chromedriver\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
web = 'https://en.wikipedia.org/wiki/1982_FIFA_World_Cup'
driver.get(web)


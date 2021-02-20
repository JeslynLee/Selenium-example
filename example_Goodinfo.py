import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}],
            "selectedDestinationId": "Save as PDF", "version": 2,
            "isCssBackgroundEnabled": True, "scalingType": 3, "scaling": 100}
prefs = {"printing.print_preview_sticky_settings.appState": json.dumps(settings),
         "savefile.default_directory": "C:/Users/user/Downloads"}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')

webdriver_path = 'D:/Python/CultivationGrid/selenium/chromedriver.exe'
driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

driver.get("https://goodinfo.tw/StockInfo/index.asp")
driver.find_element_by_id("txtStockCode").click()
driver.find_element_by_id("txtStockCode").clear()
driver.find_element_by_id("txtStockCode").send_keys("0050")
driver.find_element_by_xpath(u"//input[@value='股票查詢']").click()
driver.find_element_by_id("imgKC").click()
sleep(5)
driver.execute_script('window.print();')
driver.close()


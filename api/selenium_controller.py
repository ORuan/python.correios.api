from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import requests, io, pdb, pdb, time, os, json, sys
import chromedriver_autoinstaller

#OA016913717BR
#user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}

class SearchCorreios():
    def __init__(self, code):
        self.code = code

    def config(self):
        path_install = chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        return webdriver.Chrome(
                        chrome_options=options,
                        executable_path=path_install
                    )
    def selenium_get_code(self):
        content_stages = []
        driver = self.config()
        try:
            driver.get(url='https://www2.correios.com.br/sistemas/rastreamento/default.cfm')
        except err as InvalidSessionIdException:
            print('error: ', err)
            driver.close()            
            return json.dumps({error:'ERRO'})
        text_area_correios = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]/div/div/form/fieldset/label/textarea')
        text_area_correios.send_keys(self.code)
        btn_send_code = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]/div/div/form/fieldset/div[2]/input')
        btn_send_code.click()
        content = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]')
        time.sleep(2)
        return content.text
        driver.close()
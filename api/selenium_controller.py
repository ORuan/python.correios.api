from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import requests
import io
import pdb
import pdb
import time
import os
import json
import sys
import chromedriver_autoinstaller
from selenium import webdriver
import pdb
# OA016913717BR
#user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}


class SearchCorreios():
    def __init__(self, code):
        self.code = code

    def config(self):
        # Check if the current version of chromedriver exists
        path_install = chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        return webdriver.Chrome(
            chrome_options=options,
            executable_path=path_install
        )

    def selenium_get_code(self):
        driver = self.config()

        try:
            driver.get(
                url='https://www2.correios.com.br/sistemas/rastreamento/default.cfm')
        except err as InvalidSessionIdException:
            print('error: ', err)
            driver.close()
            return json.dumps({error: 'ERRO'})

        driver.execute_script("""
            function automate(code){
                let text_area = document.getElementById('objetos')
                text_area.value = code;
                let btn_send = document.getElementById('btnPesq');
                btn_send.click()
            }; automate('"""+self.code+"""')
            """)
        content = driver.execute_script("""
            function get_content(){
                let __json={}
                let order = Array()
                let response = Array()   
                let content = document.querySelectorAll('.ctrlcontent .listEvent.sro tbody') 
                response = Array.prototype.slice.call(content)
                for (let i=0; i<response.length; i++){
                    __json[i] = response[i].innerText
                }
                return __json;
            }; return get_content()
        """)
        return content

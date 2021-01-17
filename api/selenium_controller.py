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
from seleniumwire import webdriver

# OA016913717BR
#user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}


class SearchCorreios():
    def __init__(self, code):
        self.code = code

    def config(self):
        # Check if the current version of chromedriver exists
        path_install = chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        return webdriver.Chrome(
            chrome_options=options,
            executable_path=path_install
        )

    def interceptor(self, request):
        # Delete the header first
        del request.headers['X-OPNET-AIX-PAGEID']  
        # Delete the header first
        del request.headers['X-OPNET-Transaction-Trace']

    def selenium_get_code(self):
        content_stages = []
        driver = self.config()
        driver.request_interceptor = self.interceptor

        try:
            driver.get(
                url='https://www2.correios.com.br/sistemas/rastreamento/default.cfm')
        except err as InvalidSessionIdException:
            print('error: ', err)
            driver.close()
            return json.dumps({error: 'ERRO'})
        text_area_correios = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]/div/div/form/fieldset/label/textarea')
        text_area_correios.send_keys(self.code)
        btn_send_code = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]/div/div/form/fieldset/div[2]/input')
        btn_send_code.click()
        content = driver.execute_script(
            'function get_content(){let t={},e=(Array(),Array()),r=document.querySelectorAll(".ctrlcontent .listEvent.sro tbody");e=Array.prototype.slice.call(r);for(let r=0;r<e.length;r++)t[r]=e[r].innerText;return t};get_content()')
        #content = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]')
        return content
        driver.close()


"""function automate(code){
    let text_area = document.getElementById('objetos')
    text_area.value = code;
    let btn_send = document.getElementById('btnPesq');
    btn_send.click()
}; automate(code)"""

"""
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
}; get_content
"""

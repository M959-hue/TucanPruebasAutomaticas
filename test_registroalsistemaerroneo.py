import csv
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegistroalsistemaerroneo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_registroalsistemaerroneo(self):
    # Test name: Registro al sistema erroneo
    # Step # | name | target | value
    # 1 | open | https://tucan.toolsincloud.net/index.php | 
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1361, 684)
    with open('Archivos csv/registros_cp02_2.csv', newline='',encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            name = fila['name']
            username = fila['username']
            email = fila['email']
            password = fila['password']
            # 3 | click | id=auto |
            self.driver.find_element(By.ID, "auto").click() 
            # 4 | waitForElementVisible | id=exampleInputEmail1 | 30000
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "exampleInputEmail1")))
            # 4 | click | id=exampleInputEmail1 |
            self.driver.find_element(By.ID, "exampleInputEmail1").click()
            # 5 | type | id=exampleInputEmail1 | Tester
            self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(name)
            # 6 | click | name=username | 
            self.driver.find_element(By.NAME, "username").click()
            # 7 | click | name=username | 
            self.driver.find_element(By.NAME, "username").click()
            # 8 | type | name=username | Tester!”#
            self.driver.find_element(By.NAME, "username").send_keys(username)
            # 9 | click | css=.form-group:nth-child(4) > #exampleInputEmail1 | 
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            # 10 | type | css=.form-group:nth-child(4) > #exampleInputEmail1 | tester@soft
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(email)
            # 11 | click | id=exampleInputPassword1 | 
            self.driver.find_element(By.ID, "exampleInputPassword1").click()
            # 12 | type | id=exampleInputPassword1 | 123
            self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
            # 13 | click | name=signup | 
            self.driver.find_element(By.NAME, "signup").click()
            # 14 | verifyText | css=.alert:nth-child(2) > .text-center | email is not valid email
            assert self.driver.find_element(By.CSS_SELECTOR, ".alert:nth-child(2) > .text-center").text == "email is not valid email"
            # 15 | verifyText | css=.alert:nth-child(3) > .text-center | password must between 5 and 20 length
            assert self.driver.find_element(By.CSS_SELECTOR, ".alert:nth-child(3) > .text-center").text == "password must between 5 and 20 length"
            # 16 | verifyText | css=.text-center:nth-child(1) | Only Chars and Numbers allowed in username
            assert self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(1)").text == "Only Chars and Numbers allowed in username"
  

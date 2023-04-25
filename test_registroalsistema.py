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

class TestRegistroalsistema():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_registroalsistema(self):
    # Test name: Registro al sistema
            # Step # | name | target | value
        # 1 | open | https://tucan.toolsincloud.net/index.php | 
    self.driver.get("https://tucan.toolsincloud.net/index.php")
            # 2 | setWindowSize | 1361x684 | 
    self.driver.set_window_size(1361, 684)
    with open('Archivos csv/registros_cp02_1.csv', newline='') as csvfile:
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
            # 5 | click | id=exampleInputEmail1 | 
            self.driver.find_element(By.ID, "exampleInputEmail1").click()
            # 5 | type | id=exampleInputEmail1 | PruebaSide
            self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(name)
            # 6 | click | name=username | 
            self.driver.find_element(By.NAME, "username").click()
            # 7 | type | name=username | Side
            self.driver.find_element(By.NAME, "username").send_keys(username)
            # 8 | click | css=.form-group:nth-child(4) > #exampleInputEmail1 | 
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            # 9 | click | css=.form-group:nth-child(4) > #exampleInputEmail1 | 
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            # 10 | click | css=.form-group:nth-child(4) > #exampleInputEmail1 | 
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
            # 11 | type | css=.form-group:nth-child(4) > #exampleInputEmail1 | pruebaside@selenium.com
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(email)
            # 12 | click | id=exampleInputPassword1 | 
            self.driver.find_element(By.ID, "exampleInputPassword1").click()
            # 13 | type | id=exampleInputPassword1 | pruebaselenium03
            self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
            # 14 | click | name=signup | 
            self.driver.find_element(By.NAME, "signup").click()
            #
            self.driver.refresh()
            self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(11) strong").click()


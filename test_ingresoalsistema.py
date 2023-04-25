import csv
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIngresoalsistema():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_ingresoalsistema(self):
    # Test name: Ingreso al sistema
    # Step # | name | target | value
    # 1 | open | https://tucan.toolsincloud.net/index.php | 
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    # 2 | setWindowSize | 1361x684 | 
    self.driver.set_window_size(1361, 684)
    # 3 | read credentials from csv file
    with open('Archivos csv/registros_cp01_1.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row['Email']
            password = row['Password']
            # 4 | click | name=email | 
            self.driver.find_element(By.NAME, "email").click()
            # 5 | type | name=email | predeterminado.username@gmail.com
            self.driver.find_element(By.NAME, "email").send_keys(email)
            # 6 | click | name=password | 
            self.driver.find_element(By.NAME, "password").click()
            # 7 | type | name=password | clave123
            self.driver.find_element(By.NAME, "password").send_keys(password)
            # 8 | click | name=login | 
            self.driver.find_element(By.NAME, "login").click()
            # 9 | assertText | css=.grid-user .username | @pruebasoftware3
            # 10 | go back to login page
            self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(11) strong").click()
test = TestIngresoalsistema()
test.setup_method()
test.test_ingresoalsistema()

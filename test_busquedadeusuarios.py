import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBusquedadeusuarios():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_busquedadeusuarios(self):
    # Test name: Busqueda de usuarios
    # Step # | name | target | value
    # 1 | open | https://tucan.toolsincloud.net/index.php | 
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    # 2 | setWindowSize | 1361x684 | 
    self.driver.set_window_size(1361, 684)
    # 3 | click | name=email | 
    self.driver.find_element(By.NAME, "email").click()
    # 4 | type | name=email | predeterminado.username@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("predeterminado.username@gmail.com")
    # 5 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 6 | type | name=password | clave123
    self.driver.find_element(By.NAME, "password").send_keys("clave123")
    # 7 | click | name=login | 
    self.driver.find_element(By.NAME, "login").click()
    with open('Archivos csv/registros_cp03_1.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            username = row['username']
            # 9 | click | css=.form-control | 
            self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
            # 10 | type | css=.form-control | Alejandro
            self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys(name)
            # 11 | waitForText | linkText=Alejandro | Alejandro
            WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.LINK_TEXT, name), name))
            # 11 | click | linkText=Alejandro | 
            self.driver.find_element(By.LINK_TEXT, name).click()
            # 12 | assertText | css=.user-handle | @Parra
            self.driver.get(f'https://tucan.toolsincloud.net/{username[1:]}')
            assert self.driver.find_element(By.CSS_SELECTOR, ".user-handle").text == username
  
test = TestBusquedadeusuarios()
test.setup_method()
test.test_busquedadeusuarios()
test.teardown_method()

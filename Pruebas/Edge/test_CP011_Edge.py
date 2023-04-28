import csv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIngresoalsistema():
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.vars = {}
    
    def teardown_method(self):
        self.driver.quit()
        
    def test_ingresoalsistema(self):
        print("Nombre de la prueba: Ingreso al sistema")
        print("Navegador: Firefox") 
        self.driver.get("https://tucan.toolsincloud.net/index.php")
        self.driver.maximize_window()
        success_count = 0
        failure_count = 0
        with open('Archivos csv/registros_cp01_1.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                email = row['Email']
                password = row['Password']
                self.driver.find_element(By.NAME, "email").click()
                self.driver.find_element(By.NAME, "email").send_keys(email)
                self.driver.find_element(By.NAME, "password").click()
                self.driver.find_element(By.NAME, "password").send_keys(password)
                self.driver.find_element(By.NAME, "login").click()
                # Check if login was successful or not
                if self.driver.current_url == "https://tucan.toolsincloud.net/home.php":
                    success_count += 1
                    print(f"La prueba {success_count} fue exitosa")
                else:
                    failure_count += 1
                    print(f"La prueba {failure_count} fue fallida")
                self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(11) strong").click()

test = TestIngresoalsistema()
test.setup_method()
test.test_ingresoalsistema()
test.teardown_method()
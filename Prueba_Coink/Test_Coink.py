import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Funciones.Page_Login import Funciones_Globales

class base_test(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    #CASO DE PRUEBA 1-2 Modulo de autenticacion
    def test_time(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://coink.com/ingreso/", 5)

    #CASO DE PRUEBA 3 Funcionalidad de ingresar SIN ser usuario
    def test_login_incorrect(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://coink.com/ingreso/", 1)
        f.click_xpath_valida("//a[@href='https://personas.coink.com']", 1)
        f.texto_id_valida("phone", "3214912113", 1)
        f.enter_pin_in_fields("input[type='number']","1993",1)
        f.captchap()
        f.click_xpath_valida("//button[@type='submit']", 1)
    # CASO DE PRUEBA 4 Funcionalidad volver dando clic en el boton Entendido de la ventana modal
        f.close_modal("//h2[contains(.,'!Algo paso!')]", 1)
        f.click_xpath_valida("//a[contains(.,'ENTENDIDO')]",1)

    #CASO DE PRUEBA 5 Autenticacion exitosa con credenciales validas
    #CASO DE PRUEBA 8 Autenticacion exitosa despues de los 15 min de bloqueo
    def test_login_correct(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://coink.com/ingreso/", 1)
        f.click_xpath_valida("//a[@href='https://personas.coink.com']", 1)
        f.texto_id_valida("phone", "3204912113", 1)
        f.enter_pin_in_fields("input[type='number']","1994",1)
        f.captchap()
        f.click_xpath_valida("//button[@type='submit']", 1)

    # CASO DE PRUEBA 6 - 7 Funcionalidad de bloque de cuenta y intentar autenticarse durante el periodo de bloqueo
    def test_login_blockade(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://coink.com/ingreso/", 1)
        f.click_xpath_valida("//a[@href='https://personas.coink.com']", 1)
        f.texto_id_valida("phone", "3214912113", 1)
        f.enter_pin_in_fields("input[type='number']", "1993", 1)
        f.captchap()
        f.click_xpath_valida("//button[@type='submit']", 1)
        f.close_modal("//div[@class='dialog']", 1)
        f.click_xpath_valida("//a[contains(.,'ENTENDIDO')]", 1)


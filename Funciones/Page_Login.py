import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def navegar(self, url, tie):
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(tie)
        return t

    #Funcion para dar clic al boton ingresar ahora
    def click_xpath_valida(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            #val.clear()
            val.click()
            print("Se dio click en el boton{}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+xpath)
            return t

    #Funcion para ingresar el numero de celular
    def texto_id_valida(self, id, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, id)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} en el texto {}".format(id, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + id)

    # Función para ingresar el PIN en campos individuales
    def enter_pin_in_fields(self,css, pin, tiempo):
        try:
            # Localiza los campos de entrada de PIN
            pin_fields = self.driver.find_elements(By.CSS_SELECTOR, css)

            # Verifica que hay al menos 4 campos
            if len(pin_fields) < 4:
                raise ValueError("No se encontraron suficientes campos para ingresar el PIN.")

            # Ingresa cada dígito del PIN en los primeros 4 campos encontrados
            for field, digit in zip(pin_fields[:4], pin):
                field.send_keys(digit)
                time.sleep(0.3)

            print("Escribiendo en el campo {} en el texto {}".format(css, pin))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + css)

    def check_captchap(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+xpath)

    def captchap(self):
        try:
            # Cambia al iframe del reCAPTCHA
            recaptcha_iframe = self.driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
            self.driver.switch_to.frame(recaptcha_iframe)

            # Localiza el cuadro del reCAPTCHA y haz clic
            recaptcha_checkbox = self.driver.find_element(By.CSS_SELECTOR, "div.recaptcha-checkbox-border")
            recaptcha_checkbox.click()

            # Regresa al contexto principal
            self.driver.switch_to.default_content()

            # Espera para que el reCAPTCHA se complete (si es necesario)
            time.sleep(10)

            # Continúa con el envío del formulario u otros pasos
            #submit_button = self.driver.find_element(By.ID, "submit_button")  # Ajusta el selector
            #submit_button.click()
            print("Click en el elemento {}".format("div.recaptcha-checkbox-border"))
            t = time.sleep(1)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + "div.recaptcha-checkbox-border")

    def close_modal(self,xpath, tiempo):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        close_button = self.driver.find_element(By.XPATH, xpath)
        close_button.click()

from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.bot import Bot

class LinguaLeo(Bot):
    user = 'testikB32@gmail.com'
    password = '12317871'

    def wait_element(self, by, req):
        return self.wait_driver.until(EC.presence_of_element_located((by, req)))

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://lingualeo.com/ru/r/9aej75")
        cls.wait_driver = WebDriverWait(cls.driver, 10)

    def set_error_list(self):
        self.error_list = ('Пользователь с таким адресом эл. почты уже есть на сервисе')

    def authenticate(self):
        self.loggin_user()
        if self.check_user():
            return True
        el = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'error_list')]/li")
        print el.text
            #
        return False

    def check_user(self):
        current_url = self.driver.current_url
        if current_url.split('/')[-1] == 'dashboard':
            return 'registered'
        elif current_url.split('/')[-1] == '1?refererstep=registration':
            return 'unregistered'

    def loggin_user(self):
        email_input = self.wait_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div[1]/form/div[1]/input")
        email_input.send_keys(self.user)
        password_input = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div[1]/form/div[2]/input')
        password_input.send_keys(self.password)
        button_submit = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div[1]/form/button')
        button_submit.click()

    def registration_user(self):
        gender = self.wait_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div/div/span['+str(randint(1, 2))+']/i')
        gender.click()

        age = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div/div/input')

        age.send_keys('\b')
        age.send_keys('\b')
        age.send_keys(randint(15, 30))
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[3]/a[1]').click()

        self.wait_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div['+str(randint(1, 3))+']').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[3]/a[1]').click()

        self.wait_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div/div[3]/div/a['+str(randint(3, 8))+']').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[2]/div/div[3]/div/a['+str(randint(3, 8))+']').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[3]/div/div[3]/div/a['+str(randint(3, 8))+']').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[4]/div/div[3]/div/a['+str(randint(3, 8))+']').click()

        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[3]/a[1]').click()

        entertainment_slide = self.wait_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div[2]/div/div[4]/div/div/div")

        check_lists = entertainment_slide.find_elements_by_class_name("check-con")

        for check_con in check_lists:
            checkbox_list = check_con.find_elements_by_class_name("checkbox-fl__bg")
            checkbox_len = len(checkbox_list)
            random_bool = [ randint(0,1) for p in xrange(0, checkbox_len) ]
            for k, v in enumerate(checkbox_list):
                if random_bool[k]:
                    v.click()

        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/div[3]/a[2]').click()


try:
    bot = LinguaLeo()
    bot.authenticate()
    print bot.check_user()
    # if bot.check_user() == 'registered':
    #
    #     print 'user registered'
    # else:
    #     bot.registration_user()


    pass

finally:
    print 'finally'
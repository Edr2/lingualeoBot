#coding: utf-8
from random import randint, shuffle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bot import Bot

class LinguaLeo(Bot):
    """Attributes from config.json:"""
    user            = None
    password        = None
    referral_link   = None
    jungle_link     = None
    upto_level      = None

    @classmethod
    def setUpClass(cls):
        cls.load_config('config.json')
        cls.driver = webdriver.Firefox()
        cls.wait_driver = WebDriverWait(cls.driver, 5)

    def wait_element(self, by, req):
        return self.wait_driver.until(EC.presence_of_element_located((by, req)))

    def run(self):
        self.goto_text_page()
        level = int(self.wait_element(By.XPATH, "//span[@data-level-number]").text)
        while( level != self.upto_level ):
            content_links = self.driver.find_elements_by_class_name("content-link")
            content_links[randint(0,len(content_links)-1)].click()

            words = self.driver.find_elements_by_tag_name('tran')
            shuffle(words)
            words = words[int(len(words)/1.3):]
            for word in words:
                word.click()
                content = self.wait_element(By.XPATH, "//div[@class='transw-content']")
                #todo: if not translate!
                link = content.find_element_by_class_name('transw-link')
                if(link):
                    link.click()

            self.driver.back()
        pass

    def goto_text_page(self):
        self.driver.get(self.jungle_link)
        self.wait_element(By.XPATH, "//li[@data-filter-entry='all']").click()
        self.wait_element(By.XPATH, "//a[@data-oid-track='format:text,jungle']").click()
        sort_by_pages = self.wait_element(By.XPATH, "//a[@data-sort-by='pages']")
        while( sort_by_pages.get_attribute('data-sort-by-dir')!='asc'):
            sort_by_pages.click()

    def set_error_list(self):
        self.error_list = {u'username_already_exists':u'Пользователь с таким адресом эл. почты уже есть на сервисе'}

    def authenticate(self):
        status = self.loggin_user()
        if status == 'unauthorized':
            el = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'error_list')]/li")
            err_method_name = [k for k,v in self.error_list.items() if v == el.text][0]
            err_function = getattr(self, err_method_name)
            err_function()
        elif status == 'registered':
            return True
        elif status == 'unregistered':
            self.registrate_user()

    def username_already_exists(self):
        index = self.user.index('@')
        another_email = self.user[:index] + '1' + self.user[index:]
        user_input = raw_input("""This email already exists with another password.\n\
        Please chose another way(number):\n\
        1 - Exit and edit config file.
        2 - Lets try with another email( %s )
        """ % another_email)
        if int(user_input) == 2:
            self.user = another_email
            self.authenticate()
        elif int(user_input) == 1:
            print 'Config file path:'
        else:
            self.username_already_exists()

    def check_user(self):
        current_url = self.driver.current_url
        if current_url.split('/')[-1] == 'dashboard':
            return 'registered'
        elif current_url.split('/')[-1] == '1?refererstep=registration':
            return 'unregistered'
        elif current_url.split('/')[-1] == 'register':
            return 'unauthorized'

    def loggin_user(self):
        self.driver.get(self.referral_link)
        email_input = self.wait_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div[1]/form/div[1]/input")
        email_input.send_keys(self.user)
        password_input = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div[1]/form/div[2]/input')
        password_input.send_keys(self.password)
        button_submit = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div[1]/form/button')
        button_submit.click()
        return self.check_user()

    def registrate_user(self):
        gender = self.driver.find_element(By.XPATH, '//div[contains(@class, "variant-select__list")]/span['+str(randint(1, 2))+']/i')
        gender.click()

        age = self.driver.find_element(By.XPATH, '//input[contains(@class, "variant-count__value")]')
        age.send_keys('\b')
        age.send_keys('\b')
        age.send_keys(randint(15, 30))
        self.driver.find_element(By.XPATH, '//div[contains(@class, "acenter")]/a[1]').click()

        self.wait_element(By.XPATH, '//div[contains(@class, "slide-item__content-inner")]/div/div['+str(randint(1,3))+']').click()
        self.driver.find_element(By.XPATH, '//div[contains(@class, "acenter")]/a[1]').click()

        self.wait_element(By.XPATH, '//div[contains(@class, "level-line__con-yellow")]/div/a['+str(randint(3,8))+']').click()
        self.driver.find_element(By.XPATH, '//div[contains(@class, "level-line__con-blue")]/div/a['+str(randint(3,8))+']').click()
        self.driver.find_element(By.XPATH, '//div[contains(@class, "level-line__con-green")]/div/a['+str(randint(3,8))+']').click()
        self.driver.find_element(By.XPATH, '//div[contains(@class, "level-line__con-red")]/div/a['+str(randint(3,8))+']').click()
        self.driver.find_element(By.XPATH, '//div[contains(@class, "acenter")]/a[1]').click()

        self.driver.find_element(By.XPATH, '//div[contains(@class, "slide-item__content-inner")]/div')
        check_lists = self.driver.find_elements_by_class_name("check-con")

        for check_con in check_lists:
            checkbox_list = check_con.find_elements_by_class_name("checkbox-fl__bg")
            checkbox_len = len(checkbox_list)
            random_bool = [ randint(0,1) for p in xrange(0, checkbox_len) ]
            for k, v in enumerate(checkbox_list):
                if random_bool[k]:
                    v.click()

        self.driver.find_element(By.XPATH, '//div[contains(@class, "acenter")]/a[2]').click()

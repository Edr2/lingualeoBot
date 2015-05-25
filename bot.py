class Bot():
    @classmethod
    def setUpClass(cls):
        "Hook method for setting up class before running in the class."

    @classmethod
    def set_error_list(self):
        pass

    def __init__(self):
        self.setUpClass()
        self.set_error_list()

    def run(self):
        pass

    def close(self):
        pass



# class botLingua( driver ):
#  pass
#
#
# driver.get("http://lingualeo.com/ru/jungle?isNew=1&levelMin=1&levelMax=1&entry=search&sortBy=best&sortDir=desc&userLang=ru&defaultSort=1&contentFormat=3&byTheme=0")
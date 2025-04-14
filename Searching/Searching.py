from Searching.intel_search import intel_search
from Searching.drushim import drushim_search
from Searching.amazon import amazon
import os
from selenium import webdriver



class Searching(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.jobs_found = []
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Searching, self).__init__(options=options)

        self.implicitly_wait(15)
        #self.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def intel(self):
        self.jobs_found.extend(intel_search(self))

    def drushim(self):
        self.jobs_found.extend(drushim_search(self))
    def amazon(self):
        self.jobs_found.extend(amazon(self))
























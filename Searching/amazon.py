from selenium.webdriver.common.by import By

jobs_found = []
def amazon(self):
    self.get(
        'https://amazon.jobs/content/en/locations/israel/tel-aviv?city%5B%5D=Tel+Aviv-Yafo&city%5B%5D=Haifa&employment-type%5B%5D=Intern&category%5B%5D=Software+Development')
    boxes = self.find_element(By.CSS_SELECTOR, 'ul[class="jobs-module_root__gY8Hp"]')
    box = boxes.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for info in box:
        title = info.find_element(By.CLASS_NAME, 'header-module_title__9-W3R').text
        object = info.find_elements(By.CLASS_NAME, 'css-1ruyw7v')
        location = object[0].text
        date = object[1].text
        link = info.find_element(By.CLASS_NAME, 'header-module_title__9-W3R').get_attribute('href')
        jobs_found.append([title, location, date, link])
    return jobs_found


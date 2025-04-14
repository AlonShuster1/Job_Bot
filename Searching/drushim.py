
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def drushim_search(self):
    self.get('https://www.drushim.co.il/')
    self.find_element(By.CLASS_NAME, 'show-all-selection-wrapper').click()
    self.find_element(By.CSS_SELECTOR, 'a[title="הייטק-תוכנה"]').click()
    # filter by location
    self.find_element(By.CSS_SELECTOR, '[data-cy="cy-input-where"]').send_keys('באר שבע')

    options = self.find_element(By.CLASS_NAME, 'v-select-list')
    options.find_elements(By.CLASS_NAME, 'v-list-item--link')[0].click()
    self.find_element(By.CLASS_NAME, 'v-select__selection--comma').click()
    self.implicitly_wait(15)
    element = self.find_element(By.XPATH,
                                '//div[contains(@class, "v-list-item__title") and contains(text(), "100 ק")]')
    element.click()
    self.find_element(By.CSS_SELECTOR,
                      'button[class="v-btn v-btn--contained theme--light v-size--default search-btn display-18 small cy-search-btn"]').click()

    # click on experience button (wait before first button is clickable)
    wait = WebDriverWait(self, 15)
    experience_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cy="cy-button-experience-filter"]')))
    experience_btn.click()

    self.find_element(By.CSS_SELECTOR, 'input[data-cy="cy-button-experience-filter0"]').click()
    self.find_element(By.CSS_SELECTOR, 'button[data-cy="cy-button-experience-filter-btn"]').click()

    # accessing job boxes:
    option = self.find_element(By.CLASS_NAME, 'jobs-row')
    options = option.find_elements(By.CLASS_NAME, 'jobList_vacancy')
    jobs_found = []
    for info in options:
        title = info.find_element(By.CLASS_NAME, 'primary--text').get_attribute('innerHTML').strip()
        cities = info.find_element(By.CLASS_NAME, 'flex-basis-0').text.strip()
        cities = cities.split('|')[0].strip()
        date = info.find_element(By.CLASS_NAME, 'inline-flex').text
        link = info.find_element(By.CLASS_NAME, 'px-1').get_attribute('href')
        jobs_found.append([title, cities, date, link])
    return jobs_found




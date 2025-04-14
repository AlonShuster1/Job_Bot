#searching intel
from selenium.webdriver.common.by import By

def intel_search(self):
    self.get(
        "https://intel.wd1.myworkdayjobs.com/en-US/External?shared_id=YzNiNDdlOTgtMjk4Yi00NTU4LTk5MjktODFkNzVlNDcwN2M0")
    # filter by location:
    self.find_element(By.CSS_SELECTOR, 'button[data-uxi-element-id="filter_distanceLocation"]').click()
    # Tel Aviv:
    self.find_element(By.ID, "1e4a4eb3adf101ad7f35e278bf812cd1").click()
    # petah Tikva:
    self.find_element(By.ID, "1e4a4eb3adf101aaeda8a474bf818ecd").click()
    # Kiryat Gat:
    self.find_element(By.ID, "1e4a4eb3adf101cb242c9e74bf8189cd").click()
    # Jerusalem
    self.find_element(By.ID, "1e4a4eb3adf101f41cd29774bf8184cd").click()
    # Haifa
    self.find_element(By.ID, "1e4a4eb3adf1013563ba9174bf817fcd").click()
    # Cesaria
    self.find_element(By.ID, "6dc05d901d65100158f5ba48aafb0000").click()
    # resetting mouse:
    self.find_element(By.CSS_SELECTOR, 'button[data-uxi-element-id="filter_distanceLocation"]').click()
    # filter by category: student:
    self.find_element(By.CSS_SELECTOR, 'button[data-uxi-element-id="filter_jobFamilyGroup"]').click()
    # intern/student:
    self.find_element(By.ID, "dc8bf79476611087d67b36517cf17036").click()
    # search:
    self.find_element(By.CSS_SELECTOR, 'button[data-automation-id="viewAllJobsButton"]').click()

    self.refresh()

    large_box = self.find_element(By.CLASS_NAME, 'css-27w6p6')
    small_boxes = large_box.find_elements(By.CLASS_NAME, 'css-1q2dra3')

    jobs_found = []
    for box in small_boxes:
        title = box.find_element(By.CSS_SELECTOR, 'a[data-automation-id="jobTitle"]').get_attribute('innerHTML').strip()
        link = box.find_element(By.CSS_SELECTOR, 'a[data-automation-id="jobTitle"]').get_attribute('href')

        info_boxes = box.find_elements(By.CLASS_NAME, 'css-129m7dg')
        location = info_boxes[0].get_attribute('innerHTML').strip()
        posted_on = info_boxes[1].get_attribute('innerHTML').strip()

        jobs_found.append([title, location, posted_on, link])
    return jobs_found
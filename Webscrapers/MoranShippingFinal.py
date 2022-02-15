from selenium import webdriver
import time


class Priority:

    # MoranShipping Page
    def __init__(self, front_page):
        self.front_page = front_page

    def data(self):
        # Finds the chrome driver. Might need to replace later
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(self.front_page)

        # Allows pop up to appear then dismisses it
        time.sleep(3)
        obj = driver.switch_to.alert
        obj.accept()

        # Checks and prints date and Priority
        Priority.check_priority(driver)

        # Clicks on the most recent update
        Priority.click(driver)

        # Grabs the current pages summary
        Priority.summary(driver)

        # Ends program
        driver.quit()

    def check_priority(self):
        # Organizes the layout for the header
        priority_title = self.find_elements_by_class_name("msa-fv")[2]
        degree = self.find_elements_by_class_name("msa-fv")[3]
        titles = "Date" + "\n" + priority_title.text
        data = "Priority" + "\n" + degree.text

        print(titles + "\n" * 2 + data)
        print("\n")

    def summary(self):
        # Scrapes the entire Notice
        for i in self.find_elements_by_class_name('MsoNormal'):
            print(i.text)
        ref_date = self.find_elements_by_class_name('msa-fn')[5]
        print(ref_date.text)

    def click(self):
        # Clicks on the most recent update
        click = self.find_elements_by_class_name("msa-fv [href]")[0]
        click.click()


# Pages and info for the programs
front_page = Priority('http://pta.ports.moranshipping.com/default.aspx')

# Runs the programs
Priority.data(front_page)

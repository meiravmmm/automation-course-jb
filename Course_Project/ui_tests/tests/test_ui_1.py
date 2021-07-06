import time
from time import sleep
from nltk.corpus.reader import xpath
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_001():
    driver = DriverFactory.create()
    driver.get('http://localhost:8080')
    project_name = 'Merav_123'
    LoginModel(driver).login()
    HomePage(driver).open_project()

    new_project = NewProject(driver)
    new_project.ProjectName(project_name)
    new_project.ADVANCED_SETTINGS_title()
    new_project.Description()
    new_project.status_on_track()
    new_project.save()
    new_project.Work_packages()

    time.sleep(10)
    actual = new_project.Work_packages()
    assert project_name == actual, (f'Project name {project_name} mismatch {actual}')
    time.sleep(10)


def test_main_002():
    driver = DriverFactory.create()
    driver.get('http://localhost:8080')
    LoginModel(driver).login()
    SelectProject(driver).Select_TestProject1()
    previous_count = SelectProject(driver).Select_Work_packages()
    SelectProject(driver).select_Task()
    SelectProject(driver).verify_task_name()
    SelectProject(driver).verify_subject_description()
    SelectProject(driver).save_button()
    SelectProject(driver).new_row_added(previous_count)
    SelectProject(driver).verify_data(expected_subject='GOOD WORK', expected_type='TASK')
    sleep(10)


# login to openproject- test1
class LoginModel:
    def __init__(self, driver : WebDriver):
        self.class_driver = driver

    def login(self):
        self.class_driver.find_element_by_css_selector("a[title='Sign in']").click()
        self.class_driver.find_element_by_id('username-pulldown').send_keys('admin')
        self.class_driver.find_element_by_id('password-pulldown').send_keys('0123456789')
        self.class_driver.find_element_by_id('login-pulldown').click()


# click + project - test2
class HomePage:
    def __init__(self, driver: WebDriver):
        self.class_driver = driver

    def open_project(self):
        element = self.class_driver.find_element_by_xpath("//a[@title='New project']")
        # time to wait
        # WebDriverWait(self.class_driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        # sleep(10)

        # option 1 - bypass - not intractable
        # url = element.get_attribute('href')
        # self.class_driver.get(url)

        # option 2 - bypass - not intractable
        self.class_driver.execute_script('arguments[0].click();', element)


class NewProject :
    def __init__(self, driver: WebDriver):
        self.class_driver = driver

    # unique value for project name - test3
    def ProjectName(self, project_name):
        sleep(5)
        self.class_driver.find_element_by_id("formly_3_textInput_name_0").send_keys(project_name)

    # click "ADVANCED SETTINGS" - test4
    def ADVANCED_SETTINGS_title(self):
        self.class_driver.find_element_by_xpath("//button[contains(.,'Advanced settings')]").click()

    # Type some text description text box - text5
    def Description(self):
        self.class_driver.find_element_by_xpath("//*[@id='formly_9_formattableInput_description_1']/div/op-ckeditor/div/div[2]/div").send_keys('GOOD WORK')

    #Type select status on track - test7
    def status_on_track(self):
        self.class_driver.find_element_by_id('formly_9_selectProjectStatusInput__links.status_4').click()
        sleep(5)
        self.class_driver.find_element_by_xpath("//ng-dropdown-panel//div[.='On track']").click()

    #click save - text 8
    def save(self):
        self.class_driver.find_element_by_xpath("//button[contains(text(), 'Save')]").click()

    # On "work packages" verfy the textse on the button= name of the project - text 9
    def Work_packages(self):
        return self.class_driver.find_element_by_id("projects-menu").get_attribute('title')





class SelectProject :
    def __init__(self, driver: WebDriver):
        self.class_driver = driver

    #select a project menu button - test 2
    def Select_TestProject1(self):
        self.class_driver.find_element_by_id('projects-menu').click()
        sleep(3)
        self.class_driver.find_element_by_xpath("//li[.='TestProject1']").click()

    # click work packages displayed the number of rows - test 3
    def Select_Work_packages (self):
        self.class_driver.find_element_by_xpath("//a[.//span/i and ./span[.='Work packages']]").click()
        sleep(3)
        row_count = len(self.class_driver.find_elements_by_xpath("//tbody[contains(@class,'results-tbody')]/tr"))
        return row_count
        print(row_count)

    #click +create green button and select "TASK" - test 4
    def select_Task(self):
        self.class_driver.find_element_by_xpath("//button[.='Create']").click()
        sleep(5)
        self.class_driver.find_element_by_xpath("//*[@id='types-context-menu']/ul/li/a/span[.='Task']").click()
        sleep(10)

    #verify the text "New TASK on top of the form that got opened on the right side - test 5
    def verify_task_name(self):
        sleep(5)
        elements = self.class_driver.find_elements_by_xpath("//wp-type-status//span")

        assert elements[0].text == 'New'
        assert elements[1].text == 'TASK'


    #Type unique strings into the subject and description boxes - test 6
    def verify_subject_description(self):
        self.class_driver.find_element_by_id('wp-new-inline-edit--field-subject').send_keys("GOOD WORK")

    # click save button - test 7
    def save_button(self):
        self.class_driver.find_element_by_id("work-packages--edit-actions-save").click()
        sleep(10)


    #verify that new row was added to the wowp-new-inline-edit--field-subjectrk packages table -test 8
    def new_row_added(self,previous_row_count):
        row_count = len(self.class_driver.find_elements_by_xpath("//tbody[contains(@class,'results-tbody')]/tr"))
        assert row_count== previous_row_count+1, "row_count is wrong"
        print(row_count)

    def verify_data(self, expected_subject, expected_type):
        assert self.class_driver.find_element_by_xpath("//tbody[contains(@class,'results-tbody')]/tr[last()]/td[contains(@class,'subject')]").text == expected_subject
        assert self.class_driver.find_element_by_xpath("//tbody[contains(@class,'results-tbody')]/tr[last()]/td[contains(@class,'type')]").text == expected_type

    #verify the subject and type of the last table row - test 9

    # //tbody[contains(@class,'results-tbody')]/tr[last()]/td[contains(@class,'subject')]
    # //tbody[contains(@class,'results-tbody')]/tr[last()]/td[contains(@class,'type')]



class DriverFactory:
    @staticmethod
    def create() -> WebDriver:
        return webdriver.Chrome("../Web_driver/chromedriver.exe")

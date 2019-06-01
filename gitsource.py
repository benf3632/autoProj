import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class github:

    @staticmethod
    def login(browser, username, password):
        browser.get("https://github.com/login")
        login_input = browser.find_element_by_name("login")
        login_input.send_keys(username)
        password_input = browser.find_element_by_name("password")
        password_input.send_keys(password)
        signin_button = browser.find_element_by_name("commit")
        signin_button.click()

    @staticmethod
    def create(browser, username, folder):
        browser.get("https://github.com/new")
        WebDriverWait(browser,5)
        repName_input = browser.find_element_by_name("repository[name]")
        repName_input.send_keys(folder)
        private_check = browser.find_element_by_id("repository_visibility_private")
        private_check.click()

        create_rep = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
        create_rep.submit()

        return "git remote add origin https://github.com/" + username + "/" + folder + ".git"


class gitlab:

    @staticmethod
    def login(browser, username, password):
        browser.get("https://gitlab.com/users/sign_in")
        login_input = browser.find_element_by_id("user_login")
        login_input.send_keys(username)
        password_input = browser.find_element_by_id("user_password")  
        password_input.send_keys(password)
        signin_button = browser.find_element_by_name("commit")
        signin_button.click()

    @staticmethod
    def create(browser, username, folder):
        browser.get("https://gitlab.com/projects/new")
        WebDriverWait(browser, 5)
        repName_input = browser.find_element_by_id("project_name")
        repName_input.send_keys(folder)
        create_button = browser.find_element_by_name("commit")
        create_button.click()

        return "git remote add origin https://gitlab.com/" + username + "/" + folder + ".git"


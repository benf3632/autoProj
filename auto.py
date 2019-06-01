import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

def login(browser):
    browser.get("https://github.com/login")
    login_input = browser.find_element_by_name("login")
    login_input.send_keys(str(sys.argv[2]))
    password_input = browser.find_element_by_name("password")
    password_input.send_keys(str(sys.argv[3]))
    signin_button = browser.find_element_by_name("commit")
    signin_button.click()

def create(browser, folder):
    browser.get("https://github.com/new")
    WebDriverWait(browser,5)
    repName_input = browser.find_element_by_name("repository[name]")
    repName_input.send_keys(folder)
    private_check = browser.find_element_by_id("repository_visibility_private")
    private_check.click()

    create_rep = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    create_rep.submit()

    remote_string = "git remote add origin https://github.com/" + sys.argv[2] + "/" + folder + ".git"
    push = "git push -u origin master"

    path = "C:\\Users\\CookieS\\Documents\\Programming\\"
    os.chdir(path)
    os.system("mkdir " + folder)
    os.chdir(path + folder)
    os.system("git init")
    os.system(remote_string)
    os.system("type nul > README.md")
    os.system("git add .")
    os.system("git commit -m \"initial commit\"")
    os.system(push)

def checkSysArgs():
    if (len(sys.argv) != 4):
        print("Usage: [Project Name] [Username] [Password]")
        return False
    return True

def main():
    res = checkSysArgs()
    if (not res):
        sys.exit(15)
    else:
        browser = webdriver.Chrome()
        login(browser)
        create(browser, str(sys.argv[1]))

if __name__ == "__main__":
    main()
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from gitsource import github
from gitsource import gitlab

def setupLocal(folder, remote_string):
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
    if (len(sys.argv) != 5):
        print("Usage: [Project Name] [Username] [Password] [gh - github | gl - gitlab]")
        return False
    return True

def main():
    res = checkSysArgs()
    if (not res):
        sys.exit(15)
    else:
        browser = webdriver.Chrome()
        source = str(sys.argv[4])
        folder = str(sys.argv[1])
        username = str(sys.argv[2])
        password = str(sys.argv[3])
        remote_string = ""

        if (source == "gh"):
            github.login(browser, username, password)
            remote_string = github.create(browser, username, folder)
        elif (source == "gl"):
            gitlab.login(browser, username, password)
            remote_string = gitlab.create(browser, username, folder)
        else:
            print ("Invalid source given only gh or gl")
        
        setupLocal(folder, remote_string)


if __name__ == "__main__":
    main()
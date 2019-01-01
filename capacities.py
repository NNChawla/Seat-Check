from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = os.getcwd() + "\\chromedriver.exe"

while True:
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    driver.get("https://my.olemiss.edu/irj/portal?NavigationTarget=navurl://03a271886019580e536eac4cd6d64f0e&role=Student&workset=Course%20Registration")
    
    username = driver.find_element_by_name('j_username').send_keys('username')
    password = driver.find_element_by_name('j_password').send_keys('password')
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    submit.click()

    driver.switch_to.frame('ivuFrm_page0ivu1')
    driver.switch_to.frame('isolatedWorkArea')

    while driver.find_elements_by_tag_name('select')==[]:
        pass
    """sleep is in case of network lag, elements needed some
    time to load otherwise it was attempting to access them
    without them being fully populated"""
    time.sleep(1)
    selects = driver.find_elements_by_tag_name('select')
    time.sleep(1)

    term = selects[0].find_element_by_tag_name('option')
    term.click()

    year = selects[1].find_element_by_tag_name('option')
    year.click()

    button = driver.find_element_by_tag_name('button')
    button.click()

    time.sleep(1)

    seats = driver.find_elements_by_tag_name('span')
    seats = seats[9].text.split('/')

    send = True
    if int(seats[0])!= 46:
        send = True

    if send:
        driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@placeholder='Email or phone']").send_keys('nnchawla@go.olemiss.edu')
        driver.find_element_by_xpath("//input[@value='Next']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys('password')
        driver.find_element_by_xpath("//input[@value='Sign in']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//div[@gh='cm']").click()
        time.sleep(1)
        driver.find_element_by_tag_name('textarea').send_keys('nnchawla@go.olemiss.edu')
        driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys('CSCI 343 Seats: ' + seats[0] + ' at ' + time.asctime())
        driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']").click()
        
    time.sleep(1)
    driver.get_screenshot_as_file("capture1.png")
    driver.quit()
    time.sleep(1800)

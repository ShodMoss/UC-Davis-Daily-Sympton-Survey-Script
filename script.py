from distutils.log import Log
from multiprocessing.connection import wait
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def completeSurvey(username, password):
    driver = webdriver.Chrome()
    driver.get('https://campusready.ucdavis.edu/symptom-survey')

    studentAndEmployees = driver.find_element_by_xpath('//*[@id="block-affiliatesymptomsurvey"]/section/div/div[2]/p/a')
    studentAndEmployees.click()

    Username = driver.find_element_by_xpath('//*[@id="username"]')
    Username.send_keys(username) #add personal username

    Password = driver.find_element_by_xpath('//*[@id="password"]')
    Password.send_keys(password) #add personal password

    Login = driver.find_element_by_xpath('//*[@id="submit"]')
    Login.click()

    driver.implicitly_wait(60) #waiting for 2 factor authentication

    QRtest = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button')
    if (QRtest == QRtest.is_displayed()): #checks if user recently requested for a covid test
        QRtest.click()

    completeSurvey = driver.find_element_by_xpath('//*[@id="ctl03"]/div[2]/div/a')
    completeSurvey.click()
 
    Continue = driver.find_element_by_xpath('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a')
    Continue.click()

    Question1 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[2]/fieldset/div/div[2]/div')
    Question1.click()

    Question2 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[3]/fieldset/div/div[2]/div')
    Question2.click()

    Question3 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[4]/fieldset/div/div[2]/div')
    Question3.click()

    Question4 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[5]/fieldset/div/div[2]/div')
    Question4.click()

    Question5 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[6]/fieldset/div/div[2]/div')
    Question5.click()

    bestAbility = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[7]/fieldset/div')
    bestAbility.click()

    submit = driver.find_element_by_xpath('//*[@id="mainbody"]/footer/div/div[2]/input')
    submit.click()

userResponse = input("Do you have covid? Do you have any symptons of covid? \
    Have you been around anyone with covid? \
    If answering yes to any one of these questions please reply with no\
    Answer with 'yes' or 'no' only please") #Can delete this questionnaire if wanting to automate it for yourself
if (userResponse == 'yes'): 
    print("We cannot fill out the survey for you.")
else:
    username = input("What is your UC Davis username?")
    password = input("What is your UC Davis password?")
    completeSurvey(username,password)



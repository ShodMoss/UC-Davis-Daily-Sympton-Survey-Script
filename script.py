from distutils.log import Log
from multiprocessing.connection import wait
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

studentAndEmployees = driver.find_element_by_xpath('//*[@id="block-affiliatesymptomsurvey"]/section/div/div[2]/p/a')
inputUsername = driver.find_element_by_xpath('//*[@id="username"]')
inputPassword = driver.find_element_by_xpath('//*[@id="password"]')
Login = driver.find_element_by_xpath('//*[@id="submit"]')
completeSurvey = driver.find_element_by_xpath('//*[@id="ctl03"]/div[2]/div/a')
Continue = driver.find_element_by_xpath('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a')
Question1 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[2]/fieldset/div/div[2]/div')
Question2 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[3]/fieldset/div/div[2]/div')
Question3 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[4]/fieldset/div/div[2]/div')
Question4 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[5]/fieldset/div/div[2]/div')
Question5 = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[6]/fieldset/div/div[2]/div')
bestAbility = driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[7]/fieldset/div')
submit = driver.find_element_by_xpath('//*[@id="mainbody"]/footer/div/div[2]/input')
QRtest = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button')

def completeSurvey(username, password):
    
    driver.get('https://campusready.ucdavis.edu/symptom-survey')
    studentAndEmployees.click()
    inputUsername.send_keys(username)
    inputPassword.send_keys(password)
    Login.click()
    driver.implicitly_wait(60)
    if (QRtest == QRtest.is_displayed()):
     QRtest.click()
    completeSurvey.click()
    Continue.click()
    Question1.click()
    Question2.click()
    Question3.click()
    Question4.click()
    Question5.click()
    bestAbility.click()
    submit.click()

userResponse = input("Do you have covid? Do you have any symptons of covid? \
    Have you been around anyone with covid? \
    If answering yes to any one of these questions please reply with no\
    Answer with 'yes' or 'no' only please")
if (userResponse == 'yes'):
    print("We cannot fill out the survey for you.")
else:
    username = input("What is your UC Davis username?")
    password = input("What is your UC Davis password?")
    completeSurvey(username,password)



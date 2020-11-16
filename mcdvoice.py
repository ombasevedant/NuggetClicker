from fake_useragent import UserAgent
from selenium import webdriver
from random import randrange
import time
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb

ua = UserAgent(verify_ssl=False)
user_agent = ua.random

print("USER AGENT: " + user_agent)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=" + user_agent)
driver = webdriver.Chrome(chrome_options=chrome_options)


def getNuggets(val_code):
    
    
    lstOfVal = val_code.split("-")
    CN1 = lstOfVal[0]
    CN2 = lstOfVal[1]
    CN3 = lstOfVal[2]
    CN4 = lstOfVal[3]
    CN5 = lstOfVal[4]
    CN6 = lstOfVal[5]

    url = "https://www.mcdvoice.com/" 

    print(url)

    driver.get(url)
    time.sleep(1)

#need the input code from the other part here
    driver.find_element_by_id('CN1').send_keys(CN1)
    time.sleep(.25)
    driver.find_element_by_id('CN2').send_keys(CN2)
    time.sleep(.25)
    driver.find_element_by_id('CN3').send_keys(CN3)
    time.sleep(.25)
    driver.find_element_by_id('CN4').send_keys(CN4)
    time.sleep(.25)
    driver.find_element_by_id('CN5').send_keys(CN5)
    time.sleep(.25)
    driver.find_element_by_id('CN6').send_keys(CN6)
    time.sleep(.25)    

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    driver.find_element_by_xpath(
        "//div[contains(@class, 'Opt1')]/span").click()

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    driver.find_element_by_xpath(
        "//td[contains(@class, 'Opt5')]/span").click()

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    rows = driver.find_elements_by_tag_name("tr")
    
    for row in rows:
        cell = row.find_elements_by_tag_name("td")[1] 
        cell.click()
        time.sleep(.25)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    rows = driver.find_elements_by_tag_name("tr")
    for row in rows:
        cell = row.find_elements_by_tag_name("td")[1] 
        cell.click()
        time.sleep(.25)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page (skippable lets skip this one part)
    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    driver.find_element_by_xpath(
        '/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]').click()

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page 
    rows = driver.find_elements_by_tag_name("tr")
    for row in rows:
        cell = row.find_elements_by_tag_name("td")[1] 
        cell.click()
        time.sleep(.25)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    s = "I love McDonald's =). McDonalds has the crispiest chicken in the nation."
    textbox = driver.find_element_by_xpath(
        '/html/body/div/div[3]/div[2]/form/div/div[1]/div[2]/div/div/div[2]/textarea')
    for c in s: 
        textbox.send_keys(c)
        time.sleep(.01)
    time.sleep(2)
    
    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    driver.find_element_by_xpath(
        '/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]').click()
    

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    driver.find_element_by_xpath(
        '/html/body/div/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]').click()

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    rows = driver.find_elements_by_tag_name("tr")
    for row in rows:
        cell = row.find_elements_by_tag_name("td")[1] 
        cell.click()
        time.sleep(.25)

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    driver.find_element_by_xpath(
        "/html/body/div/div[3]/div[2]/form/div/div[1]/div[2]/div/div[2]/span").click()

    driver.find_element_by_id('NextButton').click()
    time.sleep(1)

#next page
    code = driver.find_element_by_class_name(
        'ValCode').get_attribute("innerHTML").split(' ')[2]

    return code

n_obj = tk.Tk()
n_obj.withdraw()
user_input = simpledialog.askstring(title="Survey Code", prompt="Please enter your code (with hyphens):")

c = getNuggets(user_input)

#some way to display code to user
tkmb.showinfo("Verification Code", "Your code is: " + c)


driver.quit()
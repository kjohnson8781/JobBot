
import time
from time import sleep 
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import csv

starttime = time.time()
driver = wb.Firefox()

descrip = ['NEPA', 'environmental assessments', 'field surveys', 'weland delineation', 'sampling']
location = 'Texas'
position = 'environmental scientist'

url_list = []
company_list = []
title_list = []



action = ActionChains(driver)
driver.get("https://www.indeed.com/")
driver.find_element(By.ID,"text-input-what").send_keys(position)
driver.find_element(By.ID,"text-input-where").clear()
driver.find_element(By.ID,"text-input-where").send_keys(location)

time.sleep(.5)

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/span/div[4]/div[1]/div/div/div/div/form/button').click()
time.sleep(2)

# driver.find_element(By.CLASS_NAME, "jobsearch-ResultsList css-0") 
# /html/body/div/div[2]/div/span/div[4]/div[5]/div[2]/div/div/div[2]/div[1]/ul

time.sleep(2)

for i in range(10):
    joblist = driver.find_element(By.CSS_SELECTOR, "ul[class^='jobsearch-ResultsList']") 
    jobads = joblist.find_elements(By.CSS_SELECTOR, "div[class^='cardOutline tapItem']")
    for j in range(len(jobads)): #len(jobads)-1,
        # print("-----------------------------------")
        # print(jobads[i].text)

        # print("-----------------------------------")
        
        try:
            
            if (jobads[j].text != ""):
                jobads[j].click()
                
                time.sleep(.5)
                # driver.switch_to.frame("vjs-container-iframe")
                # print('title test')
                driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
                
                # print(driver.page_source)
                
                time.sleep(.5)
                
                soup = bs(driver.page_source,features="html.parser")

                title_finder = soup.find('title')
                titletext = title_finder.get_text()
                titletext = titletext.split("-")[0]

                company_finder = soup.find_all('div', class_='icl-u-lg-mr--sm icl-u-xs-mr--xs')
                for company in company_finder:
                    if(company.find('a')):
                        ctext = company.find('a').get_text()
            
                job_finder = soup.find('div', class_='jobsearch-jobDescriptionText')
                text = job_finder.get_text()
                for k in range(len(descrip)):
                    if(str(descrip[k]) in text):
                        url = driver.current_url
                        if not url in url_list:
                            url_list.append(url)
                            company_list.append(ctext)
                            title_list.append(titletext) 

                # print(url_list)
                # print(company_list)
                # print(title_list)
                    
                driver.switch_to.default_content()
                time.sleep(1)


        except Exception as e:
            print("Unable to read job error:" , e)

    try:
        paginationList = driver.find_element(By.CSS_SELECTOR,"[aria-label=pagination]")
        # print("driver", paginationList)
        pList = paginationList.find_elements(By.TAG_NAME, 'li') # next button
        # print("plist", len(pList))
        # for li in pList:
        #     print(li)
        pList[-1].click()

    except Exception as e:
            print("Can't find next button:" , e)
    try:
        action.send_keys(Keys.RETURN).perform()
    except Exception as e:
        print("no popup found")

    time.sleep(5)

time.sleep(10)
driver.quit()

header = ['Position Title', 'Company', 'URL']
rows = zip(title_list, company_list, url_list)
with open('joblist.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)


# print(time.time() - starttime)


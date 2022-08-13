from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import time
from time import sleep 
import selenium
from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

starttime = time.time()
driver = wb.Firefox()

descrip = ['PlayStation', 'Python', 'SQL']
urls = []

location = 'Austin'

driver.get("https://www.indeed.com/")
driver.find_element(By.ID,"text-input-what").send_keys("data center")
time.sleep(.5)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/span/div[4]/div[1]/div/div/div/div/form/button').click()
time.sleep(2)

joblist = driver.find_element(By.CSS_SELECTOR, "ul[class^='jobsearch-ResultsList']") 
# driver.find_element(By.CLASS_NAME, "jobsearch-ResultsList css-0") 
# /html/body/div/div[2]/div/span/div[4]/div[5]/div[2]/div/div/div[2]/div[1]/ul
jobads = joblist.find_elements(By.CSS_SELECTOR, "div[class^='cardOutline tapItem']")
for i in range(len(jobads)-1,len(jobads)):
    # print("-----------------------------------")
    # print(jobads[i].text)

    # print("-----------------------------------")
    
    try:
        
        if (jobads[i].text != ""):
            jobads[i].click()
            
            time.sleep(1)
            # driver.switch_to.frame("vjs-container-iframe")
            # print('title test')
            driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
            
            # print(driver.page_source)
            
            
            
            soup = bs(driver.page_source,features="html.parser")
            # found_key = False

            title_finder = soup.find('title')
            # # for title in title_finder:
            titletext = title_finder.get_text()
            print(titletext)
            time.sleep(.5)

            company_finder = soup.find_all('div', class_='icl-u-lg-mr--sm icl-u-xs-mr--xs')
            # print('c,', len(company_finder))
            # for company in company_finder:
            for company in company_finder:
                if(company.find('a')):
                    print(company.find('a').get_text())


            job_finder = soup.find('div', class_='jobsearch-jobDescriptionText')
            print(job_finder)
            all_text = job_finder.find_all('br')
            # for text in all_text:
                

            # companytext = company_finder.get_text()
            # print(companytext)
            # time.sleep(.5)

            # key_finder = soup.find_all('div', class_='jobsearch-jobDescriptionText')
            # # print('len', len(key_finder))
            # for key in key_finder:
            #     ptags = key.find_all('p')
            #     for text in ptags:
            #         # print("d len", len(descrip))
            #         for j in range(len(descrip)):
            #             # print("descrip j", descrip[j], ", text, ", text.get_text())
            #             if(str(descrip[j]) in text.get_text()):
            #                 found_key = True
                    
            
            # if(found_key):
            #     url = driver.current_url
            #     urls.append(url)
            
            # print(urls)
            

            # print(soup)
            driver.switch_to.default_content()
            time.sleep(1)


    except Exception as e:
        print("Unable to read job error:" , e)

    
    

time.sleep(100)
driver.quit()
# print(time.time() - starttime)
# try:
#     test = driver.find_element(By.XPATH, '')

# driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[2]input').send_keys("kjj8781@tamu.edu")
# driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/form/div[3]/input').send_keys("Schoo!2022")
# time.sleep(5)

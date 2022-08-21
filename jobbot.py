
import time
from time import sleep 
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import csv

starttime = time.time() # to track how much time the code takes

driver = wb.Firefox() # initialize driver

# USER INPUT (change this based on needed search)
descrip = ["NEPA", "environmental assessments", "field surveys", "wetland delineation", "sampling"]
location = "Texas"
position = "environmental scientist"

# Initialize data lists
url_list = []
company_list = []
title_list = []



action = ActionChains(driver) # initialize action for popup 

# START OF DRIVER 
driver.get("https://www.indeed.com/")                               # Go to job website 
driver.find_element(By.ID,"text-input-what").send_keys(position)    # Input wanted user position
driver.find_element(By.ID,"text-input-where").clear()               # Delete location data
driver.find_element(By.ID,"text-input-where").send_keys(location)   # Input wanted user location

time.sleep(.5) # sleep driver to make sure inputs load in

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/span/div[4]/div[1]/div/div/div/div/form/button').click() # Click on search button

time.sleep(2) # Wait for results to load

for i in range(10):   # Parse through 10 pages of results (change as needed)
    joblist = driver.find_element(By.CSS_SELECTOR, "ul[class^='jobsearch-ResultsList']")  # Create list of all job results on page
    jobads = joblist.find_elements(By.CSS_SELECTOR, "div[class^='cardOutline tapItem']")  # Find the text in all the job results on page (on Indeed the job descriptions pop up as cards)
    
    # Parse through all job results
    for j in range(len(jobads)):      
        try:
            
            if (jobads[j].text != ""): # Error checking in case the driver added blank jobs
                jobads[j].click() # Click through each job result in order to parse through text
                
                time.sleep(.5) # Wait for card to load

                driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe")) # Switch driver to look at content in card
                
                time.sleep(.5)
                
                soup = bs(driver.page_source,features="html.parser") # Use BeautifulSoup to get html code of card page
                
                # FIND JOB TITLE
                title_finder = soup.find('title') 
                titletext = title_finder.get_text()
                titletext = titletext.split("-")[0] # Remove extraneous info Indeed adds onto title

                # FIND COMPANY TITLE
                company_finder = soup.find_all('div', class_='icl-u-lg-mr--sm icl-u-xs-mr--xs')
                for company in company_finder:
                    if(company.find('a')):
                        ctext = company.find('a').get_text()

                # FIND JOB DESCRIPTION
                job_finder = soup.find('div', class_='jobsearch-jobDescriptionText')
                text = job_finder.get_text()

                # Parse through job description to find keywords
                for k in range(len(descrip)):
                    if(str(descrip[k]) in text):
                        url = driver.current_url                # Get URL of job card driver is parsing through
                        if not url in url_list:                 # Ensure no duplicates
                            url_list.append(url)
                            company_list.append(ctext)
                            title_list.append(titletext) 
                    
                driver.switch_to.default_content() # Switching out of card frame in order to go to next page
                time.sleep(1)


        except Exception as e:
            print("Unable to read job error:" , e)

    # GO TO NEXT PAGE
    try:
        paginationList = driver.find_element(By.CSS_SELECTOR,"[aria-label=pagination]")
        pList = paginationList.find_elements(By.TAG_NAME, 'li') # next button
        pList[-1].click()

    except Exception as e:
            print("Can't find next button:" , e)

    # Catch and close popup if one appears
    try:
        action.send_keys(Keys.RETURN).perform()
    except Exception as e:
        print("no popup found")

    time.sleep(5)

time.sleep(5)
driver.quit()

# WRITE RESULTS TO FILE
header = ['Position Title', 'Company', 'URL']
rows = zip(title_list, company_list, url_list)
with open('joblist.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)


# print(time.time() - starttime)


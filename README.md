# JobBot - An Automated Job Searching Script

JobBot is a python script that automatically searches through job postings on Indeed for user inputted keywords. The script obtains the Job Title, Company Name, and URL for all the job results that have a description that matches a keyword. The data is then aggregated into a csv file for a simple, effortless end-user experience.

![](https://github.com/kjohnson8781/JobBot/blob/main/JobBotPresentation.gif) 

## Installation

1. Install [geckodriver](https://github.com/mozilla/geckodriver/releaseshttps://github.com/mozilla/geckodriver/releases)
  * Unzip File

  * Copy .exe file into python parent (ex. C:\Python34)

2. Install selenium: ```pip install selenium``` 

3. Install BeautifulSoup: ```pip install beautifulsoup4``` 

## Usage

1. Input User Preferences
  * Keywords 
```python
descrip = []
```
  * Location
```python
location = " "
```
  * Position
```python
position = " "
```
2. Input number of pages you want to iterate through.
```python
for i in range(#)
```
3. Run ```$ python JobBot.py```
4. The script will open Indeed.com and start searching
5. Navigate to csv file "joblist.csv" in Users
6. Open file and enjoy!

## Inspiration
My friend was expressing frustrations on how long it takes to look through job postings. I wanted to do a side project so I thought this would be a fun script to write. It is not perfect but most bugs will fix themselves if you run the code again. Special thanks to Selenium and BeautifulSoup for making this script possible. 

## License
[MIT](https://choosealicense.com/licenses/mit/)

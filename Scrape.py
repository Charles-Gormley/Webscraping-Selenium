# Webscraping-Selenium

# Webscraping Tool that pull data off an Ahrefs premium account for SEO Keyword Research. 
# Can Parse thoruhg hundreds of keywords and insert that data into an excel file. 

#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter
import time

#Browser
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Opening Google Login
driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")


#Manual Input Time
time.sleep(45)

#Defining Search Bar
search = driver.find_element_by_id('se_pe_target')

#Backspace Code
expo = 'www.experian.com'
count = len(expo) + 1
while count > 0:
    search.send_keys(Keys.BACKSPACE)
    count -= 1
time.sleep(2)

#Create Excel Files
book = xlsxwriter.Workbook('Site_Explorer6.xlsx')
sheet = book.add_worksheet()

#Declaring Titles

url = ["www.liberty1financial.com",
"www.badcredit.org/",
"www.discover.com/",
"www.creditsesame.com/",
"www.bankofamerica.com/credit-cards/"]



b = 0

time.sleep(20)
for y in url:
    b += 1
    search.send_keys(y)
    search.send_keys(Keys.ENTER)
    Rank = driver.find_element_by_id('topAhrefsRank')
    sheet.write(b, 1, Rank.text)
    URL = driver.find_element_by_id('UrlRatingContainer')
    sheet.write(b, 2, URL.text)
    DR = driver.find_element_by_id('DomainRatingContainer')
    sheet.write(b, 3, DR.text)
    Backlinks = driver.find_element_by_id('numberOfRefPages')
    sheet.write(b, 4, Backlinks.text)
    Referring_Domains = driver.find_element_by_id('numberOfRefDomains')
    sheet.write(b, 5, Referring_Domains.text)
    OrganicKey = driver.find_element_by_id('numberOfOrganicKeywords')
    sheet.write(b, 6, OrganicKey.text)
    OrganicTraffic = driver.find_element_by_id('numberOfOrganicTraffic')
    sheet.write(b, 7, OrganicTraffic.text)
    BacklinkStats = driver.find_element_by_id('BacklinksStatsContainer')
    Backie = BacklinkStats.text
    l = Backie.split()
    for j in range(11):
      i = 1 + j*3
      column = j+8
      sheet.write(b, column, l[i])

    time.sleep(12)
    count = len(url) + 50
    while count > 0:
        search.send_keys(Keys.BACKSPACE)
        count -= 1
    time.sleep(8)

a = 0
Titles = ['Ahrefs Rank', 'URL Rank', 'Domain Rank', 'Backlinks', 'Referring Domains', 'Organic Keywords', 'Traffic Value',
          'Referring domains', 'Dofollow', 'Governmentatl', 'Educational', '.gov', '.edu', '.com',
          '.net', '.org', 'Backlinks', 'Dofollow', 'Nofollow', 'UGC', 'Sponsored',
          'Text', 'REdirect', 'Image', 'Form', 'Governmental', 'Educational']
for x in Titles:
    a+=1
    sheet.write(0, a, x)




#declare data
book.close()

#Leaving Driver
driver.quit()

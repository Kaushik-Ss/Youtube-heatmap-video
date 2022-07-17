#!/usr/bin/env python
# coding: utf-8
                    
# WARNING 
# This file uses a dependent website to embed youtube link so as for the end time to work 
# This is caused because YouTube has restricted video payback on localhost
# Embed videos need a subdomain to host the file otherwise the video wont open
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from svgpathtools import parse_path, Line, Path, wsvg
import requests
import pyperclip

import os
from urllib.request import urlopen
import webbrowser
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from selenium import webdriver  

os.chdir('C:\\Users\\Kau\\Desktop\\web')
baseDir=os.getcwd()



url=input("Enter Url\n")
# url='https://www.youtube.com/watch?v=2yAxWc_ZQRA'                      

# A lot of text manipulation
html = str(urlopen(url).read())
str_ind=html.index('{"heatMarkerRenderer":')
end_ind=html.index('heatMarkersDecorations')
text_html=html[str_ind+22:end_ind-3]
text_html=text_html.replace('"timeRangeStartMillis":','')

text_html=text_html.replace('"markerDurationMillis":','')
text_html=text_html.replace('"heatMarkerIntensityScoreNormalized":','')
text_html=text_html.replace('{"heatMarkerRenderer":','')

text_html=text_html.replace('},',',\n')
             
with open("tes.txt",'w',encoding = 'utf-8') as f:
   f.write(text_html)


                        
temp=text_html
temp=temp.replace(',\n','},')
temp=temp.replace('}},{','\n')
temp=temp[1:-2]
temp=temp.split('\n')


                        
temp_val=[]
for i in temp:
    temp_values=i.split(',')
    tempp=[int(i) for i in temp_values[:-1]]
    tempp.append(float(temp_values[-1]))
    temp_val.append(tempp)

k=0
for i in temp_val:
    if i[2]==1.0:
        break
    k+=1
max_val=temp_val[k]
max_time=max_val[0]
mid_time=max_val[1]
start_time=max_time-2*mid_time
end_time=max_time+2*mid_time
start_time=round(start_time,1)
end_time=round(end_time,1)


start_time=start_time/1000
end_time=end_time/1000
end_time=int(end_time)
start_time=int(start_time)


min_s_t=start_time//60
sec_s_t=start_time%60
min_e_t=end_time//60
sec_e_t=end_time%60
t='t=XmYs'
t='?t='+str(min_s_t)+'m'+str(sec_s_t)+'s'


vid_link=''                    

if min_s_t==0 and min_e_t==0:
    st=str(start_time)
    ed=str(end_time)
    v_ind=url.index('v=')
    vid_link=url[v_ind:]
    url_final='?t='+st+'&end='+ed
    url_final='?t='+st
else:
    url_final=t

url_l='{}?start={}&end={}&autoplay=1'.format(url,str(start_time),str(end_time))
time_rem=end_time-start_time

url_l='https://listenonrepeat.com/?v={}&s={}&e={}&autoplay=1'.format(vid_link[2:],str(start_time),str(end_time))
print(url_l)
print('Website opened in a browser')

url_pls='https://www.socialvideoplaza.com/en/tools/embed-code-link-generator'

# options = Options()
# options.headless = True
driver = webdriver.Chrome()

driver.maximize_window()  
driver.get(url_pls)  
m = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/button[1]')
m.click()

driver.find_element_by_name("edtYouTubeURL").send_keys(url)
driver.find_element_by_name("edtStartTimeMinutes").send_keys(str(min_s_t))
driver.find_element_by_name("edtStartTimeSeconds").send_keys(str(sec_s_t))
driver.find_element_by_name("edtStopTimeMinutes").send_keys(str(min_e_t))
driver.find_element_by_name("edtStopTimeSeconds").send_keys(str(sec_e_t))
# driver.find_element_by_name("chkLoop").click()
# driver.find_element_by_name("chkAutoplay").click()
# driver.find_element_by_name("chkModestbranding").click()
# driver.find_element_by_name("chkLoop").click()
# driver.find_element_by_name("chkResponsive").click()
m = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/form/input[15]')
m.click()
pageSource = str(driver.page_source)
# print(pageSource)
m1=pageSource.index('src="https://www.youtube.com/embed')
print(pageSource.index('"&gt;&lt;'))
m2=pageSource[pageSource.index('src="https://www.youtube.com/embed'):].index('"&gt;&lt;')
link=pageSource[m1+5:m2+m1].replace('&amp;','&')
print(link)

# driver.implicitly_wait(20)
# /html/body/div[1]/div/div/section/div[1]/a[1]
# time.sleep(10)
target = driver.find_element_by_xpath('//a[@href]')
 
# Click the target to navigate to destination
target.click()    
# content = driver.find_ele/ment_by_css_selector('#page > div > div > section > div:nth-child(2) > button:nth-child(16)')
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div/div/section/div[1]/a[1]'))).click()

webbrowser.open_new_tab(link)
WebDriverWait(driver, 1000)


#page > div > div > section > div:nth-child(2) > button:nth-child(16)
#page > div > div > section > div:nth-child(2) > button:nth-child(16)

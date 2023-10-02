#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from bs4 import BeautifulSoup
import requests
#driver.maximize_window()


# In[5]:


driver=webdriver.Chrome()


# # Q 1)Write a python program which searches all the product under a particular product from www.amazon.in. The
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.

# In[4]:


var=input("enter the item:")


# # Q2.	In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: "Brand  
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and  “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.  
# 

# In[4]:


driver.get("https://www.amazon.in/")


# In[5]:


product=driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
product.send_keys('guitars')


# In[6]:


search=driver.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]')
search.click()


# In[7]:


#scrape all the product urls
product_urls=[]
start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        product_urls.append(i.get_attribute("href"))
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(3)    


# In[8]:


len(product_urls)


# In[33]:


for url in product_urls:
    driver.get(url)
    time.sleep(2)


# In[12]:


Brands=[]
price=[]
name_product=[]
replacement=[]
Availability=[]
delivery=[]


# In[10]:


for url in product_urls:
  driver.get(url)
  time.sleep(2)  
  
  try:
      brand=driver.find_element(By.XPATH,'//div[@id="productOverview_feature_div"]/div/table/tbody/tr[1]/td[2]')
      Brands.append(brand.text)
  except NoSuchElementException:
      Brands.append('-')


# In[11]:


len(Brands)


# In[14]:


for url in product_urls:
    driver.get(url)
    time.sleep(2)  
    
    try:
        np=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        name_product.append(np.text)
    except NoSuchElementException:
        name_product.append('-')
        
    try:
        pr=driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]')
        price.append(pr.text)
    except NoSuchElementException:
        price.append('-')         
    try:
        rep=driver.find_element(By.XPATH,'//div[@class="a-column a-span12 a-text-center icon-container scrollable-container celwidget"]/span')
        replacement.append(rep.text)
    except NoSuchElementException:
        replacement.append('-')   
        
    try:
        deli=driver.find_element(By.XPATH,'//div[@class="a-spacing-base"]/span[1]')
        delivery.append(deli.text)
    except NoSuchElementException:
        delivery.append('-')   
    try:
        avl=driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-success"]')
        Availability.append(avl.text)
    except NoSuchElementException:
        Availability.append('-')    


# In[16]:


len(price),len(name_product),len(Availability),len(delivery),len(replacement)


# In[18]:


import pandas as pd
df=pd.DataFrame({'BRAND_NAME':Brands,'Name_of_product':name_product,'PRICE':price,'Exp_Delivery':delivery,'Availability':Availability,'Replacement':replacement})
df


# # 4)Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “BrandName”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,¶
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV

# In[16]:


driver=webdriver.Chrome()


# In[24]:


driver.get("https://www.flipkart.com/")


# In[25]:


phone=driver.find_element(By.XPATH,'//input[@class="Pke_EE"]')
phone.send_keys('one plus nord mobile')


# In[27]:


search=driver.find_element(By.XPATH,'//button[@class="_2iLD__"]')
search.click()


# In[28]:


brand=[]
battery=[]
camera=[]
display=[]
ram=[]
price=[]


# In[29]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
for i in brand_tags:
    title=i.text
    brand.append(title)


# In[30]:


len(brand)


# In[31]:


battery_tags=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"][4]')
for i in battery_tags:
    title=i.text
    battery.append(title)


# In[32]:


len(battery)


# In[33]:


camera_tags=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"][3]')
for i in camera_tags:
    title=i.text
    camera.append(title)


# In[34]:


len(camera)


# In[35]:


display_tags=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"][2]')
for i in display_tags:
    title=i.text
    display.append(title)


# In[36]:


len(display)


# In[37]:


ram_tags=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"][1]')
for i in ram_tags:
    title=i.text
    ram.append(title)


# In[40]:


len(ram)


# In[39]:


price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for i in price_tags:
    title=i.text
    price.append(title)


# In[41]:


len(price)


# In[44]:


product_urls=[]
url_tags=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url_tags:
        product_urls.append(i.get_attribute("href"))


# In[45]:


product_urls


# In[42]:


df=pd.DataFrame({'BRAND_NAME':brand,'CAMERA':camera,'PRICE':price,'RAM':ram,'DISPLAY':display,'BATTERY':battery})
df


# # Q3.	Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.  

# In[4]:


driver.get("https:images.google.com")


# In[7]:


image=driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]')
image.send_keys('cars')


# In[8]:


search=driver.find_element(By.XPATH,'//button[@class="Tg7LZd"]')
search.click()


# In[28]:


for _ in range(20):
    driver.execute_script("window.scrollBY(0,100)")
    
    
images= driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]') 
img_urls=[]
for i in images:
    source=image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):#for checking first four letters 'http'
            img_urls.append(source)
            
            
for i in range(len(img_urls)):
    if i>10:
        breakBy.PATH,
    print("downloading {0} of {1} images" .format(i,10)) 
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\HP\Desktop\Fliprobo"+str(i)+".jpg","wb")
    file.write(response.content)


# # 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted from any YouTube Video.¶

# In[5]:


driver.get("https://www.youtube.com/")


# In[7]:


video=driver.find_element(By.XPATH,'//input[@class="ytd-searchbox"]')
video.send_keys('aradhya song telugu')


# In[8]:


search=driver.find_element(By.XPATH,'//button[@class="style-scope ytd-searchbox"]')
search.click()


# In[ ]:





# In[32]:


comm_name=[]
comment=[]
time=[]


# In[ ]:


for _ in range(20):
    driver.execute_script("window.scrollBY(0,100)")


# In[37]:


title_tags=driver.find_elements(By.XPATH,'//a[@id="author-text"]')
for i in title_tags:
    title=i.text
    comm_name.append(title)
    
comm_tags=driver.find_elements(By.XPATH,'//yt-formatted-string[@id="content-text"]')
for i in comm_tags:
    title=i.text
    comment.append(title)
    
time_tags=driver.find_elements(By.XPATH,'//yt-formatted-string[@class="published-time-text style-scope ytd-comment-renderer"]')
for i in time_tags:
    title=i.text
    time.append(title)    


# In[38]:


len(comm_name),len(comment),len(time)


# In[39]:


# import pandas as pd;
df=pd.DataFrame({'NAME':comm_name,'COMMENT':comment,'TIME':time})
df


# # Q5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps

# In[23]:


driver=webdriver.Chrome()


# In[24]:


driver.get("https://www.googlemaps.com")


# In[25]:


maps=driver.find_element(By.XPATH,'//input[@id="searchboxinput"]')
maps.send_keys('hyderabad')


# In[26]:


search=driver.find_element(By.XPATH,'//button[@class="mL3xi google-symbols"]')
search.click()


# In[30]:


try:
    url_string=driver.current_url
    print("URL Extracted: ",url_string)
    lat_lng=re.findall(r'@(.*)data',url_string)
    long_tude.split(lat_lng)


# # 6.	Write a program to scrap all the available details of best gaming laptops from digit.in.  

# In[43]:


driver=webdriver.Chrome()


# In[44]:


driver.get(("https://www.digit.in/"))


# In[46]:


lap=driver.find_element(By.XPATH,'//input[@id="woocommerce-product-search-field-0"]')
lap.send_keys('top 10 best laptops in india')


# In[ ]:


search=driver.find_element(By.XPATH,'//button[@class="icon-search-onclick"]')
search.click() 


# # 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.

# In[65]:


driver=webdriver.Chrome()


# In[6]:


driver.get("https://www.forbes.com")


# In[7]:


#search=driver.find_element(By.XPATH,'//button[@class="icon--search"]')
#search.click() 


# In[9]:


fob=driver.find_element(By.XPATH,'//div[@class="_69hVhdY4"]')
fob.send_keys('billionaries')


# In[64]:


search=driver.find_element(By.XPATH,'//button[@class="search-modal__submit"]')
search.click() 


# In[16]:


rank=[]
name=[]
Net_worth=[]
Age=[]
source=[]
teritory=[]
Citizenship=[]


# In[11]:


rank_tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"]/div[1]')
for i in rank_tags:
    title=i.text
    rank.append(title)


# In[13]:


len(rank)


# In[18]:


ti_tags=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"]/div[1]/span')
for i in ti_tags:
    title=i.text
    teritory.append(title)


# In[19]:


len(teritory)


# # Q9.	Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms from price, facilities and property description.  

# In[4]:


driver=webdriver.Chrome()


# In[5]:


driver.get("https://www.hostelworld.com/")


# In[9]:


hos=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/input')
hos.send_keys('london')


# In[10]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/ul/li[2]/button/div[2]/div[1]')
search.click() 


# In[11]:


hostel_name=[]
dist_centre=[]
ratings=[]
total_reviews=[]
pri_pvt=[]
dor_pri=[]


# In[14]:


ho_tags=driver.find_elements(By.XPATH,'//div[@class="property-name"]')
for i in ho_tags:
    title=i.text
    hostel_name.append(title)


# In[15]:


len(hostel_name)


# In[16]:


ra_tags=driver.find_elements(By.XPATH,'//span[@class="number"]')
for i in ra_tags:
    title=i.text
    ratings.append(title)


# In[17]:


len(ratings)


# In[25]:


d_tags=driver.find_elements(By.XPATH,'//span[@class="distance-description"]')
for i in d_tags:
    title=i.text
    dist_centre.append(title)


# In[26]:


len(dist_centre)


# In[35]:


tr_tags=driver.find_elements(By.XPATH,'//span[@class="keyword"]')
for i in tr_tags:
    title=i.text
    total_reviews.append(title)


# In[36]:


len(total_reviews)


# In[37]:


import pandas as pd;
df=pd.DataFrame({'HOSTEL_NAME':hostel_name,'RATINGS':ratings,'REVIEW':total_reviews})
df


# # rtr

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get("https://www.hostelworld.com/")


# In[6]:


hos=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/input')
hos.send_keys('london')


# In[7]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/ul/li[2]/button/div[2]')
search.click() 


# In[11]:


product_urls=[]
url=driver.find_elements(By.XPATH,'//a[@class="property-card-container"]')
for i in url:
    product_urls.append(i.get_attribute("href"))
time.sleep(3)   


# In[12]:


len(product_urls)


# In[13]:


product_urls


# In[14]:


for url in product_urls:
    driver.get(url)
    time.sleep(2)


# In[15]:


hostel_name=[]
dist_centre=[]
ratings=[]
total_reviews=[]
pri_pvt=[]
dor_pri=[]


# In[32]:


try:
    ho_tags=driver.find_elements(By.XPATH,'//div[@class="property-name"]')
    for i in ho_tags:
        title=i.text
        hostel_name.append(title)
except NoSuchElementException:
        Brands.append('-')


# In[ ]:


try:
    di_tags=driver.find_elements(By.XPATH,'//span[@class="distance-description"]')
    for i in di_tags:
        title=i.text
        dist_centre.append(title)
except NoSuchElementException:
        dist_centre.append('-')


# In[ ]:


d_tags=driver.find_elements(By.XPATH,'//span[@class="distance-description"]')
for i in d_tags:
    title=i.text
    dist_centre.append(title)


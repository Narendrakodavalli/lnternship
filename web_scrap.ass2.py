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


# In[3]:


driver=webdriver.Chrome()


# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data

# In[92]:


#opening the shinepage on automated chrome browser
driver.get("https://www.shine.com/")


# In[93]:


#entering designation and location as req

designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Analyst')


# In[94]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys("Bangalore")


# In[95]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[9]:


#create emoty list
#job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[111]:


#scrapng job titile from the given page
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags:
    title=i.text
    job_title.append(title)
    


# In[112]:


print(len(job_title))


# In[103]:


#scrapng job location from the given page
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[104]:


print(len(job_location))


# In[101]:


#scrapng job company from the given page//
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[102]:


print(len(company_name))


# In[105]:


#scrapng job experience from the given page
experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)


# In[106]:


print(len(experience_required))


# In[108]:


# import pandas as pd;
df=pd.DataFrame({'Company_name':company_name,'Location':job_location,'Experience':experience_required})
df.head(10)

# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data. This task will be done in following steps: 
1.	First get the webpage https://www.shine.com/ 
2.	Enter “Data Scientist” in “Job title, Skills”  field and enter “Bangalore” in “enter the location” field. 
3.	Then click the search  button. 
4.	Then scrape the data for the first 10 jobs results you get. 
5.	Finally create a dataframe of the scraped data. 

# In[75]:


driver=webdriver.Chrome()


# In[76]:


#opening the shinepage on automated chrome browser
driver.get("https://www.shine.com/")


# In[77]:


#entering designation and location as req

designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Scientist')


# In[78]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys("Bangalore")


# In[79]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[80]:


#create emoty list
job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[81]:


#scrapng job titile from the given page
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags:
    title=i.text
    job_title.append(title)


# In[82]:


print(len(job_title))


# In[83]:


#scrapng job location from the given page
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[84]:


print(len(job_location))


# In[85]:


#scrapng job company from the given page//
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)


# In[86]:


print(len(company_name))


# In[87]:


#scrapng job experience from the given page
experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)


# In[88]:


print(len(experience_required))


# In[90]:


# import pandas as pd;
df=pd.DataFrame({'Title':job_title,'Company_name':company_name,'Location':job_location,'Experience':experience_required})
df.head(10)


# # Q3: In this question you have to scrape data using the filters available on the webpage
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[3]:


driver=webdriver.Chrome()


# In[4]:


#opening the shinepage on automated chrome browser
driver.get("https://www.shine.com/")


# In[24]:


#entering designation and location as req

designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Scientist')


# In[25]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Delhi/NCR')


# In[27]:


search=driver.find_element(By.CLASS_NAME," btn btn-secondary undefined")
search.click()


# In[136]:


salary=driver.find_element(By.XPATH,'//li[@class="filter_filter_lists_items__wlFfo"]')
salary.send_keys('3 To 6 Lakh (128)')                          


# In[121]:


#create emoty list
job_title=[]
job_location=[]
company_name=[]
salary_required=[]


# In[122]:


#scrapng job titile from the given page
title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for i in title_tags:
    title=i.text
    job_title.append(title)


# In[123]:


print(len(job_title))


# In[125]:


#scrapng job location from the given page
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location)


# In[126]:


print(len(job_location))


# In[ ]:





# In[ ]:





# In[ ]:





# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 6. Brand
# 7. Product Description
# 8. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrapeTo scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url : https://www.flipkart.com/
# 2. Enter “sunglasses” in the search field where “search for products, brands and more” is written and click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the required data as usual.

# In[244]:


driver=webdriver.Chrome()


# In[245]:


driver.get("https://www.flipkart.com/")


# In[246]:


item=driver.find_element(By.CLASS_NAME,"Pke_EE")
item.send_keys('sunglasses')


# In[247]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[248]:


brand=[]
Product=[]
Price=[]
Discount=[]


# In[249]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    title=i.text
    brand.append(title)


# In[250]:


print(len(brand))


# In[251]:


price_tags=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
for i in price_tags:
    title=i.text
    Price.append(title)


# In[252]:


print(len(Price))


# In[253]:


Product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Product_tags:
    title=i.text
    Product.append(title)


# In[254]:


print(len(Product))


# In[255]:


discount_tags=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
for i in discount_tags:
    title=i.text
    Discount.append(title)


# In[256]:


print(len(Discount))


# In[257]:


brands=[]


# In[260]:


start=0
end=3
for page in range(start,end):
    brand_tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tag:
            title=i.text
            brands.append(title)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)
    


# In[261]:


len(brands)


# In[262]:


print(brands[:100])


# In[263]:


Prices=[]


# In[300]:


start=0
end=3
for page in range(start,end):
    price_tag=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
    for i in price_tag:     
          Prices.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[301]:


len(Prices)


# In[281]:


print(Prices[:100])


# In[237]:


Products=[]


# In[288]:


start=0
end=3
for page in range(start,end):
    product_tag=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in product_tag:     
          Products.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)

    


# In[291]:


print(Products[:100])


# In[293]:


Discounts=[]


# In[294]:


start=0
end=3
for page in range(start,end):
    discount_tag=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
    for i in discount_tag:     
          Discounts.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[296]:


print(Discounts[:100])


# In[ ]:


# import pandas as pd;
df=pd.DataFrame({'BRAND':brands,'PROD_DES':Products,'PRICE':Prices,'DISCOUNT':Discounts})
df.

As shown in the above page you have to scrape the tick marked attributes. These are:
1. Rating
2. Review summary
3. Full review
4. You have to scrape this data for first 100reviews.
Note: All the steps required during scraping should be done through code only and not manually.
Q6:# 5)Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART

# In[4]:


driver=webdriver.Chrome()


# In[7]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketce=FLIPKART/")


# In[8]:


Ratg=[]


# In[10]:


ratg_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in ratg_tags:
    title=i.text
    Ratg.append(title)


# In[11]:


print(Ratg)


# In[12]:


R_sum=[]


# In[13]:


Rsum_tags=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in Rsum_tags:
    title=i.text
    R_sum.append(title)                               


# In[14]:


print(R_sum)


# In[15]:


f_rew=[]


# In[22]:


frew_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in frew_tags:
    title=i.text
    f_rew.append(title)


# In[23]:


print(f_rew)


# In[25]:


Rating=[]


# In[28]:


start=0
end=10
for page in range(start,end):
    rating_tag=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tag:     
          Rating.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[64]:


print(len(Rating))


# In[32]:


print(Rating[:100])


# In[52]:


Review=[]


# In[63]:


start=0
end=10
for page in range(start,end):
    ratg_tag=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in ratg_tag:     
          Review.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[60]:


print(len(Review))


# In[55]:


print(Review[:100])


# In[44]:


full_review=[]


# In[45]:


start=0
end=10
for page in range(start,end):
    full_tag=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_tag:     
          full_review.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[59]:


print(len(full_review))


# In[46]:


print(full_review[:100])


# In[62]:


# import pandas as pd;
df=pd.DataFrame({'RATING':Rating,'REVIEW_SUMM':Review,'FULL_REVIEW':full_review})
df.head(100)


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

# In[89]:


driver=webdriver.Chrome()


# In[90]:


driver.get("https://www.flipkart.com/")


# In[91]:


item=driver.find_element(By.CLASS_NAME,"Pke_EE")
item.send_keys('sneakers')


# In[92]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[94]:


brand=[]
Product=[]
Price=[]
Discount=[]


# In[95]:


brand_tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tag:
    title=i.text
    brand.append(title)


# In[96]:


print(len(brand))


# In[98]:


Product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Product_tags:
    title=i.text
    Product.append(title)


# In[74]:


print(len(Product))


# In[99]:


price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags:
    title=i.text
    Price.append(title)


# In[100]:


print(len(Price))


# In[101]:


Brands=[]


# In[107]:


start=0
end=3
for page in range(start,end):
    brands_tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brands_tag:
            title=i.text
            Brands.append(title)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[116]:


print(len(Brands[:100]))


# In[104]:


Prices=[]


# In[105]:


start=0
end=3
for page in range(start,end):
    prices_tag=driver.find_elements(By.XPATH,'//div[@class="_3I9_wc"]')
    for i in prices_tag:     
          Prices.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[117]:


print(len(Prices[:100]))


# In[113]:


Products=[]


# In[114]:


start=0
end=3
for page in range(start,end):
    product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in product_tags:     
          Products.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[118]:


print(len(Products[:100]))


# In[119]:


# import pandas as pd;
df=pd.DataFrame({'Brand':Brands,'Product_des':Products,'Price':Prices})
df.head(100)


# # Q7: Go to webpage https://www.amazon.in/ 
# Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[5]:


driver=webdriver.Chrome()


# In[ ]:


driver.get("https://www.amazon.in/")


# In[ ]:


item=driver.find_element(By.CLASS_NAME,"nav-search-field ")
item.send_keys('Laptop')


# In[ ]:





# In[ ]:





# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on Top Quotes3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[99]:


driver=webdriver.Chrome()


# In[100]:


driver.get("https://www.azquotes.com/")#//a[@class="title"]


# In[101]:


author=[]
quote=[]
ty_quote=[]


# In[120]:


qu_tag=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in qu_tag:
    title=i.text
    quote.append(title)


# In[121]:


print(len(quote))


# In[69]:


aut_tag=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in aut_tag:
    title=i.text
    author.append(title)


# In[70]:


print(len(author))


# In[71]:


ty_tag=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in ty_tag:
    title=i.text
    ty_quote.append(title)


# In[72]:


print(len(ty_quote))


# In[73]:


AUTHOR=[]
QUOTE=[]
TYPE_QUOTE=[]


# In[86]:


start=0
end=10
for page in range(start,end):
    auth_tag=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in auth_tag:
            title=i.text
            AUTHOR.append(title)
    next_button=driver.find_element(By.XPATH,'//li[@class="next inactive"')
    next_button.click()
    time.sleep(3)


# In[81]:


print(len(AUTHOR))


# In[32]:


start=0
end=10
for page in range(start,end):
    quo_tag=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quo_tag:
            title=i.text
            QUOTE.append(title)
    next_button=driver.find_element(By.XPATH,'//li[@class="next inactive"]')
    next_button.click()
    time.sleep(3)


# In[33]:


print(len(QUOTE))


# In[34]:


start=0
end=10
for page in range(start,end):
    ty_tag=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in ty_tag:
            title=i.text
            TYPE_QUOTE.append(title)
    next_button=driver.find_element(By.XPATH,'//li[@class="next inactive"]')
    next_button.click()
    time.sleep(3)


# In[35]:


print(len(TYPE_QUOTE))


# In[ ]:





# In[ ]:





# # Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/. 
#  
# This task will be done in following steps: 
# 1.	First get the webpagehttps://www.jagranjosh.com/ 
# 2.	Then You have to click on the GK option 
# 3.	Then click on the List of all Prime Ministers of India 
# 4.	Then scrap the mentioned data and make theDataFrame. 
# 

# In[81]:


driver=webdriver.Chrome()


# In[82]:


driver.get("https://www.jagranjosh.com/")


# In[83]:


Name=[]
Born_Dead=[]
Term_of_office=[]
Remarks=[]


# In[79]:


Na_tag=driver.find_elements(By.XPATH,'//td')
for i in Na_tag:
    title=i.text
    Name.append(title)


# In[80]:


print(len(Name))


# In[76]:


Name


# In[85]:


te_tag=driver.find_elements(By.XPATH,'\\td[3]')
for i in te_tag:
    title=i.text
    Term_of_office.append(title)


# In[71]:


Name


# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price) from https://www.motor1.com/ 
#  
# This task will be done in following steps: 
# 1.	First get the webpage https://www.motor1.com/ 
# 2.	Then You have to type in the search bar ’50 most expensive cars’ 
# 3.	Then click on 50 most expensive cars in the world.. 
# 4.	Then scrap the mentioned data and make the dataframe. 
# 

# In[30]:


driver=webdriver.Chrome()


# In[31]:


driver.get("https://www.motor1.com/ ")


# In[36]:


most_exp=[]


# In[37]:


most_tag=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in most_tag:
    title=i.text
    most_exp.append(title)


# In[38]:


len(most_exp)


# In[39]:


price=[]


# In[40]:


price_tag=driver.find_elements(By.XPATH,'//strong')
for i in price_tag:
    title=i.text
    price.append(title)


# In[42]:


print(len(price))


# In[43]:


print(price)


# In[46]:


import pandas as pd;
df=pd.DataFrame({'Car_name':most_exp,'PRICE':price})
df


# In[ ]:





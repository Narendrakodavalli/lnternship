#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[3]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


# 1.	Scrape  	the  	details  of  	most  	viewed  videos  on  	YouTube  	from  	Wikipedia.  	Url 
#  = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details:  A) Rank   
# B)	Name   
# C)	Artist   
# D)	Upload date   
# E)	Views   

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[6]:


Name=[]
Rank=[]
Artist=[]
Upload_date=[]
Views=[]


# In[7]:


names = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[2]')
for name in names:
    Name.append(name.text)


# In[8]:


len(Name)


# In[9]:


artists = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[3]')
for artist in artists:
    Artist.append(artist.text)


# In[10]:


len(Artist)


# In[11]:


up_dates = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[5]')
for up_dat in up_dates:
    Upload_date.append(up_dat.text)


# In[12]:


len(Upload_date)


# In[13]:


views = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[4]')
for view in names:
    Views.append(view.text)


# In[14]:


len(Views)


# In[15]:


ranks = driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[1]')
for rank in names:
    Rank.append(rank.text)


# In[16]:


len(Rank)


# In[19]:


df=pd.DataFrame({"Rank":Rank,"Names":Name,"Artists":Artist,
                "Upload_dates":Upload_date,"Views":Views})
df


# 2.	Scrape the details team India’s international fixtures from bcci.tv.   
# Url = https://www.bcci.tv/.   
# You need to find following details:   
# A)	Series   
# B)	Place   
# C)	Date   
# D)	Time   
# Note: - From bcci.tv home page you have reach to the international fixture page through code.

# In[38]:


driver=webdriver.Chrome()


# In[39]:


driver.get(" https://www.bcci.tv/")


# In[41]:


Series=[]
Place=[]
Date=[]
Time=[]


# In[42]:


series = driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for serie in series:
    Series.append(serie.text)


# In[43]:


len(Series)


# In[44]:


places=driver.find_elements(By.XPATH,'//div[@class="match-place ng-scope"]')
for place in places:
    Place.append(place.text)


# In[45]:


len(Place)


# In[46]:


dates=driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for date in dates:
    Date.append(date.text)


# In[47]:


len(Date)


# In[49]:


times=driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for time in times:
    Time.append(time.text)


# In[50]:


len(Time)


# In[51]:


df=pd.DataFrame({"Series":Series,"Place":Place,
                "Date":Date,"Time":Time})
df


# 3.	Scrape the details of State-wise GDP of India from statisticstime.com.   
# Url = http://statisticstimes.com/   
# You have to find following details: A) Rank   B) State   
# C)	GSDP(18-19)- at current prices   
# D)	GSDP(19-20)- at current prices   
# E)	Share(18-19)   
# F)	GDP($ billion)   
# Note: - From statisticstimes home page you have to reach to economy page through code.   
# 

# 4.	Scrape the details of trending repositories on Github.com.   
# Url = https://github.com/   
# You have to find the following details:   
# A)	Repository title   
# B)	Repository description   
# C)	Contributors count   
# D)	Language used   
# Note: - From the home page you have to click on the trending option from Explore menu through code.   
# 

# In[4]:


driver=webdriver.Chrome()


# In[5]:


driver.get("https://github.com/")


# In[11]:


element=driver.find_element(By.XPATH,'//li[@class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item"]')
drp=Select(element)


# In[ ]:


drp.select_by_visible_text('Trending')


# In[12]:


Repy_title=[]
Repy_dn=[]
Co_cnt=[]
Lan_us=[]


# In[13]:


repos = driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]')
for repo in repos:
    Repy_title.append(repo.text)


# In[14]:


len(repos)


# In[16]:


repdes = driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
for repod in repdes:
    Repy_dn.append(repod.text)


# In[17]:


len(repdes)


# In[19]:


coc_cnt = driver.find_elements(By.XPATH,'//span[@class="d-inline-block mr-3"]')
for rep in coc_cnt:
    Co_cnt.append(rep.text)


# In[20]:


len(coc_cnt)


# In[22]:


lan_u = driver.find_elements(By.XPATH,'//span[@itemprop="programmingLanguage"]')
for lan in lan_u:
    Lan_us.append(lan.text)


# In[23]:


len(Lan_us)


# 5.	Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/  You have to find the following details:   
# A)	Song name   
# B)	Artist name   
# C)	Last week rank   
# D)	Peak rank   
# E)	Weeks on board   
#  
#       Note: - From the home page you have to click on the charts option then hot 100-page link through code.   
#    
# 

# In[6]:


driver=webdriver.Chrome()


# In[7]:


driver.get("https:/www.billboard.com/")


# In[8]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[3]/div/nav/ul/li[4]/a')
search.click()


# In[17]:


song_name=[]
Artist_name=[]
last_week_rank=[]
peak_rank=[]
weeks_on_board=[]


# In[10]:


s_name = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]//h3')
for s_nam in s_name:
    song_name.append(s_nam.text)


# In[11]:


len(song_name)


# In[13]:


wob = driver.find_elements(By.XPATH,'//div[@class="o-chart-results-list-row-container"]//li[6]')
for w_b in wob:
    weeks_on_board.append(w_b.text)


# In[14]:


len(weeks_on_board)


# In[18]:


low = driver.find_elements(By.XPATH,'//li[@class="o-chart-results-list__item // a-chart-color u-width-72 u-width-55@mobile-max u-width-55@tablet-only lrv-u-flex lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light u-background-color-white-064@mobile-max u-hidden@mobile-max"][1]')
for l_w in low:
    last_week_rank.append(l_w.text)


# In[19]:


len(last_week_rank)


# In[22]:


pk = driver.find_elements(By.XPATH,'//li[@class="o-chart-results-list__item // a-chart-bg-color a-chart-color u-width-72 u-width-55@mobile-max u-width-55@tablet-only lrv-u-flex lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-background-color-grey-lightest lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light u-hidden@mobile-max"][2]')
for p_k in pk:
    peak_rank.append(p_k.text)


# In[23]:


len(peak_rank)


# In[25]:


as_name = driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]//li[1]/span')
for a_s in as_name:
    Artist_name.append(a_s.text)


# In[26]:


len(Artist_name)


# 6.	Scrape the details of Highest selling novels.   
# A)	Book name   
# B)	Author name   
# C)	Volumes sold   
# D)	Publisher   
# E)	Genre   
#  
#       Url - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare  
# 

# In[3]:


driver=webdriver.Chrome()


# In[4]:


driver.get("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare  ")


# In[5]:


title=[]
author=[]
volum_sold=[]
publisher=[]
genre=[]


# In[6]:


tit_le = driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]//tr/td[2]')
for tit in tit_le:
    title.append(tit.text)


# In[7]:


len(title)


# In[9]:


autho_r = driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]//tr/td[3]')
for aut in autho_r:
    author.append(aut.text)


# In[10]:


len(author)


# In[11]:


volum_so = driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]//tr/td[4]')
for vol in volum_so:
    volum_sold.append(vol.text)


# In[12]:


len(volum_sold)


# In[14]:


pub_ser = driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]//tr/td[5]')
for pub in pub_ser:
    publisher.append(pub.text)


# In[15]:


len(publisher)


# In[16]:


gen_ser = driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]//tr/td[6]')
for gen in gen_ser:
    genre.append(gen.text)


# In[17]:


len(genre)


# In[18]:


#making data frame
df=pd.DataFrame({"Title":title,"Author":author,"Volum_sold":volum_sold,
                "Publisher":publisher,"Genre":genre})
df


# 7.	Scrape the details most watched tv series of all time from imdb.com.   
# Url = https://www.imdb.com/list/ls095964455/ You have to find the following details:   
# A)	Name   
# B)	Year span   
# C)	Genre   
# D)	Run time   
# E)	Ratings   
# F)	Votes   

# In[19]:


driver=webdriver.Chrome()


# In[20]:


driver.get("https://www.imdb.com/list/ls095964455/ ")


# In[21]:


Movie_name=[]
Genre=[]
year_span=[]
run_time=[]
ratings=[]
votes=[]


# In[22]:


mov_le = driver.find_elements(By.XPATH,'//h3[@class="lister-item-header"]//a')
for mov in mov_le:
    Movie_name.append(mov.text)


# In[23]:


len(Movie_name)


# In[25]:


year_s = driver.find_elements(By.XPATH,'//h3[@class="lister-item-header"]//span[2]')
for year in year_s:
    year_span.append(year.text)


# In[26]:


len(year_span)


# In[28]:


genr_e = driver.find_elements(By.XPATH,'//span[@class="genre"]')
for gen in genr_e:
    Genre.append(gen.text)


# In[29]:


len(Genre)


# In[31]:


run_t = driver.find_elements(By.XPATH,'//span[@class="runtime"]')
for run in run_t:
    run_time.append(run.text)


# In[32]:


len(run_time)


# In[34]:


rat_t = driver.find_elements(By.XPATH,'//div[@class="ipl-rating-star small"]//span[2]')
for rat in rat_t:
    ratings.append(rat.text)


# In[35]:


len(ratings)


# In[37]:


vot_t = driver.find_elements(By.XPATH,'//span[@name="nv"]')
for vot in vot_t:
    votes.append(vot.text)


# In[38]:


len(votes)


# In[40]:


#making data frame
df=pd.DataFrame({"Movie_name":Movie_name,"year_span":year_span,"Genre":Genre,"run_time":run_time,
                "ratings":ratings,"votes":votes})
df


# 8.	Details of Datasets from UCI machine learning repositories.   
# Url = https://archive.ics.uci.edu/  You have to find the following details:   
# A)	Dataset name   
# B)	Data type   
# C)	Task   
# D)	Attribute type   
# E)	No of instances   
# F)	No of attribute G) Year   
#  
#       Note: - from the home page you have to go to the Show All Dataset page through code.   
# 

# In[40]:


driver=webdriver.Chrome()


# In[41]:


driver.get("https://archive.ics.uci.edu/  ")


# In[42]:


data_set = driver.find_element(By.XPATH,'//a[@class="btn-primary btn"]')
data_set.click()


# In[43]:


data_name=[]
data_type=[]
task=[]
attribute_type=[]
no_instances=[]
no_attributes=[]
year=[]


# In[44]:


dat_nam = driver.find_elements(By.XPATH,'//a[@class="link-hover link text-xl font-semibold"]')
for nam in dat_nam:
    data_name.append(nam.text)


# In[45]:


len(data_name)


# In[46]:


dat_typ = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]//div[2]')
for typ in dat_typ:
    data_type.append(typ.text)


# In[47]:


len(data_type)


# In[48]:


tas = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]//div[1]/span[1]')
for tk in tas:
    task.append(tk.text)


# In[49]:


len(task)


# In[50]:


no_ins = driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]')
for inst in no_ins:
    no_instances.append(inst.text)


# In[51]:


len(no_instances)


# In[52]:


time.sleep(5)


# In[53]:


yar_d = driver.find_elements(By.XPATH,'//tbody[@class="border"]//tr/td[3]')
for yr in yar_d:
    year.append(yr.text)


# In[54]:


len(year)


# In[56]:


attrib = driver.find_elements(By.XPATH,'//tbody[@class="border"]//tr/td[3]')
for att in attrib:
    no_attributes.append(att.text)


# In[57]:


len(no_attributes)


# In[58]:


attr_typ = driver.find_elements(By.XPATH,'//tbody[@class="border"]//tr/td[2]')
for aty in attr_typ:
    attribute_type.append(aty.text)


# In[59]:


len(attribute_type)


# In[60]:


#making data frame
df=pd.DataFrame({"data_name":data_name,"data_type":data_type,"task":task,"attribute_type":attribute_type,"no_instances":no_instances,
                "no_attributes":no_attributes,"year":year})
df


# In[ ]:





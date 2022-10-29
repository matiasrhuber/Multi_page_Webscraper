#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup

countries = ['united-states','brazil','germany']

### Yield Curve Data collection ###
US_yc = []
BR_yc = []
GER_yc = []

for country in countries:
    source = requests.get(f'http://www.worldgovernmentbonds.com/country/{country}').text

    soup = BeautifulSoup(source, 'lxml')
    soup = soup.find('div', class_='w3-responsive')

    for date in soup.find_all('tr', class_='w3-border-bottom'):
        yc_rate = date.find('td', class_='w3-center w3-extralight-gray').b.text
        if country == 'united-states':
            US_yc.append(yc_rate)
        if country == 'brazil':
            BR_yc.append(yc_rate)
        if country == 'germany':
            GER_yc.append(yc_rate)

### Trading Economics Data ###
### Interest Rate ###
US_int = []
BR_int = []
GER_int = []

### Stock Market ###
US_sm = []
BR_sm = []
GER_sm = []

### Currency ###
US_cu = []
BR_cu = []
GER_cu = []

### GDP Growth Rate ###
US_GDP = []
BR_GDP = []
GER_GDP = []

### Unemployment Rate ###
US_jobs = []
BR_jobs = []
GER_jobs = []

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

for country in countries:
    source = requests.get(f'https://tradingeconomics.com/{country}/forecast', headers=headers).text

    soup = BeautifulSoup(source, 'lxml')
    soup = soup.find('div', id='ctl00_ContentPlaceHolder1_ctl01_Panel1')
    soup_table = soup.find_all('td', class_='table-value')

    if country == 'united-states':
        for currency in soup_table[0:5]:
            US_cu.append(currency.text.strip())
        for stock_market in soup_table[6:11]:
            US_sm.append(stock_market.text.strip())
        for interest_rate in soup_table[48:53]:
            US_int.append(interest_rate.text.strip())
        for GDP in soup_table[18:23]:
            US_GDP.append(GDP.text.strip())
        for job in soup_table[30:35]:
            US_jobs.append(job.text.strip())
    
    if country == 'brazil':
        for currency in soup_table[0:5]:
            BR_cu.append(currency.text.strip())
        for stock_market in soup_table[6:11]:
            BR_sm.append(stock_market.text.strip())
        for interest_rate in soup_table[48:53]:
            BR_int.append(interest_rate.text.strip())
        for GDP in soup_table[18:23]:
            BR_GDP.append(GDP.text.strip())
        for job in soup_table[30:35]:
            BR_jobs.append(job.text.strip())
    
    if country == 'germany':
        for currency in soup_table[0:5]:
            GER_cu.append(currency.text.strip())
        for stock_market in soup_table[6:11]:
            GER_sm.append(stock_market.text.strip())
        for interest_rate in soup_table[48:53]:
            GER_int.append(interest_rate.text.strip())
        for GDP in soup_table[18:23]:
            GER_GDP.append(GDP.text.strip())
        for job in soup_table[30:35]:
            GER_jobs.append(job.text.strip())
# %%
US_jobs
# %%
soup_table[0:5]
# %%
US_sm
# %%

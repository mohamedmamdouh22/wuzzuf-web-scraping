import requests
import pandas as pd
import math
from bs4 import BeautifulSoup
# job_title=input("Enter job title:")
page=requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q=python&start=0')
soup=BeautifulSoup(page.content,'lxml')
n=soup.find('strong').text.strip()

jobs_list=[]
def main(page):
    soup=BeautifulSoup(page.content,'lxml')
    jobs=soup.find_all('div',{'class':'css-pkv5jc'}) # getting all the jobs from the website
    def get_jobs(job):
        try:
            title=job.find('h2',{'class':'css-m604qf'}).text.strip()
        except:
            title='not found'
        try:
            link='https://wuzzuf.net'+job.find('h2',{'class':'css-m604qf'}).find('a',{'class':'css-o171kl'}).attrs['href']
        except:
            link='not found'
        try:
            company=job.find('a',{'class':'css-17s97q8'}).text.strip().split()[0]
        except:
            company='not found'
        try:
            location=job.find('span',{'class':'css-5wys0k'}).text.strip()
        except:
            location='not found'
        try:
            posted=job.find('div',{'class':'css-d7j1kk'}).find('div').text.strip()
        
        except:
            posted='not found'
        try:
            job_type=job.find('span',{'class':'eoyjyou0'}).text.strip()
        except:
            job_type='not found'
        try:
            exp=job.find('div',{'class':'css-y4udm8'}).find_all('div')[1].text
        except:
            exp='not found'
        jobs_list.append(
            {
                'Title':title,
                'Company':company,
                'Location':location,
                'Post date':posted,
                'Job_type':job_type,
                # 'Salary':salary,
                'Skills':exp,
                'Link':link,
            }
        )
    for i in range(len(jobs)):
        get_jobs(jobs[i])
    df=pd.DataFrame(jobs_list)
    df.to_csv('jobs.csv')
    # print(df)
    
    # get_jobs(jobs[0])
n=math.ceil(int(n)/15)

for i in range(n):
    page=requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={i}')
    main(page)
    print('page',i+1,'done')
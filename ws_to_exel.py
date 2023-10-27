import requests,openpyxl
import time
from bs4 import BeautifulSoup


excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet=excel.active
sheet.title='Jobs openings'
print(excel.sheetnames)

sheet.append(['Job Title','Company Name', 'Skills','Link','Time'])


print("Put some skills that you dont know.")
unfamiliar= input('>')
print("Filtering out ",unfamiliar)

def find_jobs():
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=django&txtLocation=').text
    soup=  BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li' , class_='clearfix job-bx wht-shd-bx')

    
    for index,job in enumerate(jobs):

        pub_date=job.find('span',class_='sim-posted').span.text
        if 'few' in pub_date:
            job_name=job.find('header',class_='clearfix').h2.a.text.replace('  ','')
            company_name=job.find('h3',class_='joblist-comp-name').text.replace('  ','')
            skills=job.find('span',class_='srp-skills').text.replace('  ','')
            more_info=job.header.h2.a['href']

            if unfamiliar not in skills:
                sheet.append([job_name,company_name, skills,more_info,pub_date])
                
                print('File saved.')
    excel.save('JobSearchs.xlsx')
                   

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait+60)


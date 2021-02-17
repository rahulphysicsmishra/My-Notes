from bs4 import BeautifulSoup
import requests

print("Input the skills you don't want in job posting")
Unwanted_skills = input('>> ')

def job_filter():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    # print(jobs.text.strip())
    for job in jobs:
        posted = job.find('span', class_='sim-posted').text.strip()
        if 'days' in posted:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            #print(company_name)
            skills = job.find('span', class_='srp-skills').text.strip()
            #print(skills)
            more_info = job.header.h2.a['href']
            if Unwanted_skills not in skills:
                print(f"company name: {company_name}")
                print(f"required skills: {skills}")
                print(f"date-posted: {posted}")
                print(f"more info: {more_info}")
                print("\n")

job_filter()
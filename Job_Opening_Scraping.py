from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from time import time
import datetime
import os


def find_job(job_title, location):

    start_time = time()
    requests = 0

    # Declaring empty lists to store the data
    titles = []
    companies = []
    links = []
    dates = []

    # 15 jobs/page
    # Page1 -> page=0 | Page2 -> page=10 | Page3 -> page=20 and etc
    for page in range (0,50,10):

        url = f'https://sg.indeed.com/jobs?q={job_title}&l={location}&sort=date&start={page}'
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Control the crawling rate, avoid hammering server w/ multiple requests/sec and IP banned
        # sleep(), pause the loops rate & randomly generates int within specified interval
        sleep(randint(1,2))
        requests = requests + 1
        elapsed_time = time() - start_time
        print(f'Request: {requests}; Frequency: {requests/elapsed_time} requests/s')

        # Select all the 14 jobs containers (JobCard) from a single page
        jobs_containers = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')

        # For every job in these 14 jobs
        for container in jobs_containers:
            # Extract the Job Title
            title = container.h2.a.text
            title = title.replace('\n', '')
            titles.append(title)

            # Extract the Company Name
            company = container.div.find('span', class_ = 'company').text
            company = company.replace('\n', '')
            companies.append(company)

            # Extract the Application URL
            link = container.find('a')['href']
            main_site = 'https://sg.indeed.com'
            link = main_site + link
            links.append(link)

            # Extract the Posted Date
            date = container.find('span', class_ = 'date').text
            dates.append(date)
        
    return titles, companies, links, dates

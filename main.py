# import libraries
import requests
from bs4 import BeautifulSoup
import time

# Asking user input to filter out unowned skills
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering Out {unfamiliar_skill}')


def find_jobs():
    # Using the Requests Library to see a Website's HTML
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'html.parser')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    # Looping through jobs objects
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text
        # Jobs Filtration by publish date
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_link = job.header.h2.a['href']
            # Jobs Filtration by owned skills
            if unfamiliar_skill not in skills:
                # Storing the jobs paragraph in text files
                with open(f'posts/{index}.text', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Skills: {skills.strip()}\n')
                    f.write(f'More Link: {more_link}')
                print(f'File Saved : {index}')


if __name__ == "__main__":
    # Setting up the Project to scrape every 10 minutes
    while True:
        find_jobs()
        time_waits = 10
        print(f'Waiting {time_waits} minutes.....')
        time.sleep(time_waits * 60)


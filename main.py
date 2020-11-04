import requests
import pandas as pd
import datetime
import os
from Job_Opening_Scraping import find_job

# Input the Job Title #
titles, companies, links, dates = find_job('data scientist', 'singapore')

# Add in export datetime with filename
# For example, timestamp 04112020-145301 indicates 4th Nov 2020, 2:53:01 PM 
now = datetime.datetime.now()
timestamp = str(now.strftime("%d%m%Y-%H%M%S"))

jobs = pd.DataFrame({'title':titles, 'company':companies, 'link':links, 'date':dates})
filename = "JobsExtractOn_" + timestamp + ".xlsx"
jobs.to_excel(filename, index=False)

#! /usr/bin/env/ python
"""
# Clasificadosonline.com Job Search Script
# This will scrape Clasificadosonline.com for jobs
#
"""
# Do the imports: Dictionary is from the file dictionary.py
from dictionary import *
from bs4 import BeautifulSoup as soup
import requests

# create the scraper class
class classifiedScraper(object):

# Initialization:
# run your functions here or apply to a global variable object
# print len and the like to the object can be applied here
# Init right now only got two functions the scraper and the file handler (writer)
    def __init__(self):
        self._scraper()
        self._file_handler()

# leaving the print statement as a final error check or Done! This outputs the
# complete job name. There may be duplicate here, so it would be good to do an
# if / else loop somwhere
        print(len(job_list))

# Scraper function to be used on __init__
    def _scraper(self,*args,**kwargs):
        global job_list

        try:
            headers = requests.utils.default_headers()
            headers.update({'User-Agent': 'Mozilla/5.0'})
            pueblo_list = [x for x in pueblos.values()]
            # Url Variables
            general_url = "https://www.clasificadosonline.com"
            general_job_url = "https://www.clasificadosonline.com/UDJobsListing.asp?"
            search_page_url = "https://www.clasificadosonline.com/Jobs.asp"
            try:
                job_list = []
                for index, name in enumerate(pueblo_list,start=0):
                    jobs_cat = "JobsCat=%{}".format(25)
                    txkey_cat = "&txkey={}".format("")
                    pueblo_cat = "&Pueblo={}".format(name)
                    submit_cat = "&Submit=Buscar+-+GO"
                    offset_cat = "&offset=".format("")
                    job_search_url = (general_job_url+jobs_cat+pueblo_cat+txkey_cat+submit_cat+offset_cat)

                    response = requests.get(job_search_url,headers=headers)
                    page_soup = soup(response.content,"html.parser")

                    # Applying the soup to some variables
                    job_anchor_list = page_soup.find_all("td",{"class":"Ver14nounder"})
                    category_list = page_soup.find_all("select",{"class":"Ver14"})

                    for item in job_anchor_list:
                        try:
                            jobs_anchor = item.find("a",{"class":"Ver14nounder"})
                            href_list = jobs_anchor.get("href")
                            job_url = general_url + href_list
                            jobs = jobs_anchor.get_text()
                            if jobs or job_url not in job_list:
                                job_list.append(jobs)
                                job_list.append(job_url)

                            else: continue
                        except Exception as e:
                            print("There was an error: ",e)

                    # Check & close the response
                    print("Soup done!", name)
                    response.close()

            except Exception as e:
                print("There was an error",e)

            # Job search url variable, have tried to do some other type of string
            # formatting but this is the best I could do \ is not working and
            # returning empty objects
        except Exception as e:
            print("There was an error: ",e)

    def _file_handler(self,*args,**kwargs):

# If you want to use some database use it here.I am using a
# text file because the list hardly ever reaches 50 and I want the latest
# anyway. However this can be changed into a database that would use
# time imports and synchronize with the scraper.
        try:
            file = "jobList.txt"
            f = open(file,"w",encoding="utf-8")
            Headers = "Job, Href \n"
            f.write(Headers)
            for item in job_list:
                try:
                    f.write(item + "\n")
                except Exception as e:
                    print("There was an error: ",e)

            f.close()

        except Exception as e:
            print("There was an error:",e)

# running the class
def main():
    classifiedScraper()

# Checking to run main()
if __name__ == "__main__":
    main()

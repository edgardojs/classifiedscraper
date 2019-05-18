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

# create the scraper class and
# Initialization:
# run your functions here or apply to a global variable object
# Init right now only got two functions the scraper and the file handler (writer)

class classifiedScraper(object):
    def __init__(self):
        self._scraper()
        self._file_handler()

# leaving the print statement as a final error check or Done! This outputs the
# complete job name. There may be duplicate here, so it would be good to do an
# if / else loop somwhere
        print("Script Finished!")
# Scraper function to be used on __init__
    def _scraper(self,*args,**kwargs):
        global job_list
        try:
# header definitions for robots.txt COMPLIANCE
            headers = requests.utils.default_headers()
            headers.update({'User-Agent': 'Mozilla/5.0'})

# take the values from the dictionary file and make a list
            pueblo_list = [x for x in pueblos.values()]

# Url Variables
            general_url = "https://www.clasificadosonline.com"
            general_job_url = "https://www.clasificadosonline.com/UDJobsListing.asp?"
            search_page_url = "https://www.clasificadosonline.com/Jobs.asp"
            job_list = []

            def single_page_parser():
                global page_soup
                jobs_cat = "JobsCat=%{}".format(25)
                txkey_cat = "&txkey={}".format("")
                # Gets the value from pueblo list... maybe an enumerate here too?
                pueblo_cat = "&Pueblo={}".format(pueblo_list[8])
                submit_cat = "&Submit=Buscar+-+GO"
                offset_cat = "&offset=".format("")
                job_search_url = (general_job_url+jobs_cat+pueblo_cat+txkey_cat+submit_cat+offset_cat)
                response = requests.get(job_search_url,headers=headers)
                page_soup = soup(response.content,"html.parser")
                return page_soup
                response.close()

            def multi_page_parser(): # use with caution, breaks with heavy usage do not abuse
                global page_soup
                for index, name in enumerate(pueblo_list,start=0):
                    jobs_cat = "JobsCat=%{}".format(25)
                    txkey_cat = "&txkey={}".format("")
                    pueblo_cat = "&Pueblo={}".format(name)
                    submit_cat = "&Submit=Buscar+-+GO"
                    offset_cat = "&offset=".format("")
                    job_search_url = (general_job_url+jobs_cat+pueblo_cat+txkey_cat+submit_cat+offset_cat)
                    response = requests.get(job_search_url,headers=headers)
                    page_soup = soup(response.content,"html.parser")
                    return page_soup
                    response.close()

# Applying the soup to some variables change to multi_page_parser() uncomment multi_page_parser
# and comment single_page_parser if you want to use the whole list

            #multi_page_parser
            single_page_parser()
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
            print("Soup done!")

        except Exception as e:
            print("There was an error: ",e)

    def _file_handler(self,*args,**kwargs):

# If you want to use some database use it here.I am using a
# text file because the list hardly ever reaches 50 and I want the latest
# anyway. However this can be changed into a database that would use
# time imports and synchronize with the scraper.
        try:
            file = "jobList.txt"
            f = open(file,"a+",encoding="utf-8")
            read_file = open(file,"r",encoding="utf-8")
            file_contents = read_file.read()
            for item in job_list:
                if item not in file_contents:
                    f.write(item + "\n")
                    print("New job!", item)

            Headers = "Job, Href \n"
            for line in read_file.readlines():
                if item not in line:
                    f.write(item + "\n")
                    print("New Job!",item)

        except Exception as e:
            print("There was an error:",e)

# running the class
def main():
    classifiedScraper()

# Checking to run main()
if __name__ == "__main__":
    main()

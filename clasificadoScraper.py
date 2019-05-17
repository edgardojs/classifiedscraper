#! /usr/bin/env/ python
"""
# Clasificadosonline.com Job Search Script
# This will scrape Clasificadosonline.com for jobs
#
"""
# Do the imports
from bs4 import BeautifulSoup as soup
import requests

# create the scraper class
class classifiedScraper(object):


# Initialization:
# run your functions here or apply to a global variable object
# print len and the like to the object can be applied here


    def __init__(self):
        self._scraper()
        self._file_handler()

# leaving the print statement as a final error check or Done!
        #print(len(job_anchor_list))

# Scraper function to be used on __init__
    def _scraper(self,*args,**kwargs):
        global page_soup
        global category_list
        try:

            headers = requests.utils.default_headers()
            headers.update({'User-Agent': 'Mozilla/5.0'})

            # Made pueblo a variable
            # This is here the dictionary imports belong
            # get user input somehow to get the variables to format.
            pueblo = "Humacao"

            # Url Variables
            general_url = "https://www.clasificadosonline.com/UDJobsListing.asp?"
            search_page_url = "https://www.clasificadosonline.com/Jobs.asp"

            # Job Category List
            # integrate pueblo values after looking in the dictionary
            # dictionary portion not yet done.

            jobs_cat = "JobsCat=%{}".format(25)
            pueblo_cat = "&Pueblo={}".format(pueblo)
            txkey_cat = "&txkey={}".format("")
            submit_cat = "&Submit=Buscar+-+GO"
            offset_cat = "&offset=".format("")

            # Job search url variable, have tried to do some other type of string
            # formatting but this is the best I could do \ is not working and
            # returning empty objects
            job_search_url = (general_url + jobs_cat + pueblo_cat + txkey_cat + submit_cat + offset_cat)

            # Requests module stuff scraping done with soup
            response = requests.get(url),headers=headers)
            page_soup = soup(response.content,"html.parser")

            category_list = page_soup.find_all("select",{"class":"Ver14"})

            # Stuff yet to implement here for checks and usable Variables

            # print(category_list)
            # pueblo_list =
            # job_anchor_list = page_soup.findAll("td",{"class":"Ver14nounder"})

            response.close()

        except Exception as e:
            print("There was an error: ",e)

# File Handler function
    def _file_handler(self,*args,**kwargs):

# If you want to use some database use it here.I am using a
# text file because the list hardly ever reaches 50 and I want the latest
# anyway. However this can be changed into a database that would use
# time imports and synchronize with the scraper
        try:
            file = "jobList.txt"
            f = open(file,"w")
            Headers = "Company,Job \n"
            f.write(Headers)
            for item in category_list:
                try:
                    global jobs
                    jobs = item.find_all(["option"])
                    for item in jobs:
                        item.find(["value"])

                    f.write(str(jobs))
                except Exception as e:
                    print("There was an error: ",e)
        except Exception as e:
            print("There was an error:",e)
# running the class
def main():

    classifiedScraper()

# Checking to run main()
if __name__ == "__main__":
    main()

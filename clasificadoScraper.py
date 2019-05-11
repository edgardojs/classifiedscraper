#! /usr/bin/env/ python
"""
# Clasificadosonline.com Job Search Script
# This will scrape Clasificadosonline.com for jobs
#
"""
# Do the imports
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import urllib.request


# create the scraper class
class classifiedScraper(object):
# Initialization:
# run your functions here or apply to a global variable object
# print len and the like to the object can be applied here
    def __init__(self):
        self._scraper()
        self._file_handler()
# leaving the print statement as a final error check or Done!
        print(len(job_anchor_list))


# Scraper function to be used on __init__
    def _scraper(self,*args,**kwargs):
        global job_anchor_list

        try:
            # This html parser. Lxml and xpath may find the div or
            # tbody or table where both job and company are found
            # jobs are Ver14nounder and company is Ver12C span style8 and
            # Ver12nounder If I can find the way to acces the main div
            # correctly I can do a for loop for each and then join

            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent','Mozilla/5.0')]

            # Change this line where pueblo to your municipality, if where you live
            # has a space (San Juan) would be replaced by a plus(+) sign  you can go as far as UDJobsListing.asp? but not sure if it would
            # be to general and require to scrape multpiple pages within the offset value. If you're interested in multiple pages or all Jobs
            # you may need to go and scrape multiple responses on the pages and
            # apply soup() to all of them

            response = opener.open("https://www.clasificadosonline.com/UDJobsListing.asp?JobsCat=%25&Pueblo=Humacao&txkey=&Submit=Buscar+-+GO")
            html_contents = response.read()
            page_soup = soup(html_contents,"html.parser")
            job_anchor_list = page_soup.findAll("td",{"class":"Ver14nounder"})

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
            for item in job_anchor_list:
                try:
                    global jobs
                    jobs = item.find("a",{"class":"Ver14nounder"}).get_text()
                    f.write(jobs + '\n')

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

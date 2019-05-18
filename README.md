# Clasificadosonline.com scraper
Clasificadosonline.com is a popular webpage in Puerto Rico to look for jobs. This currently takes just an item from a list but you can edit at your liking. I hope this can give anyone an idea of what a few lines of Python can do.

Required imports:

BS4 (BeautifulSoup)
requests

Usage: 

Each address is saved in a string which is used by requests to get url information. There are various categories in which the page reacts provided by these variables:

                jobs_cat = "JobsCat=%{}".format(25) 
                txkey_cat = "&txkey={}".format("")
                pueblo_cat = "&Pueblo={}".format(pueblo_list[8])
                submit_cat = "&Submit=Buscar+-+GO"
                offset_cat = "&offset=".format("")
                
If you modify any of these variables either by changing the JobsCat=& txkey pueblo and offset. Submit is the "post" and I advice not to touch unless you know what you're doing, other variables can be modified through "{}".format().


There are two parsers:

single_page_parser()
The default is the single parse function. The pueblo_cat decides municipality or area. Change the number inside pueblo_list[] to access another name in the list of towns and areas


multi_page_parser() 
!! Experimental use at your own risk. Comment the line on #single_page_parser, uncomment and align for multiple page scraping. Please do not abuse of this feature. Uses the entire pueblo_list[] for scraping

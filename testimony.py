#!/usr/bin/env python 2

""" Download all bill testimony for a give bill and year to a given folder 

usage: python testimony.py BILL_NUMBER YEAR DEST

     BILL_NUMBER    should be formatted like HB-5303
     YEAR           is the session year
     DEST           is the destination folder

"""

from dllinks import download_urls, get_urls
from sys import argv

bill = argv[1]
year = argv[2]
dst = argv[3]


url = "https://www.cga.ct.gov/asp/menu/CommDocTmyBillAllComm.asp?bill="+str(bill)+"&doc_year=" + str(year)
base_url = "https://www.cga.ct.gov"
download_urls(get_urls(url), dst=dst, base_url=base_url)

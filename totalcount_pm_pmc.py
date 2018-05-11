# search total publication for each year based on Entrez Date
# python totalcount_pm_pmc.py PMC
# python totalcount_pm_pmc.py PM


import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re, sys

search_string = ['1975', '1976', '1977', '1978', '1979', 
                 '1980', '1981', '1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990', '1991', '1992','1993','1994','1995','1996','1997','1998','1999',
                 '2000', '2001', '2002','2003','2004','2005','2006','2007','2008','2009',
                 '2010', '2011', '2012','2013','2014','2015','2016','2017','2018','2019']

# set database
if str(sys.argv[1]) == "PMC":
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?&db=pmc'
elif str(sys.argv[1]) =="PM":
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?&db=pubmed'

else:
	"Invalid Mode: Use PM or PMC"


year = ''

for id in search_string:
	url2 = url+'&term=("'+year+'%2F01%2F01"%5BEntrez+Date%5D+%3A+"'+year+'%2F12%2F31"%5BEntrez+Date%5D)'
	page = urlopen(url2, timeout= 50)		
	soup = BeautifulSoup(page.read())
	count = float(soup.count.getText())
	print (year, count)
	
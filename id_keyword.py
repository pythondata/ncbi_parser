# extract pmid/pmcid and year when search keyword in a csv file
# python pmc_pm_id_keyword_fromcsv_tocsv.py CAR-T 1990 2018

import urllib2
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup 
import re, sys
import csv

#PM or PMC search string from csv file
ifile = open(str(sys.argv[1])+'.csv')
csv_ifile = csv.reader(ifile)	
each_row = []

start_year = int(sys.argv[2])
end_year = int(sys.argv[3])
years = [str(i) for i in range(start_year,end_year)]


if str(sys.argv[4]) == "PMC":
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?&db=pmc'
elif str(sys.argv[4]) =="PM":
	url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?&db=pubmed'

else:
	"Invalid Mode: Use PM or PMC"

#open file for reporting
Id = ''
with open("results/"+str(sys.argv[4])+"_"+str(sys.argv[1])+"_"+ str(start_year)+"_"+ str(end_year)+".csv", "wb") as f:
	for rows in csv_ifile:
		for each_row in rows:
			for year in years:
				url2 = url+'&term=('+each_row+')+AND+("'+str(year)+'%2F01%2F01"%5BPublication+Date%5D+%3A+"'+str(year)+'%2F12%2F31"%5BPublication+Date%5D)&retmax=10000000'
				#url2 = url + '&term=('+search_string+')&retmax=10000000'
				page = urlopen(url2, timeout= 150)
				xmlPmidList = BeautifulSoup(page.read())
				Ids = [eachlink.getText() for eachlink in xmlPmidList.idlist.findAll("id")]
				for Id in Ids:
					print >>f, Id, each_row, year
	

f.close()
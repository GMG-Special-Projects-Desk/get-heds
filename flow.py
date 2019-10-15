import sys
import requests
import xml.etree.ElementTree as ET
import xmltodict
import datetime
from bs4 import BeautifulSoup
import time
def limit():
	# this means only include sitemaps before a year
	limit = "none"
	try:
		limit = sys.argv[2]
	except:
		print(" No Limit ")
	return limit

def get_site():
	return sys.argv[1]

def get_sitemap_links(limit,site):
	if limit == False:
		# print('FLOW :: GETTING ALL SITEMAP LINKS FOR', site)
		return parse_sitemap(limit,site)
	else:
		# print('FLOW :: GETTING MOST RECENT SITEMAP LINKS', site)
		return parse_sitemap(limit,site)

def parse_sitemap(limit,site):
	response = make_request(site)
	d = xmltodict.parse(response.content)
	
	links = []
	for d in d['sitemapindex']['sitemap']:
		if checkdate(limit,d):
			# print("APPENDING :: "+d['loc'])
			links.append(d['loc'])
	
	return links

def get_articles(link):
	response = requests.get(link)
	d = xmltodict.parse(response.content)
	heds = []
	for l in d['urlset']['url']:
		link = l['loc']
		heds.append(get_hed(link))
	
	return heds


def get_hed(link):
	try:
		response = requests.get(link)
		d = response.text
		soup = BeautifulSoup(d, "html.parser")
		h = soup.find_all('h1')[-1].text
		print(h.encode('utf-8').strip())
		return h
	except:
		print("issue getting headline for "+link)

def make_request(site):
	return requests.get('https://'+site+'/sitemap.xml')

def checkdate(limit,d):
	da = datetime.datetime.strptime(d['lastmod'].split('T')[0], '%Y-%m-%d')
	if limit == "none":
		return True
	else:
		li = datetime.datetime.strptime(limit, '%Y')
		return li > da
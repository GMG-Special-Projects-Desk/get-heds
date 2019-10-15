from flow import *
from site import *

links = get_sitemap_links(limit(),get_site())
h = []
for l in links:
	for hed in get_articles(l):
		try:
			h.append(hed)
		except:
			print(".")

for a in h:
	print(a.encode('utf-8').strip())
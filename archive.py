from flow import *
from site import *

links = get_sitemap_links(limit(),get_site())
h = []
for l in links:
	for heds in get_articles(l):
		try:
			h.append(hed)
		except:
			print("error")

for a in h:
	print(a.encode('utf-8').strip())
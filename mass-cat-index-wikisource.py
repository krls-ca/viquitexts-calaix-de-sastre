#!/usr/bin/python
# -*- coding: utf-8 -*-

import pywikibot, re, time
from bs4 import BeautifulSoup
from pywikibot.proofreadpage import ProofreadPage
from pywikibot.proofreadpage import IndexPage

def getCategoryNeeded(ql):
	if ql == 0:
		#WITHOUT_TEXT
		return u'[[Category:Testurik gabe]]'
		#Testurik gabe
	elif ql == 1:
		#Berrikusi gabe
		#NOT_PROOFREAD
		return u'[[Category:Berrikusi gabe]]'
	elif ql == 2:
		#Arazoak dakartza
		#PROBLEMATIC
		return u'[[Category:Arazoak dakartza]]'
	elif ql == 3:
		#Berrikusita 
		#PROOFREAD
		return u'[[Category:Berrikusita]]'
	elif ql == 4:
		#VALIDATED
		#Balioztatua
		return u'[[Category:Balioztatua]]'

categories = [u'[[Category:Testurik gabe]]', u'[[Category:Berrikusi gabe]]', u'[[Category:Arazoak dakartza]]', u'[[Category:Berrikusita]]', u'[[Category:Balioztatua]]', u'[[Category:Euskara]]']
done = []

def main():
	site = pywikibot.Site("mul", "wikisource")
	arts = pywikibot.Category(site, u"Indizeak euskaraz").articles(recurse=1, reverse=True, content=False)
	'''indexPage = IndexPage(site, u'Index:Chantspopulaires00sall.pdf')
	pages = indexPage.page_gen(only_existing=True, content=True)
	for page in pages:
		if not page.isRedirectPage() and page.exists():
			name = page.title()
			title = name.replace(u"Chantspopulaires00sall", u"Chants populaires du pays basque (1870)")
			print title
			#page.move(title, reason="File renamed in Wikimedia Commons", movetalkpage=True)
			raw_input('Are you sure? (y/n)')
	exit(0)'''
	for art in arts:
		print art.title()
		if art.title() not in done: 
			indexPage = IndexPage(art)
			try:
				#indexPage.page_gen(only_existing=True, content=True, filter_ql=0)
				pages = indexPage.page_gen(only_existing=True, content=True)
			except ValueError as nopage:
				continue
			for page in pages:
				#print page.text
				if page.exists():
					print page
					cat = getCategoryNeeded(page.quality_level)
					oldText = page.text
					#print cat
					print cat
					#newText = oldText.replace(u"[[Category:Euskara]]", "")
					#match = re.match(cat, oldText)
					if cat not in oldText:
						newText = oldText
						for oldCat in categories:
							if oldCat in newText:
								newText = newText.replace(oldCat, "")
						print newText
						headerFooter = re.findall(r"(<noinclude>(?:[\S\s]+?))(?:<\/noinclude>)", newText)
						if len(headerFooter) == 1:
							newText = newText.replace(u"<noinclude></noinclude>", u"<noinclude>{0}</noinclude>".format(cat))
						else:
							footer = headerFooter[1]
							newText = newText.replace(footer, u"{0}\n{1}".format(footer, cat))
						
						pywikibot.showDiff(oldText,newText)
						#raw_input('Are you sure? (y/n)')
						page.put(newText, comment = u'Added category {0}'.format(cat), minorEdit=True)
				#time.sleep(2)
			#raw_input('Are you sure? (y/n)')
if __name__ == '__main__':
	main()
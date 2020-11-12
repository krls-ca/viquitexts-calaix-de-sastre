# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2013 Joan Creus <joan.creus.c@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import re
from datetime import datetime, date

import pywikibot as wikipedia
#import query as query
import pywikibot.data.api

site = wikipedia.Site('ca','wikisource')
punts = {}
vali = {}
revi = {}
llibres = []
for x in range(1859, 1908):
	ll = u'Jochs Florals de Barcelona en '+str(x)+u'.djvu'
	llibres.append(ll)
begin = 1
end = [184, 152, 184,149,154,137,212,151,227,320, 329, 237, 198,127, 153, 169, 291, 323, 241, 219, 468, 303, 133, 127, 163, 0, 0, 183, 241, 0, 225, 265, 284, 346, 0, 0, 0, 0, 465, 293, 169, 251, 165, 175, 247, 295, 202, 138, 270]
if len(llibres) == len(end):
	print "Perfecte son iguals"
i = 0
for llibre in llibres:
	print llibre
	for pag in range(begin, end[i]+1):
		print pag
		params = {
				'action'	:'query',
				'prop'		:'revisions',
				'titles'	:u'Page:%s/%d' % (llibre, pag),
				'rvlimit'   :'50',
				'rvprop'	:'user|timestamp|content',
		}
		data = pywikibot.data.api.CachedRequest(5, **params).submit()
		revs = data["query"]["pages"].values()[0]["revisions"][::-1]
		old = None
		oldUser = None
		oldData = None
		for rev in revs:
			data = datetime.strptime(rev["timestamp"], '%Y-%m-%dT%H:%M:%SZ')
			user = rev["user"]
			txt = rev["*"]
			a,b = re.findall('<pagequality level="(\d)" user="(.*?)" />', txt)[0]
			a = int(a)
			b = user
			if a == 3 and old < 3 and data >= datetime(2014, 11, 14, 0, 0, 0) and data < datetime(2014, 11, 25, 0, 0, 0):
				print u"%s proofreads the page %d." % (b, pag)
				if old == None: print u"Page doesn't exist before."
				punts[b] = punts.get(b, 0)+2
				revi[b] = revi.get(b, 0)+1
			if a == 3 and old == 4 and data >= datetime(2014, 11, 14, 0, 0, 0) and data < datetime(2014, 11, 25, 0, 0, 0):
				if (oldData >= datetime(2014, 11, 14, 0, 0, 0) and oldData < datetime(2014, 11, 25, 0, 0, 0)):
					punts[oldUser] = punts.get(oldUser, 0)-1
					vali[oldUser] = vali.get(oldUser, 0)-1
			if a == 4 and old == 3 and data >= datetime(2014, 11, 14, 0, 0, 0) and data < datetime(2014, 11, 25, 0, 0, 0):
				print u"%s validates page %d." % (b, pag)
				punts[b] = punts.get(b, 0)+1
				vali[b] = vali.get(b, 0)+1
			if a < 3 and old == 3 and data >= datetime(2014, 11, 14, 0, 0, 0) and data < datetime(2014, 11, 25, 0, 0, 0):
				if (oldData >= datetime(2014, 11, 14, 0, 0, 0) and oldData < datetime(2014, 11, 25, 0, 0, 0)):
					punts[oldUser] = punts.get(oldUser, 0)-2
					revi[oldUser] = vali.get(oldUser, 0)-1
					
				
			old = a
			oldUser = b
			oldData = data
		print "-------"
	++i 
print "punt",sorted(punts.iteritems(), key=lambda x: x[1], reverse=True)
print "vali",sorted(vali.iteritems(), key=lambda x: x[1], reverse=True)
print "revi",sorted(revi.iteritems(), key=lambda x: x[1], reverse=True)

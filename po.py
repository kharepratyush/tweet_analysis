import twitter
from collections import defaultdict

api = twitter.Api(consumer_key='#############',consumer_secret='##############',access_token_key='58003262-P7hTdA0g2Xly5C6FldD3MpG8Ca2NIbDcN6Vew0cDr',access_token_secret='zoea2HG466rr4cXqCJPNLhSco0zv8E3p6cPNFGCUjeuPP')

print 'Enter Screen Name'
s=raw_input()

statuses = api.GetUserTimeline(screen_name=s,count=3200)

a=[]
tw = []
words=[]

for s in statuses:
	
	d = s.text.encode('ascii', 'ignore')
	d = d.split()
	words+=d
	#print words

	if s.urls:
		if not s.retweeted:
		    tw.append((s,s.retweet_count))
		
	if s.hashtags:
	    for item in s.hashtags:
        	a.append(item.text)
    
        	
result = []
for entry in set(a):
    result.append((entry, a.count(entry)))

result.sort(key = lambda x: -x[1])
#print result[0:3]
for u,v in result[0:3]:
	print u,v
print '\n'

tw.sort(key = lambda x: -x[1])
#print tw[0:3]

for u,v in tw[0:3]:
	print u
	print v
print '\n'

#print words
word_result = []
for entry in set(words):
    word_result.append((entry, words.count(entry)))

word_result.sort(key = lambda x: -x[1])
#print word_result[:3]
for u,v in word_result[0:3]:
	print u,v
print '\n'

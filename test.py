import twitter
 
api = twitter.Api()
statuses = api.GetUserTimeline('isu_daruma')
for s in statuses:
    if s.text[0] != '@':
        print s.text.encode('utf-8')
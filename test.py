import urllib
import json
fieldsAttribute="feed{comments{message},message}"
authToken="EAACEdEose0cBAPJbsX7vIUXpl4fPC0yH3emBuTqDCatZAgCUnQntoI9iTejj10CpUSI6VwG429WmR3DspTfOr6twAHeA4m7nl5I4vbItt6KZCz7083AStaZAaTGHJzgovlEKLphE7UWIkb1dMhJ01nDB2w7NUlsDxx3wqidbwZDZD"
#we've to refresh authToken once an hour
#url="https://graph.facebook.com/v2.6/913814308634931?fields=feed%7Bcomments%7Bmessage%7D%2Cmessage%7D&access_token=EAACEdEose0cBAPJbsX7vIUXpl4fPC0yH3emBuTqDCatZAgCUnQntoI9iTejj10CpUSI6VwG429WmR3DspTfOr6twAHeA4m7nl5I4vbItt6KZCz7083AStaZAaTGHJzgovlEKLphE7UWIkb1dMhJ01nDB2w7NUlsDxx3wqidbwZDZD"
url="https://graph.facebook.com/v2.6/913814308634931?fields=feed%7Bcomments%7Bmessage%7D%2Cmessage%7D&access_token=EAACEdEose0cBAPJbsX7vIUXpl4fPC0yH3emBuTqDCatZAgCUnQntoI9iTejj10CpUSI6VwG429WmR3DspTfOr6twAHeA4m7nl5I4vbItt6KZCz7083AStaZAaTGHJzgovlEKLphE7UWIkb1dMhJ01nDB2w7NUlsDxx3wqidbwZDZD"
baseUrl="https://graph.facebook.com/v2.6/913814308634931?"
mainUrl=baseUrl+urllib.urlencode({'fields':fieldsAttribute,
                       'access_token': authToken})
print mainUrl
pageFile=urllib.urlopen(mainUrl)
pageData=pageFile.read()
jsonData=json.loads(str(pageData))


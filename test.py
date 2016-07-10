import urllib
import json
import sqlite3
connection=sqlite3.connect('FoodPostDB.db')
cursor=connection.cursor()
authToken=raw_input("Enter authentiation token: ")
fieldsAttribute=raw_input("Enter field attributes: ")
if len(fieldsAttribute)<1:
    fieldsAttribute="feed.limit(2){from,place,comments{from,message},picture,created_time,message,link}"
baseUrl="https://graph.facebook.com/v2.6/913814308634931?"
mainUrl=baseUrl+urllib.urlencode({'fields':fieldsAttribute,
                       'access_token': authToken})
#print mainUrl
count =0
while(count<2):
    
    postID=None
    message=None
    posterID=None
    placeID=None
    time=None
    picLink=None
    count=count+1
    print  count   
    #print "baal ta kam koros na ken??"
    print mainUrl + "\n\n"
    pageFile=urllib.urlopen(mainUrl)
    pageData=pageFile.read()
    jsonData=json.loads(str(pageData))
    print jsonData.keys()
    #mainUrl=
    '''
    if 'feed' in jsonData:
        mainUrl= jsonData['feed']['paging']['next']
    else:
        mainUrl=jsonData['paging']['next']
    '''
    if 'feed' in jsonData:
        jsonData=jsonData['feed']
    mainUrl=jsonData['paging']['next']
    #print jsonData['feed']['paging']['next']
    for data in jsonData['data']:
        if 'message' in data:
            message=data['message']
            #print message
        if 'id' in data:
            postID=data['id']
        if 'place' in data:
            placeID=data['place']['id']
        if 'picture' in data:
            picLink=data['picture']
        if 'created_time' in data:
            time=data['created_time']
        posterID=data['from']['id']
        cursor.execute(''' INSERT INTO Post
        (postID, Message, PersonID, PictureID, PlaceID, Time)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (postID, message, posterID, picLink, placeID, time,  ))
        if count%30==0:
            connection.commit()

connection.commit()
    


import urllib
import json
import sqlite3
connection=sqlite3.connect('FoodPostDB.db')
cursor=connection.cursor()
authToken=raw_input("Enter authentiation token: ")
fieldsAttribute=raw_input("Enter field attributes: ")
if len(fieldsAttribute)<1:
    fieldsAttribute="feed.limit(100){from,place,comments{from,message},picture,created_time,message,link}"
baseUrl="https://graph.facebook.com/v2.6/913814308634931?"
mainUrl=baseUrl+urllib.urlencode({'fields':fieldsAttribute,
                       'access_token': authToken})
#print mainUrl
count =0
while(count>-1):
    
    postID=None
    message=None
    posterID=None
    placeID=None
    time=None
    picLink=None
    count=count+1
    print  count   
    #print "baal ta kam koros na ken??"
    #print mainUrl + "\n\n"
    pageFile=urllib.urlopen(mainUrl)
    pageData=pageFile.read()
    jsonData=json.loads(str(pageData))
    #print jsonData.keys()
    #mainUrl=
    if 'feed' in jsonData:
        jsonData=jsonData['feed']
    if len(jsonData['data'])<1:
        break;
    mainUrl=jsonData['paging']['next']
    print mainUrl
    break
    #print jsonData['feed']['paging']['next']
    for data in jsonData['data']:
        if 'message' in data:
            message=data['message']
            #print message
        if 'id' in data:
            postID=data['id']
            cursor.execute(''' SELECT * 
            FROM Post
            WHERE PostID=?''',
            (postID, ))
            try:
                cursor.fetchone()[0]
                print "Post already in database"
                continue
            except:
                pass
        else:
            continue
        if 'place' in data:
            placeID=data['place']['id']
        if 'picture' in data:
            picLink=data['picture']
        if 'created_time' in data:
            time=data['created_time']
        if 'from' in data:
            posterID=data['from']['id']
        #print poster
        cursor.execute(''' INSERT INTO Post
        (postID, Message, PersonID, PictureLink, PlaceID, Time)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (postID, message, posterID, picLink, placeID, time,  ))
        if count%10==0:
            connection.commit()
            print "commiting"
        if count%210==0:
            choice=raw_input("Enter  y to continiue: ")
            if(choice !="y"):
                break

connection.commit()
    


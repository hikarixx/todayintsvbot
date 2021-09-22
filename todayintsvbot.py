import tweepy as twp
import twitter as twt
import pytube as pyt
from datetime import date
from datetime import timedelta
import time


# Authenticate to Twitter
#twt
user = twt.Api(consumer_key='FR7pCtcvpmBNHFodiz1ABe1Ve',
               consumer_secret='88zUOUXS1kpD20Y7som9xoCERpfbhezlLc6gaHRmRVk0RaelVM',
               access_token_key='1337349470984437760-ekWY5yFFoWIFLLAZXeYUhHgaSJo6OP',
               access_token_secret='emDasfDFFmesaP8vHn8FaqOLkMSR0WhOJuglKgH85sevT')

#twp
auth = twp.OAuthHandler("FR7pCtcvpmBNHFodiz1ABe1Ve",
                        "88zUOUXS1kpD20Y7som9xoCERpfbhezlLc6gaHRmRVk0RaelVM")
auth.set_access_token("1337349470984437760-ekWY5yFFoWIFLLAZXeYUhHgaSJo6OP",
                      "emDasfDFFmesaP8vHn8FaqOLkMSR0WhOJuglKgH85sevT")

# Create API object
api = twp.API(auth)

today = date.today().strftime("%m-%d")
tmr = (date.today() + timedelta(days=1)).strftime("%m-%d")
thisyear = int(date.today().strftime("%Y")) #must convert to int

to_post = []

#yt variables
uploads = pyt.Playlist("https://youtube.com/playlist?list=UUAzKFALPuF_EPe-AEI0WFFw")
urllist = uploads.video_urls
urllist.reverse()

#upload lists by year
y14 = urllist[0:9]
y15 = urllist[9:34]
y16 = urllist[34:62]
y17 = urllist[62:229]
y18 = urllist[229:489]
y19 = urllist[489:722]
y20 = urllist[722:952]
y21 = urllist[952:] #check for end of list at eoy
#add new yearlist each year
uploadsyears = [y14,y15,y16,y17,y18,y19,y20,y21] #update with new yearlist each year

'''
def main():
    while True:
        #run get_yt once daily
        #run statusupdate at intervals
        time.sleep(#insert time interval here)

def yearlyupdate():
    while True:
    #run yearlist once per year
'''
'''
#yearlist splitting
def yearlist():
    i = 0

def jumpsearch(list):
    step = len(list)**0.5
    while
'''
#tweeting functions
def statusupdate():
    for info in to_post:
        #info = (date, title, img, url)
        twtstr = f"Today in TSV:\n{info['title']} ({info['date']})\n{info['url']}"
        user.PostUpdate(twtstr, media=info['img'])
        #time.sleep(insert time interval)
        
#yt content functions
def searchyear(yearlist):
    n = len(yearlist) // 2
    ndate = yearlist[n].publish_date.strftime("%m-%d")
    if ndate == today:
        return yearlist[n]
    elif n == 0:
        return '' #no result
    elif ndate > today:
        return searchyear(yearlist[0:n])
    elif ndate < today:
        return searchyear(yearlist[n:])

def get_yt():
    for i in uploadsyears:
        url = searchyear(i)
        if url:
            video = YouTube(url)
            '''
            title = video.title
            img = video.thumbnail_url
            date = video.publish_date.strftime("%y%m%d") #maybe use another dateformat
            '''
            #video_info = (date, title, img, url) #maybe change url to shareable?
            info = {
                'title': video.title,
                'img': video.thumbnail_url,
                'date': video.publish_date.strftime('%y%m%d'),
                'url': url
            }
            to_post.append(info) #maybe don't append directly?

#twt content functions
def get_twt():
    today_twt = []
    for i in range (2014,thisyear+1):
        search = user.GetSearch(term='from:twosetviolin',
                                since=f'{i}-{today}',
                                until=f'{i}-{tmr}')
        for j in search:
            if j.created() != today:
                j.pop()
        if search != []:
            today_twt.extend(search)

            
#insta content functions

'''
#linear search directly from playlist
def get_yt():
    i = 0
    for video in uploads.videos:
        i += 1
        if video.publish_date.strftime("-%m-%d") == today:
            title = video.title
            img = video.thumbnail_url
            url = uploads.video_urls[i]
            video_info = (title, img, url)
            print(i)
            print(video_info)
'''
'''
#test search function
testlist = [1,3,5,7,9]
def testloop(list,search):
    n = len(list) // 2
    print(list)
    if list[n] == search:
        return list[n]
    elif n == 0:
        return False
    elif list[n] > search:
        return testloop(list[0:n],search)
    elif list[n] < search:
        return testloop(list[n:],search)
'''
'''
#datetime formats
video = pyt.YouTube('https://www.youtube.com/watch?v=fgmgEkIZcFc')
print(video.publish_date) #datetime 2020-12-16 00:00:00
print(today) #date  2020-12-18
'''

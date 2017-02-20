import requests
import time
import os
import schedule

urls = ['http://70news.wordpress.com',
        'http://activistpost.com',
        'http://americannews.com',
        'http://amren.com',
        'http://buzzfeedusa.com',
        'http://canadafreepress.com',
        'http://clashdaily.com',
        'http://conservativedailypost.com',
        'http://dailyheadlines.com',
        'http://darkmoon.me',
        'http://dcclothesline.com',
        'http://downtrend.com',
        'http://embols.com',
        'http://EUTimes.net',
        'http://fellowshipoftheminds.com',
        'http://freedomdaily.com',
        'http://freedomoutpost.com',
        'http://gopthedailydose.com',
        'http://greanvillepost.com',
        'http://humansarefree.com',
        'http://infostormer.com',
        'http://infowars.com',
        'http://ItMakesSenseBlog.com',
        'http://learnprogress.org',
        'http://newstarget.com',
        'http://rickwells.us',
        'http://sentinelblog.com',
        'http://shoebat.com',
        'http://success-street.com',
        'http://usanewsflash.com',
        'http://usapoliticsnow.com',
        'http://usasupreme.com',
        'http://usatwentyfour.com',
        'http://usfanzone.com']

#with open('fakeNewsSites.txt') as infile:
    #for line in infile:
        #url = ('http://' + line).replace('\n','')
        #urls.append(url)

def extract_html():
    print('Extracting...')
    for url in urls:
        r = requests.get(url)
        source = url.replace('http://','').replace('.com','').replace('.org', '').replace('.us', '').replace('.me', '').replace('.net', '')
        filename = '/mnt/c/Users/Brennan/Dropbox/MIDS/w210-capstone/data/notCredible/{0}/{1}.html'.format(source, date)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            f.write(r.text)
    print('Finished')
    return None
    
schedule.every().day.at("18:00").do(extract_html)
while True:
    date = time.strftime("%m-%d")
    schedule.run_pending()
    time.sleep(60)

from django.shortcuts import render
import requests
import urllib.request
import bs4 as bs
from bs4 import BeautifulSoup
from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
# Create your views here.

def home(request):
    template_name='index.html'
    station='9410840'
    airTemp_url ='https://tidesandcurrents.noaa.gov/api/datagetter?date=latest&station={}&product=air_temperature&datum=STND&time_zone=lst_ldt&units=english&format=json'
    waterTemp_url='https://tidesandcurrents.noaa.gov/api/datagetter?date=latest&station={}&product=water_temperature&datum=STND&time_zone=lst_ldt&units=english&format=json'
    pressure_url='https://tidesandcurrents.noaa.gov/api/datagetter?date=latest&station={}&product=air_pressure&datum=STND&time_zone=lst_ldt&units=english&format=json'
    wind='https://tidesandcurrents.noaa.gov/api/datagetter?date=latest&station={}&product=wind&datum=STND&time_zone=lst_ldt&units=english&format=json'
    tide='https://tidesandcurrents.noaa.gov/api/datagetter?date=recent&station={}&product=predictions&datum=STND&time_zone=lst_ldt&interval=hilo&units=english&format=json'
    airTemp = requests.get(airTemp_url.format(station)).json()
    waterTemp = requests.get(waterTemp_url.format(station)).json()
    pressure = requests.get(pressure_url.format(station)).json()
    wind = requests.get(wind.format(station)).json()
    tide = requests.get(tide.format(station)).json()
    map_url='https://www.sigalert.com/map.asp?lat=34.08402&lon=-118.52828&z=2'
    
    city_weather={
        'city':airTemp['metadata']['name'],
        'air_temp':airTemp['data'][0]['v'],
        'water_temp':waterTemp['data'][0]['v'],
        'pressure':pressure['data'][0]['v'],
        'wind':wind['data'][0]['s'],
        'gusting':wind['data'][0]['g'],
        'direction':wind['data'][0]['dr'],
        'tidetime1':(tide['predictions'][0]['t']).split(" ")[1],
        'tidetime2':(tide['predictions'][1]['t']).split(" ")[1],
        'tidetime3':(tide['predictions'][2]['t']).split(" ")[1],
        'tide1':tide['predictions'][0]['v'],
        'tide2':tide['predictions'][1]['v'],
        'tide3':tide['predictions'][2]['v'],
        'tidelevel1':tide['predictions'][0]['type'],
        'tidelevel2':tide['predictions'][1]['type'],
        'tidelevel3':tide['predictions'][2]['type'],
        'map_url':map_url
    }

    
    base_url='https://forecast.weather.gov/MapClick.php?lat=34.005&lon=-118.809&unit=0&lg=english&FcstType=text&TextType=1'
    responce =requests.get(base_url)
    html=responce.content
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.findAll('table')
    nwsForecast1 =[data.text for data in tables[0].findAll('tr')]
    nwsForecast2 =[data.text for data in tables[1].findAll('tr')]
    nwsForecast={
        'nwsForecast1':nwsForecast1[0],
        'nwsForecast2':nwsForecast2[0]
    }

    
    r1 = requests.get('https://www.malibucity.org/RSSFeed.aspx?ModID=63&CID=All-0')
    data = r1.text
    soup = BeautifulSoup(data, "xml")
    title =[data.text for data in soup.findAll('title')]
    lastBuildDate =[data.text for data in soup.findAll('lastBuildDate')]
    description =[data.text for data in soup.findAll('description')]
    pubDate =[data.text for data in soup.findAll('pubDate')]
    guid =[data.text for data in soup.findAll('guid')]
    
    rssfeed1={'title1':title[0],'lastBuildDate':lastBuildDate[0],'description':description[0]}
    rssfeed2={'title1':title[1],'lastBuildDate':pubDate[0],'description':description[1]}
    rssfeed3={'title1':title[2],'lastBuildDate':pubDate[1],'description':description[2]}
    rssfeed4={'title1':title[3],'lastBuildDate':pubDate[2],'description':description[3]}
    rssfeed5={'title1':title[4],'lastBuildDate':pubDate[3],'description':description[4]}
    rssfeed6={'title1':title[5],'lastBuildDate':pubDate[4],'description':description[5]}
    rssfeed7={'title1':title[6],'lastBuildDate':pubDate[5],'description':description[6]}
    rssfeed8={'title1':title[7],'lastBuildDate':pubDate[6],'description':description[7]}
    rssfeed9={'title1':title[8],'lastBuildDate':pubDate[7],'description':description[8]}
    

    r = requests.get('https://www.malibucity.org/RSSFeed.aspx?ModID=58&CID=All-calendar.xml')
    data = r.text
    soup1 = BeautifulSoup(data, "xml")
    title1 =[data1.text for data1 in soup1.findAll('title')]
    lastBuildDate1 =[data1.text for data1 in soup1.findAll('lastBuildDate')]
    description1 =[data1.text for data1 in soup1.findAll('description')]
    pubDate1 =[data1.text for data1 in soup1.findAll('pubDate')]
    eventDates =[data1.text for data1 in soup1.findAll('calendarEvent:EventDates')]
    eventTimes =[data1.text for data1 in soup1.findAll('calendarEvent:EventTimes')]
    location =[data1.text for data1 in soup1.findAll('calendarEvent:Location')]
    guid1 =[data1.text for data1 in soup1.findAll('guid')]
    
    rssfeed10={'title1':title1[0],'lastBuildDate':lastBuildDate1[0],'description':description1[0]}
    rssfeed11={'title1':title1[1],'lastBuildDate':pubDate1[0],'description':description1[1]}
    rssfeed12={'title1':title1[2],'lastBuildDate':pubDate1[1],'description':description1[2]}
    rssfeed13={'title1':title1[3],'lastBuildDate':pubDate1[2],'description':description1[3]}
    rssfeed14={'title1':title1[4],'lastBuildDate':pubDate1[3],'description':description1[4]}
    rssfeed15={'title1':title1[5],'lastBuildDate':pubDate1[4],'description':description1[5]}
    rssfeed16={'title1':title1[6],'lastBuildDate':pubDate1[5],'description':description1[6]}
    rssfeed17={'title1':title1[7],'lastBuildDate':pubDate1[6],'description':description1[7]}
    rssfeed18={'title1':title1[8],'lastBuildDate':pubDate1[7],'description':description1[8]}
    rssfeed19={'title1':title1[9],'lastBuildDate':pubDate1[8],'description':description1[9]}
    rssfeed20={'title1':title1[10],'lastBuildDate':pubDate1[9],'description':description1[10]}
    context={"city_weather":city_weather,"nwsForecast":nwsForecast,"rssfeed1":rssfeed1,"rssfeed2":rssfeed2,"rssfeed3":rssfeed3,"rssfeed4":rssfeed4,
    "rssfeed5":rssfeed5,"rssfeed6":rssfeed6,"rssfeed7":rssfeed7,"rssfeed8":rssfeed8,"rssfeed9":rssfeed9,"rssfeed10":rssfeed10,
    "rssfeed11":rssfeed11,"rssfeed12":rssfeed12,"rssfeed13":rssfeed13,"rssfeed14":rssfeed14,"rssfeed15":rssfeed15 ,"rssfeed16":rssfeed16 ,"rssfeed17":rssfeed17
    ,"rssfeed18":rssfeed18 ,"rssfeed19":rssfeed19,"rssfeed20":rssfeed20
    }
    return render(request,template_name,context)

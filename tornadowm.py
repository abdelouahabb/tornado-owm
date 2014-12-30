# -*- coding: utf-8 -*-
from tornado.httpclient import AsyncHTTPClient
import json
import xml.etree.ElementTree as ET


http_client = AsyncHTTPClient()
url = ''
response = ''
args = []
link = 'http://api.openweathermap.org/data/2.5/'
api = ''
result = {}
way = ''


def forecast(way, **kwargs):
    '''forecast(way, optional_arguments)

    way = [weather, daily, forecast, find, group];
    forecast: you can get weather forecast for 5 days with data every 3 hours.
    daily: you can get daily weather forecast up to 16 days (using cnt).
    find:

    q = city; you can add country code or its name after a comma (london,uk);
    or you can use lat=latitude; lon=longitude; id=coutry id;

    mode=[json, xml, html]; how you want the result

    cnt = int; number of days (from 1 to 16)
    (works only with daily and find);

    units = [imperial, metric]; (°C or °F)

    cnt = int; To limit number of listed cities, to be used with "find".

    type = [like, accurate];
    To set the accuracy level either use the 'accurate' or 'like' type parameter.
    'accurate' returns exact match values.
    'like' returns results by searching for that substring

    lang=[English-en, Russian-ru, Italian-it, Spanish-es(or sp),
    Ukrainian-uk(or ua), German-de, Portuguese-pt, Romanian-ro,
    Polish-pl, Finnish-fi, Dutch-nl, French-fr, Bulgarian-bg,
    Swedish-sv(or se), Chinese Trad-zh_tw, Chinese Simpl-zh(or zh_cn),
    Turkish-tr, Croatian-hr, Catalan-ca]

    example: forecast('daily', q='azazga', cnt=5, lang='fr')

    for full specs: http://www.openweathermap.com/api
    '''
    global api
    if way in ('weather', 'forecast', 'daily', 'find'):
        if way == 'daily':
            way = 'forecast/daily?'
        else:
            way += '?'
        for i, j in kwargs.iteritems():
            args.append('&{0}={1}'.format(i, j))
        a = ''.join(set(args))
        api = link + way + a.replace(' ', '+')

        def handle_request(resp):
            global response
            if resp.error:
                print "Error:", resp.error
            else:
                response = resp.body

        http_client.fetch(api, handle_request)
    else:
        print "please put a way: 'weather', 'forecast', 'daily', 'find' "


def get_result():
    global result
    if response.startswith('{'):
        print 'the result is JSON, stored in the variable result'
        result = json.loads(response)

    elif response.startswith('<'):
        print 'the result is XML, parse the result variable to work on the nodes,'
        print 'or, use response to see the raw result'
        result = ET.fromstring(response)

    else:
        print '''Sorry, no valid response, or you used a parameter that is not compatible with the way!\n
        please check http://www.openweathermap.com/api for more informations'''

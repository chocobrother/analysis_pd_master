from datetime import datetime
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys
import math
from .json_request import json_request

SERVICE_KEY = 'wKfGcfx0RbdE50%2BWKTO4nCuMWpgLE3wE%2F3Yk7Vf4eTItjDmlFyQiMaYIKo2wYgs%2BQkJJSG5XN3HvspNYGdnl9Q%3D%3D'
def pd_gen_url(endpoint, service_key, **params):
    return '%s?%s&serviceKey=%s' % (endpoint,urlencode(params),service_key)


def pd_fetch_foreign_visitor(country_code=112, year=2012, month=6, service_key=SERVICE_KEY):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    #service_key = 'wKfGcfx0RbdE50%2BWKTO4nCuMWpgLE3wE%2F3Yk7Vf4eTItjDmlFyQiMaYIKo2wYgs%2BQkJJSG5XN3HvspNYGdnl9Q%3D%3D'
    url = pd_gen_url(
        endpoint,
        service_key,
        YM='{0:04d}{1:02d}'.format(year, month),
        NAT_CD=country_code,
        ED_CD='E',
        _type='json')

    json_result = json_request(url=url)

    print(json_result)
    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print("%s : Error[%s] for request [%s]" % (datetime.now(), result_message, url), file=sys.stderr)
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None



def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0,
        service_key=SERVICE_KEY):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'

    pageno = 1


    print(endpoint)

    url = pd_gen_url(
        endpoint,
        service_key,
        YM='{0:04d}{1:02d}'.format(year, month),
        SIDO=district1,
        GUNGU=district2,
        RES_NM=tourspot,
        pageNo=pageno,
        numOfRows=100,
        _type='json'
            )

    json_result = json_request(url=url)
    print(json_result)

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')

    print(json_result)

    if 'OK' != result_message:
        print("%s : Error[%s] for request [%s]" % (datetime.now(), result_message, url), file=sys.stderr)
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None

#if __name__ == '__main__':
 #   pd_fetch_tourspot_visitor()
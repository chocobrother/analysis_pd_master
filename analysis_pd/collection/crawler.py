import os
import json
from .api import api
RESTORE_DIRECTORY = '__result__/crawling'

def preprocess_tourspot_visitor(data):

    if 'addrCd' in data:
        del data['addrCd']

    if 'rnum' in data:
        del  data['rnum']

    if 'gungu' in data:
        del data['gungu']

    if 'csNatCnt' in data:
        data['count_locals'] = data['csNatCnt']
        del data['csNatCnt']

    if 'csForCnt' in data:
        data['count_foreigner'] = data['csForCnt']
        del data['csForCnt']

    if 'resNm' in data:
        data['tourist_spot'] = data['resNm']
        del data['resNm']

    if 'ym' in data:
         data['date'] = data['ym']
         del data['ym']

    if 'sido' in data:
        data['district'] = data['sido']
        del data['sido']



def preprocess_foreign_visitor(data):
    del data['ed']
    del data['edCd']
    del data['rnum']

    data['country_code'] = data['natCd']
    del data['natCd']

    data['country_name'] = data['natKorNm'].replace(' ', '')
    del data['natKorNm']

    data['visit_count'] = data['num']
    del data['num']

    data['date'] = data['ym']
    del data['ym']

def crawling_foreign_visitor(
        country,
        start_year,
        end_year,
        ):

        #restore_directory = RESTORE_DIRECTORY
        results = []
        file = '%s(%s)_foreignvisitor_%s_%s.json' % (
         country[0], country[1], start_year, end_year)

        DATA = True

        if DATA:
            for year in range(start_year, end_year + 1):
                for month in range(1, 13):
                    data = api.pd_fetch_foreign_visitor(country[1], year, month)
                    if data is None:
                        continue

                    preprocess_foreign_visitor(data)
                    results.append(data)

            with open(file, 'w', encoding='utf8') as save:
                jsondata = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
                save.write(jsondata)

        return file



def crawling_tourspot_visitor(
        district,
        start_year,
        end_year,
        ):
    results = []
    filename = '%s_tourspot_%s_%s.json' % ( district, start_year, end_year)

    DATA = True

    if DATA:
        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                for data in api.pd_fetch_tourspot_visitor(
                        district1=district,
                        year=year,
                        month=month
                        ):
                    preprocess_tourspot_visitor(data)

                    results.append(data)
        print(results)
    with open(filename, 'w', encoding='utf-8') as save:
        jsondata = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        save.write(jsondata)

    return filename



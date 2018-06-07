from collection .api import api as pdapi

# test for pd_gen_url

url = pdapi.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    'NE9ahmDK93upDAzNePXu7W36688QkfHl8RdDPZnLSzqWlD8H0Jb0rOL4hGtqh2jWdz6J0b2MIdU2ENJx9nwu%2FA%3D%3D ',
    YM='{0:04d}{1:02d}'.format(2017,1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1
)


print(url)
# test for pd_fetch_tourspot_visitor

for items in pdapi.pd_fetch_tourspot_visitor(district1='서울특별시',year=2012,month=7):
    print(items)
# test for pd_fetch_foreign_visitor



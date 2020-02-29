import googlemaps
import googlemap_key
import folium
import json
import pandas as pd
import numpy as np
from folium.plugins import MarkerCluster

gmaps=googlemaps.Client(key=googlemap_key.gmaps_key)

CNch=gmaps.geocode('천안시청', language='ko')
CNch_loc=CNch[0].get('geometry').get('location')
Cheonan_loc=[CNch_loc['lat'], CNch_loc['lng']]
Cheonan_map=folium.Map(location = Cheonan_loc)
Cheonan_map=folium.Map(location=Cheonan_loc, zoom_start=15)

# 통계
coronaNum=pd.read_csv('C:\LJM\LJM 2020\corona\확진자 통계.csv', encoding='utf-8')
num='확진자 수'
coronaNum.set_index('읍면동')
EMD_name=[]
for name in coronaNum['읍면동']:
    EMD_name.append('충청남도 천안시'+str(name))


# 법정동 위치 정보 얻어오기
EMD_addr = []
EMD_lat = []
EMD_lng = []
for name in EMD_name:
    tmp=gmaps.geocode(name, language='ko')
    EMD_addr.append(tmp[0].get('formatted_address'))
    tmp_loc=tmp[0].get('geometry').get('location')
    EMD_lat.append(tmp_loc['lat'])
    EMD_lng.append(tmp_loc['lng'])
for i in range(5):
    print(EMD_addr[i], EMD_lat[i], EMD_lng[i], sep=',\t')

# 법정동 위도 경도 추가하기
coronaNum['위도'] = EMD_lat
coronaNum['경도'] = EMD_lng

# 법정동 위치 정보만 분리하기
EMD_geo = coronaNum.loc[:, ['읍면동', '위도', '경도']]
EMD_geo.set_index('읍면동', inplace=True)

# 법정동 마커 추가하기
#for n in EMD_geo.index:
#    folium.Marker([EMD_geo['위도'][n], EMD_geo['경도'][n]], popup=n).add_to(Cheonan_map)


# 법정동 경계선 표시하기 및 확진자 수에 따른 색 구분
geo_str=json.load(open('C:\LJM\LJM 2020\corona\EMD.json', encoding='utf-8'))

folium.Choropleth(geo_data=geo_str, data=coronaNum, key_on='feature.properties.EMD_KOR_NM', fill_color='PuRd',
                  columns=['읍면동', '확진자 수'], legend_name='Number of Corona patient').add_to(Cheonan_map)

# 중간 저장하기
Cheonan_map.save('C:\LJM\LJM 2020\corona\Cheonan.html')

# 데이터 저장하기
coronaNum.to_csv('C:\LJM\LJM 2020\corona\확진자 통계.csv', encoding='utf-8')


# 확진자 수 markercluster로 표시하기
marker_cluster=MarkerCluster().add_to(Cheonan_map)

homes=[]

# 1번째 확진자
home_1 = '불당대동다숲 아파트'
tmp = gmaps.geocode(home_1, language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_1=[tmp_loc['lat'], tmp_loc['lng']]

if home_1 in homes :
    loc_1=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_1)
    
folium.Marker(loc_1, popup='불당대동다숲 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_1, radius=25, fill=True, popup='천안시 1번', color='red', fill_color='orange').add_to(Cheonan_map)



# 2번째 확진자
home_2 = '두정동 세광2차 아파트'
tmp_lat = 36.8298
tmp_lng = 127.128809
loc_2=[tmp_lat, tmp_lng]

if home_2 in homes :
    loc_2=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_2)
    
folium.Marker(loc_2, popup='두정동 세광2차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_2, radius=25, fill=True, popup='천안시 2번', color='red', fill_color='orange').add_to(Cheonan_map)



# 3번째 확진자
home_3 = '불당지웰더샵 아파트'
tmp_lat = 36.81468
tmp_lng = 127.1048
loc_3=[tmp_lat, tmp_lng]

if home_3 in homes :
    loc_3=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_3)
    
folium.Marker(loc_3, popup='불당지웰더샵 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_3, radius=25, fill=True, popup='천안시 3번', color='red', fill_color='orange').add_to(Cheonan_map)



# 4번째 확진자
home_4 = '불당아이파크 아파트'
tmp_lat = 36.808554
tmp_lng = 127.1091
loc_4=[tmp_lat, tmp_lng]

if home_4 in homes :
    loc_4=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_4)
    
folium.Marker(loc_4, popup='불당아이파크 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_4, radius=25, fill=True, popup='천안시 4번', color='red', fill_color='orange').add_to(Cheonan_map)



# 5번째 확진자
home_5 = '불당동일하이빌 아파트'
tmp_lat = 36.808049
tmp_lng = 127.11237
loc_5=[tmp_lat, tmp_lng]

if home_5 in homes :
    loc_5=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_5)
    
folium.Marker(loc_5, popup='불당동일하이빌 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_5, radius=25, fill=True, popup='천안시 5번', color='red', fill_color='orange').add_to(Cheonan_map)



# 6번째 확진자
home_6 = '불당동 린스트라우스2차 아파트'
tmp_lat = 36.8148
tmp_lng = 127.1014
loc_6=[tmp_lat, tmp_lng]

if home_6 in homes :
    loc_6=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_6)
    
folium.Marker(loc_6, popup='불당동 린스트라우스2차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_6, radius=25, fill=True, popup='천안시 6번', color='red', fill_color='orange').add_to(Cheonan_map)



# 7번째 확진자
home_7 = '불당아이파크 아파트'
tmp_lat = 36.808554
tmp_lng = 127.1091
loc_7=[tmp_lat, tmp_lng]

if home_7 in homes :
    loc_7=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_7)
    
folium.Marker(loc_7, popup='불당아이파크 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_7, radius=25, fill=True, popup='천안시 7번', color='red', fill_color='orange').add_to(Cheonan_map)



# 8번째 확진자
home_8 = '불당호반3차 아파트'
tmp_lat = 36.803
tmp_lng = 127.1045
loc_8=[tmp_lat, tmp_lng]

if home_8 in homes :
    loc_8=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_8)
    
folium.Marker(loc_8, popup='불당호반3차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_8, radius=25, fill=True, popup='천안시 8번', color='red', fill_color='orange').add_to(Cheonan_map)



# 9번째 확진자
home_9 = '쌍용동 용암마을 아파트'
tmp = gmaps.geocode('쌍용동 용암마을 아파트', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_9=[tmp_loc['lat'], tmp_loc['lng']]

if home_9 in homes :
    loc_9=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_9)

folium.Marker(loc_9, popup='쌍용동 용암마을 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_9, radius=25, fill=True, popup='천안시 9번', color='red', fill_color='orange').add_to(Cheonan_map)



#10번째 확진자
home_10 = '두정동 푸르지오 4차 아파트'
tmp = gmaps.geocode('두정동 푸르지오 4차', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_10=[tmp_loc['lat'], tmp_loc['lng']]

if home_10 in homes :
    loc_10=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_10)
    
folium.Marker(loc_10, popup='두정동 푸르지오 4차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_10, radius=25, fill=True, popup='천안시 10번', color='red', fill_color='orange').add_to(Cheonan_map)



#11번째 확진자
home_11 = '천안시 북면'
tmp = gmaps.geocode('천안시 북면', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_11=[tmp_loc['lat'], tmp_loc['lng']]

if home_11 in homes :
    loc_11=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_11)

folium.Marker(loc_11, popup='북면 단독주택', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_11, radius=25, fill=True, popup='천안시 11번', color='red', fill_color='orange').add_to(Cheonan_map)



#14번째 확진자
home_14 = '두정동 푸르지오 4차 아파트'
tmp = gmaps.geocode('두정동 푸르지오 4차', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_14=[tmp_loc['lat'], tmp_loc['lng']]

if home_14 in homes :
    loc_14=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_14)
    
folium.Marker(loc_14, popup='두정동 푸르지오 4차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_14, radius=25, fill=True, popup='천안시 14번', color='red', fill_color='orange').add_to(Cheonan_map)



#15번째 확진자
home_15 = '천안시 신부동'
tmp = gmaps.geocode('천안시 신부동', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_15=[tmp_loc['lat'], tmp_loc['lng']]

if home_15 in homes :
    loc_15=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_15)

folium.Marker(loc_15, popup='신부동', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_15, radius=25, fill=True, popup='천안시 15번', color='red', fill_color='orange').add_to(Cheonan_map)



#16번째 확진자
home_16 = '불당지웰푸르지오 아파트'
tmp = gmaps.geocode('불당지웰푸르지오', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_16=[tmp_loc['lat'], tmp_loc['lng']]

if home_16 in homes :
    loc_16=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_16)
    
folium.Marker(loc_16, popup='불당지웰푸르지오 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_16, radius=25, fill=True, popup='천안시 16번', color='red', fill_color='orange').add_to(Cheonan_map)



#17번째 확진자
home_17 = 'e편한세상 두정2차 아파트'
tmp = gmaps.geocode('e편한세상 두정2차', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_17=[tmp_loc['lat'], tmp_loc['lng']]

if home_17 in homes :
    loc_17=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_17)
    
folium.Marker(loc_17, popup='e편한세상 두정2차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_17, radius=25, fill=True, popup='천안시 17번', color='red', fill_color='orange').add_to(Cheonan_map)



#20번째 확진자
home_20 = '쌍용동 쌍용마을 뜨란채 아파트'
tmp = gmaps.geocode('쌍용동 쌍용마을 뜨란채', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_20=[tmp_loc['lat'], tmp_loc['lng']]

if home_20 in homes :
    loc_20=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_20)
    
folium.Marker(loc_20, popup='쌍용마을 뜨란채 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_20, radius=25, fill=True, popup='천안시 20번', color='red', fill_color='orange').add_to(Cheonan_map)



#21번째 확진자
home_21 = '천안영성 펜타폴리스'
tmp = gmaps.geocode('충청남도 천안시 동남구 영성동 67-2', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_21=[tmp_loc['lat'], tmp_loc['lng']]

if home_21 in homes :
    loc_21=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_21)
    
folium.Marker(loc_21, popup='천안영성 펜타폴리스', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_21, radius=25, fill=True, popup='천안시 21번', color='red', fill_color='orange').add_to(Cheonan_map)



# 23번째 확진자
home_23 = '백석동 주공그린빌11단지 아파트'
tmp = gmaps.geocode('백석동 주공그린빌11단지3차 아파트', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_23=[tmp_loc['lat'], tmp_loc['lng']]

if home_23 in homes :
    loc_23=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_23)

folium.Marker(loc_23, popup='백석동 주공그린빌11단지3차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_23, radius=25, fill=True, popup='천안시 23번', color='red', fill_color='orange').add_to(Cheonan_map)



# 25번째 확진자
home_25 = '불당동 린스트라우스2차 아파트'
tmp_lat = 36.8148
tmp_lng = 127.1014
loc_25=[tmp_lat, tmp_lng]

if home_25 in homes :
    loc_25=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_25)
    
folium.Marker(loc_25, popup='불당동 린스트라우스2차 아파트', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_25, radius=25, fill=True, popup='천안시 25번', color='red', fill_color='orange').add_to(Cheonan_map)



#26번째 확진자
home_26 = '불당지웰시티푸르지오 2단지'
tmp_lat = 36.812
tmp_lng = 127.1058
loc_26=[tmp_lat, tmp_lng]

if home_26 in homes :
    loc_26=[tmp_lat+0.0005, tmp_lng+0.0005]
else :
    homes.append(home_26)

folium.Marker(loc_26, popup='불당지웰시티푸르지오 2단지', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_26, radius=25, fill=True, popup='천안시 26번', color='red', fill_color='orange').add_to(Cheonan_map)



#33번째 확진자
home_33 = '성정동 상아빌라'
tmp = gmaps.geocode('성정동 상아빌라', language='ko')
tmp_loc=tmp[0].get('geometry').get('location')
loc_33=[tmp_loc['lat'], tmp_loc['lng']]

if home_33 in homes :
    loc_33=[tmp_loc['lat']+0.0005, tmp_loc['lng']+0.0005]
else :
    homes.append(home_33)

folium.Marker(loc_33, popup='성정동 상아빌라', icon=folium.Icon(color='red', icon='star')).add_to(marker_cluster)
folium.CircleMarker(loc_33, radius=25, fill=True, popup='천안시 33번', color='red', fill_color='orange').add_to(Cheonan_map)


# 중간 저장하기
Cheonan_map.save('C:\LJM\LJM 2020\corona\Cheonan.html')




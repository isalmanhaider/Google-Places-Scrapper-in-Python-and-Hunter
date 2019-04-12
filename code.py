from googleplaces import GooglePlaces, types, lang
import pandas as pd
import numpy as np

df = pd.DataFrame(columns=list(['Place Id','Name','Address','Contact','URL','Lat',"Lng","Service/Business","District"]))

business = ['parlours','salon','beauty clinics','health care centres','gym','physical fitness centres','massage centre','pedicure centre','wedding hall','restaurents','hotel','clinics','caterering','shamiana','lawns','guest houses']
districts = ['Abbottabad','Bannu','Battagram','Buner','Charsadda','Chitral','Dera Ismail Khan','FATA','Hangu','Haripur','Karak','Kohat','Lakki Marwat','Lower Dir','Lower Kohistan','Malakand','Mansehra','Mardan','Nowshera','Peshawar','Shangla','Swabi','Swat','Tank','Torghar','Upper Dir','Upper Kohistan']

YOUR_API_KEY = 'put ur api key here'
google_places = GooglePlaces(YOUR_API_KEY)
counter= 0;
token = ""


for d in districts:
    for b in business:
        q=b+" in "+d
        print(q)
        for r in range(0,4):
            if(r==0):
                query_result = google_places.text_search(query=q)
                print(len(query_result.places))
                for place in query_result.places:
                    print(counter)
                    counter+=1
                    place.get_details()
                    df.loc[counter] = [place.place_id,place.name,place.formatted_address,place.local_phone_number,place.url,place.geo_location['lat'],place.geo_location['lng'],b,d]
            else:
                if(len(query_result.next_page_token)!=0):
                    query_result = google_places.text_search(query=q,pagetoken=query_result.next_page_token)
                    print(len(query_result.places))
                    for place in query_result.places:
                        print(counter)
                        counter+=1
                        place.get_details()
                        df.loc[counter] = [place.place_id,place.name,place.formatted_address,place.local_phone_number,place.url,place.geo_location['lat'],place.geo_location['lng'],b,d]
                        
df

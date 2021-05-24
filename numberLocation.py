import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

Key = 'Your Key'
number = str(input("Enter Phone Number: "))
print(number)

fNumber = phonenumbers.parse(number)
location = geocoder.description_for_number(fNumber, "en")
print(location)

service_provider = carrier.name_for_number(fNumber, "en")
print(str(service_provider))

geocoder = OpenCageGeocode(Key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(map)

map.save('location.html')






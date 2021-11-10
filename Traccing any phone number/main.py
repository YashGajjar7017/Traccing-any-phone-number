# first to install package "pip install phonenumbers" 
import phonenumbers
from test import number
from phonenumbers import geocoder

key = ""
print(f"your number is {number}")

ch_nmber = phonenumbers.parse(number , "CH")  #"CH" ->country history
print(geocoder.description_for_number(ch_nmber, "en"))

#--------------services provider code ------------------
from phonenumbers import carrier

service_nmber = phonenumbers.parse(number ,"RO")
print(carrier.name_for_number(service_nmber ,"en"))

#-----------------location services-----------------
# from opencage.geocoder import OpenCageGeocode
# geocoder = OpenCageGeocode(key)



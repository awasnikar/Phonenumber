import phonenumbers
from test import number

from phonenumbers import geocoder
cc_number = phonenumbers.parse(number, "CH")
print (geocoder.description_for_number(cc_number,"en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

from phonenumbers import timezone
tz_number = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(tz_number))
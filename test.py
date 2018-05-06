import googlemaps

gmaps = googlemaps.Client(key='AIzaSyC543HM-TAYHQW25N6QQ81RbcFTwv6gyUY')

# Geocoding an address
geocode_result = gmaps.geocode('Oostersingel 116c, 9711XH, Groningen')
print(geocode_result[0]['geometry'])

dist = gmaps.distance_matrix('Oostersingel 116c, 9711XH, Groningen', 'Oosterstraat 20, 9951EB, Groningen')
print(dist)
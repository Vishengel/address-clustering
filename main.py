import googlemaps
from data_parser import DataParser
from kmeans import KMeans

gmaps = googlemaps.Client(key='AIzaSyC543HM-TAYHQW25N6QQ81RbcFTwv6gyUY')

dp = DataParser(gmaps)
dp.open_file_path("C:/Users/Jelle/Documents/GitHub/address-clustering/testadressen.csv")
dp.name_address_from_csv()

kmeans = KMeans()
labeled_data, cluster_centers = kmeans.do_kmeans(dp.address_list, 3)

print(labeled_data)

for c in cluster_centers:
    street_name = gmaps.reverse_geocode(c)[0]['address_components'][1]['long_name']
    house_no = gmaps.reverse_geocode(c)[0]['address_components'][0]['long_name']
    print(street_name + " " + house_no)
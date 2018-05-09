import googlemaps
from data_parser import DataParser
from kmeans import KMeans

gmaps = googlemaps.Client(key='AIzaSyC543HM-TAYHQW25N6QQ81RbcFTwv6gyUY')

dp = DataParser(gmaps)
dp.open_file_path("C:/Users/Jelle/Documents/GitHub/address-clustering/testadressen.csv")
dp.name_address_from_csv()

kmeans = KMeans()
kmeans.do_kmeans(dp.address_list, 3)

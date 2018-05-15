import random
import numpy as np
import math

class KMeans():

    def __init__(self):
        pass

    def init_centers_rnd(self, data, k):
        """
        Set k random data points as the initial cluster centers

        :param data: the data to be clustered
        :param k: the amount of clusters
        :return: the k randomly chosen data points as a list of x, y coordinates
        """

        keys = random.sample(list(data), k)
        centers = [data[key]['coords'] for key in keys]

        return centers

    def get_euclidian_dist(self, node_a, node_b):
        """
        Get the Euclidian distance between two addresses, based on latitude/longitude

        :param node_a: first address node. A node is a dictionary with the keys 'lat' and 'lng',
                       their values containing the latitude and longitude, respectively
        :param node_b: second address node
        :return: Euclidian distance between the nodes
        """

        na_coords = np.array([node_a['lat'], node_a['lng']])
        nb_coords = np.array([node_b['lat'], node_b['lng']])

        return np.linalg.norm(na_coords - nb_coords)

    def find_closest_center(self, coords, centers):
        closest_distance = math.inf
        closest_center = -1

        for c in centers:
            dist = self.get_euclidian_dist(coords, c)
            if dist < closest_distance:
                closest_distance = dist
                closest_center = centers.index(c)

        return closest_center

    def check_same_centers(self, old_centers, new_centers):
        return old_centers == new_centers

    def get_labels(self, data, centers):
        # Placeholder function
        for key in data:
            data[key]['label'] = self.find_closest_center(data[key]['coords'], centers)
            print(data[key])

    def get_centers(self, data, k):
        # Placeholder function. Returns a single center with random latitude in (1, 100)
        return [{'lat': random.randint(1, 100), 'lng': 30}]

    def do_kmeans(self, data, k):
        centers = self.init_centers_rnd(data, k)
        old_centers = []
        print(centers)

        while not self.check_same_centers(old_centers, centers):
            old_centers = centers

            self.get_labels(data, centers)
            #centers = list(self.get_centers(data, k))




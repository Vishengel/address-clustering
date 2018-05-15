import random
import numpy as np
import math
import copy

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
        """
        Given a latitude and longitude, find the nearest cluster center

        :param coords: a dict containing a lat and lng value
        :param centers: a list of the cluster centers
        :return: the center closest to the given coordinates
        """
        closest_distance = math.inf
        closest_center = -1

        for c in centers:
            dist = self.get_euclidian_dist(coords, c)
            if dist < closest_distance:
                closest_distance = dist
                closest_center = centers.index(c)

        return closest_center

    def get_labels(self, data, centers):
        """
        Reassign each data point to the nearest cluster center

        :param data: the data to be clustered as a dictionary
        :param centers: a list of cluster centers
        :return: the reassigned data
        """
        for key in data:
            data[key]['label'] = self.find_closest_center(data[key]['coords'], centers)

        return data

    def get_new_centers(self, data, k):
        """
        Calculate the new cluster centers from the data points assigned to each cluster

        :param data: the data with each data point assigned to one of the current klusters
        :param k: the k amount of clusters
        :return: a list containing the new cluster centers
        """
        new_centers = [{'lat': 0, 'lng': 0} for i in range(k)]
        n_labels = [0] * k

        for key in data:
            new_centers[data[key]['label']]['lat'] += data[key]['coords']['lat']
            new_centers[data[key]['label']]['lng'] += data[key]['coords']['lng']
            n_labels[data[key]['label']] += 1

        for c in new_centers:
            c['lat'] /= n_labels[new_centers.index(c)]
            c['lng'] /= n_labels[new_centers.index(c)]

        #print(new_centers)
        return new_centers

    def do_kmeans(self, data, k):
        """
        This function performs the k-means algorithm

        :param data: the data to be clustered as a dictionary
        :param k: the k amount of clusters to be made
        :return: the clustered data and the coordinates of the cluster centers
        """
        centers = self.init_centers_rnd(data, k)
        old_centers = []
        #print("Initial centers: ", centers)

        while not old_centers == centers:
            old_centers = copy.copy(centers)

            data = self.get_labels(data, centers)
            centers = list(self.get_new_centers(data, k))

        return data, centers




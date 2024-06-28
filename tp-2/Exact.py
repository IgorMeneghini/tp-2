import sys
import itertools
import time

class Exact:
    def __init__(self, distance_matrix, num_centers):
        self.distance_matrix = distance_matrix
        self.vertex_numbers = len(distance_matrix)
        self.num_centers = num_centers
        self.min_max_distance = sys.maxsize
        self.optimal_centers = [0] * num_centers

    def find_centers(self, time_limit_ms):
        start_time = time.time()
        for center_combination in itertools.combinations(range(self.vertex_numbers), self.num_centers):
            if time.time() - start_time > time_limit_ms / 1000:
                return [-1]
            current_max_distance = self.calculate_max_distance(center_combination)
            if current_max_distance < self.min_max_distance:
                self.min_max_distance = current_max_distance
                self.optimal_centers = list(center_combination)
        return self.optimal_centers

    def calculate_max_distance(self, centers):
        max_distance = 0
        for vertex_index in range(self.vertex_numbers):
            min_distance_to_center = sys.maxsize
            for center_index in centers:
                min_distance_to_center = min(min_distance_to_center, self.distance_matrix[vertex_index][center_index])
            max_distance = max(max_distance, min_distance_to_center)
        return max_distance


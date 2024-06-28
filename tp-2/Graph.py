import itertools

class Graph:
    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.distance_matrix = [[float('inf')] * vertex_number for _ in range(vertex_number)]

    def add_edge(self, vertex1, vertex2, edge_cost):
        self.distance_matrix[vertex1][vertex2] = edge_cost
        self.distance_matrix[vertex2][vertex1] = edge_cost

    def get_distance(self, vertex1, vertex2):
        return self.distance_matrix[vertex1][vertex2]

    def get_vertex_number(self):
        return self.vertex_number

    def k_centers_exact(self, num_centers):
        all_vertices = list(range(self.vertex_number))
        min_radius = float('inf')
        selected_centers = set()

        for center_subset in itertools.combinations(all_vertices, num_centers):
            max_distance = 0
            for vertex in range(self.vertex_number):
                min_distance_to_center = float('inf')
                for center in center_subset:
                    min_distance_to_center = min(min_distance_to_center, self.distance_matrix[vertex][center])
                max_distance = max(max_distance, min_distance_to_center)
            if max_distance < min_radius:
                min_radius = max_distance
                selected_centers = set(center_subset)
        return selected_centers

    def k_centers_approximation(self, num_centers):
        selected_centers = set()
        is_center = [False] * self.vertex_number
        first_center = 0
        selected_centers.add(first_center)
        is_center[first_center] = True

        while len(selected_centers) < num_centers:
            max_distance = 0
            new_center = -1
            for vertex in range(self.vertex_number):
                if not is_center[vertex]:
                    min_distance_to_center = float('inf')
                    for center in selected_centers:
                        min_distance_to_center = min(min_distance_to_center, self.distance_matrix[vertex][center])
                    if min_distance_to_center > max_distance:
                        max_distance = min_distance_to_center
                        new_center = vertex
            selected_centers.add(new_center)
            is_center[new_center] = True
        return selected_centers

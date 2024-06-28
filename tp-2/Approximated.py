class Approximate:
    """
    A class to solve the K-Center problem approximately using a greedy algorithm.
    """

    def __init__(self, distance_matrix, num_centers):
        """
        Initializes the ApproximateKCenter solver with the distance matrix and the number of centers.

        Args:
            distance_matrix (list of lists): A 2D matrix representing distances between vertices.
            num_centers (int): The desired number of centers.
        """
        self.distance_matrix = distance_matrix
        self.num_vertices = len(distance_matrix)
        self.num_centers = num_centers

    def find_centers(self):
        """
        Solves the K-Center problem approximately.

        Returns:
            list: A list of indices representing the selected centers.
        """
        selected_centers = [-1] * self.num_centers
        is_center = [False] * self.num_vertices

        # Choose the first center arbitrarily
        first_center_index = 0
        selected_centers[0] = first_center_index
        is_center[first_center_index] = True

        # Choose remaining centers greedily
        for i in range(1, self.num_centers):
            farthest_vertex_index = -1
            max_distance = -1

            # Find the vertex farthest from any existing center
            for vertex_index in range(self.num_vertices):
                if not is_center[vertex_index]:
                    min_distance_to_center = 100000
                    for center_index in selected_centers:
                        if center_index != -1:
                            min_distance_to_center = min(
                                min_distance_to_center, 
                                self.distance_matrix[vertex_index][center_index]
                            )
                    if min_distance_to_center > max_distance:
                        max_distance = min_distance_to_center
                        farthest_vertex_index = vertex_index

            # Add the farthest vertex as a center
            selected_centers[i] = farthest_vertex_index
            is_center[farthest_vertex_index] = True

        return selected_centers

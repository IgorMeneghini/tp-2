import os
import time
import numpy as np
from itertools import combinations

from Approximated import Approximate
from Exact import Exact

class Main:
    @staticmethod
    def read_file(file_name):
        with open(file_name, 'r') as file:
            first_line = list(map(int, file.readline().split()))
            vertex_number = first_line[0]
            edges_number = first_line[1]
            k_value = first_line[2]

            distances_matrix = np.full((vertex_number, vertex_number), np.inf)
            np.fill_diagonal(distances_matrix, 0)

            for _ in range(edges_number):
                line_data = list(map(int, file.readline().split()))
                u_index = line_data[0] - 1
                v_index = line_data[1] - 1
                distance_value = line_data[2]
                distances_matrix[u_index][v_index] = distance_value
                distances_matrix[v_index][u_index] = distance_value

            # Aplicando o algoritmo de Floyd-Warshall
            for k_temp in range(vertex_number):
                for i_index in range(vertex_number):
                    for j_index in range(vertex_number):
                        if distances_matrix[i_index][j_index] > distances_matrix[i_index][k_temp] + distances_matrix[k_temp][j_index]:
                            distances_matrix[i_index][j_index] = distances_matrix[i_index][k_temp] + distances_matrix[k_temp][j_index]

        return distances_matrix, k_value

    @staticmethod
    def main_process():
        directory_path = "input"
        file_list = [f_name for f_name in os.listdir(directory_path) if f_name.startswith("pmed") and f_name.endswith(".txt")]

        results_data = []
        file_counter = 0

        for filename in file_list:
            file_counter += 1
            print(f"Processing file: {filename}")
            try:
                result = Main.read_file(os.path.join(directory_path, filename))
                distances_matrix = result[0]
                k_value = result[1]

                print(f"Value of k: {k_value}")

                exact_solver = Exact(distances_matrix, k_value)
                start_exact_time = time.time()
                exact_centers = exact_solver.find_centers(5)
                end_exact_time = time.time()
                exact_duration = end_exact_time - start_exact_time

                approximate_solver = Approximate(distances_matrix, k_value)
                start_approximate_time = time.time()
                approximate_centers = approximate_solver.find_centers()
                end_approximate_time = time.time()
                approximate_duration = end_approximate_time - start_approximate_time

                results_data.append(f"File: {filename}, Exact Centers: {exact_centers}, Executed in: {exact_duration:.4f}s, Approximate Centers: {approximate_centers}, Executed in: {approximate_duration:.4f}s")

            except Exception as e:
                print(f"Error processing file: {filename}")
                print(e)

        print("\nResults:")
        for result_data in results_data:
            print(result_data)


if __name__ == "__main__":
    Main.main_process()

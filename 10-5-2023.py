efficiency = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

# sort the efficiency list in ascending order
sorted_efficiency = sorted(efficiency)

# initialize the minimum cost to infinity
min_cost = float('inf')

# try excluding each worker from the list and pair up the remaining workers
for i in range(len(sorted_efficiency)):
    cost = 0
    remaining_workers = sorted_efficiency[:i] + sorted_efficiency[i+1:]
    for j in range(0, len(remaining_workers), 2):
        cost += abs(remaining_workers[j] - remaining_workers[j+1])
    if cost < min_cost:
        min_cost = cost

print(min_cost)

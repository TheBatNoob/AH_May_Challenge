from itertools import permutations

def find_permutations(number):
    digits = str(number)
    perms = permutations(digits)
    permutations_list = [''.join(perm) for perm in perms]
    return permutations_list

def calculate_average(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    average = (smallest + largest) / 2
    return average

#Number to be permutated
number = 1867
divisible_perm = []
permutations = find_permutations(number)
perm = [int(x) for x in permutations]

for i in perm:
    if i % 7 == 0:
        divisible_perm.append(i)

print(calculate_average(divisible_perm))


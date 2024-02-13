# seqcomb2 = [[['BD', 'E9', '1C'], ['BD', '7A', 'BD'], ['BD', '1C', 'BD', '55']], [['BD', 'E9', '1C'], ['BD', '1C', 'BD', '55'], ['BD', '7A', 'BD']], [['BD', '7A', 'BD'], ['BD', 'E9', '1C'], ['BD', '1C', 'BD', '55']], [['BD', '7A', 'BD'], ['BD', '1C', 'BD', '55'], ['BD', 'E9', '1C']], [['BD', '1C', 'BD', '55'], ['BD', 'E9', '1C'], ['BD', '7A', 'BD']], [['BD', '1C', 'BD', '55'], ['BD', '7A', 'BD'], ['BD', 'E9', '1C']]]
# all_perm = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

from itertools import permutations

def generate_permutations(n):
    numbers = list(range(1, n+1))  # Create a list of numbers from 1 to n
    all_permutations = list(permutations(numbers))  # Generate permutations
    all_permutations_as_lists = [list(permutation) for permutation in all_permutations]  # Convert permutations to list of lists
    return all_permutations_as_lists

def tokens_of_permutations(all_permutations, sequences):
    sequence_combination = []
    for perm in range(len(all_permutations)):
        combination = []
        for i in range(len(all_permutations[0])):
            combination.append(sequences[all_permutations[perm][i]-1])
        sequence_combination.append(combination)
    return sequence_combination

def get_unions(list1, list2):
    combinations = [list1+list2]
    for i in range(min(len(list1), len(list2)) + 1):
        if list1[-i:] == list2[:i]:
            combinations.append(list1 + list2[i:])
    return combinations

def generate_combinations(list, all_permutations):
    each_combinations = get_unions(list[0], list[1])
    combinations = each_combinations
    if (len(list)>2):
        for j in range(2, len(all_permutations[0])):
            each_combinations = combinations
            for k in range(len(each_combinations)):
                each_combinations[k] = get_unions(each_combinations[k], list[j])
                
            combinations = []
            for sublist in each_combinations:
                combinations.extend(sublist)
    return combinations

def generate_all_combinations(sequence_combination, all_permutations):
    all_combinations = []
    for i in range(len(all_permutations)):
        each_combinations = generate_combinations(sequence_combination[i], all_permutations)
        all_combinations.extend(each_combinations)
    return all_combinations

# number_of_sequences =  3
# seq = [['BD', 'E9', '1C'], ['BD', '7A', 'BD'], ['BD', '1C', 'BD', '55']]

# all_perm = generate_permutations(number_of_sequences)
# print(all_perm)
# print()
# seqcomb = tokens_of_permutations(all_perm, seq)
# print(seqcomb)
# print()
# all_combinations = generate_all_combinations(seqcomb, all_perm)
# print(all_combinations)

# for i in range(len(all_perm)):
#     print("kombinasi ke-", i+1)
#     print(all_combinations[i])

# tesss = tes_combinations([['AB', 'BC', 'DU', 'DU'], ['DU', 'DU', 'AI', 'OP'], ['OP', 'AB', 'AB']])
# print(tesss)
# tes = generate_combinations([['AB', 'BC', 'DU', 'DU'], ['DU', 'DU', 'AI', 'OP']])
# print(tes)

# ['AB', 'BC', 'DU', 'DU'], ['DU', 'DU', 'AI', 'OP'], ['OP, 'AB', 'AB']
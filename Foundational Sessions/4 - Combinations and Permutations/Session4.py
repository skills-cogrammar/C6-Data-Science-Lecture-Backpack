import math

# Calculate permutations of 3 out of 5 items
total_permutations = math.perm(5, 3)
print("Total permutations:", total_permutations)

# Calculate combinations of 3 out of 5 items
total_combinations = math.comb(5, 3)
print("Total combinations:", total_combinations)

# Probability of a specific permutation
prob_permutation = 1 / math.perm(5, 3)
print("Probability of a specific permutation:", prob_permutation)

# Probability of a specific combination
prob_combination = 1 / math.comb(5, 3)
print("Probability of a specific combination:", prob_combination)

# ------------------------------------------------------------

# Example program

import math

def calculate_classical_permutation(n, r):
    """
    Calculate permutations of r out of n items using the classical permutation formula.
    This scenario assumes no repetition of items.
    """
    return math.factorial(n) // math.factorial(n - r)

def calculate_classical_combination(n, r):
    """
    Calculate combinations of r out of n items using the classical combination formula.
    Order does not matter in this scenario.
    """
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def calculate_probability(total_outcomes, successful_outcomes):
    """
    Calculate the probability of a specific outcome given the total number of outcomes.
    """
    return successful_outcomes / total_outcomes

def is_valid_group(char_set, specific_group):
    """
    Check if the specific group of characters exists within the initial character set.
    """
    return all(specific_group.count(char) <= char_set.count(char) for char in specific_group)

# User input for the character set
char_set = input("Enter the set of characters (e.g., 'abcdef'): ")
n = len(char_set)

# User input for permutation
r_permutation = int(input(f"Enter the number of characters to arrange from the set of {n} characters (permutation): "))
unique_passwords = calculate_classical_permutation(n, r_permutation)
print(f"Number of unique arrangements (permutations) of {r_permutation} out of {n} characters: {unique_passwords}")

# User input for combination
r_combination = int(input(f"Enter the number of characters to choose from the set of {n} characters (combination): "))
character_groups = calculate_classical_combination(n, r_combination)
print(f"Number of ways to choose {r_combination} out of {n} characters (combinations): {character_groups}")

# User input for calculating probability of a specific combination
specific_group = input(f"Enter a specific group of {r_combination} characters to calculate its probability: ")
while not is_valid_group(char_set, specific_group):
    print(f"The specific group must consist of characters from the initial set '{char_set}' and not use characters more times than they appear.")
    specific_group = input(f"Re-enter the specific group of {r_combination} characters: ")

probability_of_group = calculate_probability(character_groups, 1)
print(f"Probability of randomly choosing the group '{specific_group}': {probability_of_group:.4f}")


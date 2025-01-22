from scipy.stats import kendalltau

# Define the two lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 4, 3, 2, 5, 7, 6, 8, 10, 9]

# Compute the Kendall Tau_b score and p-value
tau, p_value = kendalltau(list1, list2)

# Print the results to a file
with open("kendalltau_results.txt", "w") as f:
    print("Tau_b score: ", tau, file=f)
    print("p-value: ", p_value, file=f)

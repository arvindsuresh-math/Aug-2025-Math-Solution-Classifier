def solve():
    # Number of mango trees Randy has
    mango_trees = 60

    # Calculate half the number of mango trees
    half_mango_trees = mango_trees / 2

    # Calculate the number of coconut trees: 5 less than half the mango trees
    coconut_trees = half_mango_trees - 5

    # Calculate the total number of trees on the farm
    total_trees = mango_trees + coconut_trees

    return int(total_trees)

# Execute the function to get the answer
# print(solve())
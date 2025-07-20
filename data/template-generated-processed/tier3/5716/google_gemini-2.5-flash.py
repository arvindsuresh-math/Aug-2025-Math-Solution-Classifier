def solve():
    """Index: 5716.
    Returns: the total number of tablespoons of popcorn kernels needed.
    """
    # L1
    joanie_cups = 3 # Joanie wants 3 cups of popcorn
    mitchell_cups = 4 # Mitchell wants 4 cups of popcorn
    miles_davis_cups = 6 # Miles and Davis said they would split 6 cups of popcorn
    cliff_cups = 3 # Cliff said he would only eat 3 cups
    total_cups_desired = joanie_cups + mitchell_cups + miles_davis_cups + cliff_cups

    # L2
    kernels_per_batch = 2 # 2 tablespoons of popcorn kernels
    cups_per_batch = 4 # will make 4 cups of popcorn
    num_batches_needed = total_cups_desired / cups_per_batch

    # L3
    total_tablespoons_needed = num_batches_needed * kernels_per_batch

    # FA
    answer = total_tablespoons_needed
    return answer
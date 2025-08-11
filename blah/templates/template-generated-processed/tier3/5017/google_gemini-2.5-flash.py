from fractions import Fraction

def solve():
    """Index: 5017.
    Returns: the total number of data points the dataset contains.
    """
    # L1
    percentage_increase = Fraction(20, 100) # 20% more data points
    initial_data_points = 200 # 200 data points
    added_data_points = percentage_increase * initial_data_points

    # L2
    total_after_addition = initial_data_points + added_data_points

    # L3
    reduction_fraction = Fraction(1, 4) # 1/4 of the total data points
    reduced_data_points = reduction_fraction * total_after_addition

    # L4
    final_data_points = total_after_addition - reduced_data_points

    # FA
    answer = final_data_points
    return answer
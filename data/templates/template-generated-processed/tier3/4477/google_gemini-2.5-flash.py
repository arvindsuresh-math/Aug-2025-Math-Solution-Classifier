from fractions import Fraction

def solve():
    """Index: 4477.
    Returns: the total number of brownies given out.
    """
    # L1
    brownies_per_batch = 20 # with 20 brownies in each batch
    bake_sale_fraction = Fraction(3, 4) # set aside 3/4 of the brownies in each batch for a bake sale
    bake_sale_brownies_per_batch = brownies_per_batch * bake_sale_fraction

    # L2
    remaining_brownies_per_batch_after_sale = brownies_per_batch - bake_sale_brownies_per_batch

    # L3
    container_fraction = Fraction(3, 5) # put 3/5 of the remaining in a container
    container_brownies_per_batch = remaining_brownies_per_batch_after_sale * container_fraction

    # L4
    given_out_brownies_per_batch = remaining_brownies_per_batch_after_sale - container_brownies_per_batch

    # L5
    num_batches = 10 # 10 batches of brownies
    total_brownies_given_out = given_out_brownies_per_batch * num_batches

    # FA
    answer = total_brownies_given_out
    return answer
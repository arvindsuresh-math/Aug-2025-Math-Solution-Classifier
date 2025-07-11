from fractions import Fraction

def solve():
    """Index: 2028.
    Returns: the total number of ornamental rings remaining in the store.
    """
    # L1
    restocked_rings = 200 # Eliza buys 200 ornamental rings
    multiplier = 2 # twice the number of the remaining stock
    original_stock = restocked_rings / multiplier

    # L2
    total_initial_stock = restocked_rings + original_stock

    # L3
    sold_fraction = Fraction(3, 4) # 3/4 of the total stock
    rings_sold_first_batch = sold_fraction * total_initial_stock

    # L4
    remaining_stock_after_first_sale = total_initial_stock - rings_sold_first_batch

    # L5
    mother_buys = 300 # her mother buys 300 more ornamental rings
    stock_after_mother_buys = remaining_stock_after_first_sale + mother_buys

    # L6
    second_sale = 150 # sells 150
    final_remaining_stock = stock_after_mother_buys - second_sale

    # FA
    answer = final_remaining_stock
    return answer
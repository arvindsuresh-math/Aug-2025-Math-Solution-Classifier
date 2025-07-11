from fractions import Fraction

def solve():
    """Index: 1561.
    Returns: the number of stamps Marie can give away.
    """
    # L1
    num_notebooks = 4 # 4 notebooks
    stamps_per_notebook = 20 # 20 stamps each
    stamps_from_notebooks = num_notebooks * stamps_per_notebook

    # L2
    num_binders = 2 # two binders
    stamps_per_binder = 50 # 50 stamps each
    stamps_from_binders = num_binders * stamps_per_binder

    # L3
    total_stamps = stamps_from_notebooks + stamps_from_binders

    # L4
    fraction_to_keep = Fraction(1, 4) # 1/4 of the stamps
    stamps_to_keep = total_stamps * fraction_to_keep

    # L5
    stamps_to_give_away = total_stamps - stamps_to_keep

    # FA
    answer = stamps_to_give_away
    return answer
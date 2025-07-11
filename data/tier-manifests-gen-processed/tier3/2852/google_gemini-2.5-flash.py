from fractions import Fraction

def solve():
    """Index: 2852.
    Returns: the number of fewer ounces of parmesan cheese James needs to use.
    """
    # L1
    sodium_per_oz_parmesan = 25 # parmesan has 25 mg of sodium per oz
    parmesan_oz = 8 # 8 oz of parmesan cheese
    total_sodium_parmesan = sodium_per_oz_parmesan * parmesan_oz

    # L2
    sodium_per_tsp_salt = 50 # Salt has 50 mg of sodium per teaspoon
    salt_tsp = 2 # 2 teaspoons of salt
    total_sodium_salt = sodium_per_tsp_salt * salt_tsp

    # L3
    initial_total_sodium = total_sodium_salt + total_sodium_parmesan

    # L4
    reduction_fraction = Fraction(1, 3) # reduce the total amount of sodium by 1/3rd
    desired_sodium_reduction = initial_total_sodium * reduction_fraction

    # L5
    fewer_parmesan_oz_needed = desired_sodium_reduction / sodium_per_oz_parmesan

    # FA
    answer = fewer_parmesan_oz_needed
    return answer
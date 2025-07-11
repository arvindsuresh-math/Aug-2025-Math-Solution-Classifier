from fractions import Fraction

def solve():
    """Index: 1855.
    Returns: the total number of citizens in the town.
    """
    # L1
    total_fraction_pet_owners = 1 # WK
    fraction_own_dog = Fraction(1, 2) # half own a dog
    fraction_own_cat = total_fraction_pet_owners - fraction_own_dog

    # L2
    num_cat_owners = 30 # 30 own a cat
    total_pet_owners = num_cat_owners / fraction_own_cat

    # L3
    percent_citizens_own_pet = 0.6 # 60% of the citizens own a pet
    total_citizens = total_pet_owners / percent_citizens_own_pet

    # FA
    answer = total_citizens
    return answer
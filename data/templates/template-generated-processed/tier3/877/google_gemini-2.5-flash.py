def solve():
    """Index: 877.
    Returns: the number of strawberries each family member would have if divided equally.
    """
    # L1
    brother_baskets = 3 # 3 baskets
    strawberries_per_basket = 15 # each containing 15 strawberries
    brother_strawberries = brother_baskets * strawberries_per_basket

    # L2
    kimberly_multiplier = 8 # 8 times the amount of strawberries her brother picked
    kimberly_strawberries = kimberly_multiplier * brother_strawberries

    # L3
    parents_less_than_kimberly = 93 # her parents picked 93 strawberries less than her
    parents_strawberries = kimberly_strawberries - parents_less_than_kimberly

    # L4
    total_strawberries = brother_strawberries + kimberly_strawberries + parents_strawberries

    # L5
    family_members = 4 # divide the total number of strawberries equally amongst them
    strawberries_per_person = total_strawberries / family_members

    # FA
    answer = strawberries_per_person
    return answer
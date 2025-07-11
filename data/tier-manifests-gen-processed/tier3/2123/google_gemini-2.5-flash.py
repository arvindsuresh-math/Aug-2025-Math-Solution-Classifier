def solve():
    """Index: 2123.
    Returns: the number of bags Bruce can buy with the change.
    """
    # L1
    packs_of_crayons = 5 # 5 packs of crayons
    cost_per_crayon_pack = 5 # $5 each
    cost_crayons = packs_of_crayons * cost_per_crayon_pack

    # L2
    num_books = 10 # 10 books
    cost_per_book = 5 # $5 each
    cost_books = num_books * cost_per_book

    # L3
    num_calculators = 3 # 3 calculators
    cost_per_calculator = 5 # $5 each
    cost_calculators = num_calculators * cost_per_calculator

    # L4
    initial_money = 200 # If he has $200
    remaining_money = initial_money - cost_crayons - cost_books - cost_calculators

    # L5
    cost_per_bag = 10 # one costs $10 each
    num_bags = remaining_money / cost_per_bag

    # FA
    answer = num_bags
    return answer
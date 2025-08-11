def solve():
    """Index: 3347.
    Returns: the total money they will donate to their class funds.
    """
    # L1
    barbara_num_animals = 9 # Barbara has 9 stuffed animals
    barbara_price_per_animal = 2 # sell her stuffed animals for $2 each
    barbara_total_money = barbara_num_animals * barbara_price_per_animal

    # L2
    trish_multiplier = 2 # two times as many stuffed animals as Barbara
    trish_num_animals = barbara_num_animals * trish_multiplier

    # L3
    trish_price_per_animal = 1.50 # Trish will sell them for $1.50 each
    trish_total_money = trish_num_animals * trish_price_per_animal

    # L4
    total_donation = barbara_total_money + trish_total_money

    # FA
    answer = total_donation
    return answer
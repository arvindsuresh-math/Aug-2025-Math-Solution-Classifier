def solve():
    """Index: 1732.
    Returns: the number of scoops of ice cream left after all the kids eat.
    """
    # L1
    num_cartons = 3 # Mary has 3 cartons of ice cream
    scoops_per_carton = 10 # contains 10 scoops each
    total_scoops = num_cartons * scoops_per_carton

    # L2
    lucas_danny_connor_scoops_each = 2 # all want 2 scoops of chocolate
    num_lucas_danny_connor = 3 # Lucas, Danny and Connor
    lucas_danny_connor_total = lucas_danny_connor_scoops_each * num_lucas_danny_connor

    # L3
    olivia_vanilla = 1 # Olivia would like a scoop of vanilla
    olivia_strawberry = 1 # and one of strawberry
    shannon_multiplier = 2 # Shannon wants twice as much as Olivia
    shannon_total = shannon_multiplier * (olivia_vanilla + olivia_strawberry)

    # L4
    ethan_vanilla = 1 # Ethan wants one scoop of vanilla
    ethan_chocolate = 1 # and one of chocolate
    olivia_total = olivia_vanilla + olivia_strawberry
    total_eaten = ethan_vanilla + lucas_danny_connor_total + ethan_chocolate + shannon_total

    # L5
    scoops_left = total_scoops - total_eaten

    # FA
    answer = scoops_left
    return answer
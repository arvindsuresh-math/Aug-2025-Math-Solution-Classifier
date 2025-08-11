def solve():
    """Index: 5380.
    Returns: the amount of candy each person will have.
    """
    # L1
    hugh_candy = 8 # Hugh had eight pounds of candy
    tommy_candy = 6 # Tommy had six pounds of candy
    hugh_tommy_total = hugh_candy + tommy_candy

    # L2
    melany_candy = 7 # Melany had seven pounds of candy
    total_candy = hugh_tommy_total + melany_candy

    # L3
    num_people = 3 # If they share the candy equally
    candy_per_person = total_candy / num_people

    # FA
    answer = candy_per_person
    return answer
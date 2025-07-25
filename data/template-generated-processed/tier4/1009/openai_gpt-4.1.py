def solve():
    """Index: 1009.
    Returns: the number of male alligators on Lagoon island.
    """
    # L1
    percent_total = 100 # WK
    percent_juvenile_females = 40 # 40% are juveniles
    percent_adult_females = percent_total - percent_juvenile_females

    # L2
    num_adult_females = 15 # 15 adult females
    percent_adult_females_decimal = 0.6 # 60% as decimal
    num_female_alligators = num_adult_females / percent_adult_females_decimal

    # L3
    percent_female_alligators = 0.5 # Half the alligators are male, so half are female
    num_total_alligators = num_female_alligators / percent_female_alligators

    # L4
    num_male_alligators = num_total_alligators / 2

    # FA
    answer = num_male_alligators
    return answer
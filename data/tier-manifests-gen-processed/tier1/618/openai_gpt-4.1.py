def solve():
    """Index: 618.
    Returns: the percentage chance Jack catches either Zika virus or malaria after being bitten by a random mosquito, accounting for the vaccine.
    """
    # L1
    malaria_pct = 40 # 40% of the mosquitos in Jack's area are infected with malaria
    zika_pct = 20 # 20% of the mosquitos are infected with Zika virus
    infected_mosquito_pct = malaria_pct + zika_pct

    # L2
    infection_chance_no_vaccine = 50 # chances of getting infected after getting bitten by an infected mosquito are 50%
    chance_infected_no_vaccine = infected_mosquito_pct * infection_chance_no_vaccine / 100

    # L3
    vaccine_reduction_pct = 50 # vaccine reduces the chances of getting infected after getting bitten by 50%
    chance_infected_with_vaccine = chance_infected_no_vaccine * vaccine_reduction_pct / 100

    # FA
    answer = chance_infected_with_vaccine
    return answer
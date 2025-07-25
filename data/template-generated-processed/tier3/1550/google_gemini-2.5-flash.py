from fractions import Fraction

def solve():
    """Index: 1550.
    Returns: the number of plants that will produce flowers.
    """
    # L1
    daisy_germination_rate = Fraction(60, 100) # 60% of the daisy seeds germinate
    daisy_seeds_planted = 25 # planted 25 daisy seeds
    germinated_daisy_plants = daisy_germination_rate * daisy_seeds_planted

    # L2
    sunflower_germination_rate = Fraction(80, 100) # 80% of the sunflower seeds germinate
    sunflower_seeds_planted = 25 # 25 sunflower seeds
    germinated_sunflower_plants = sunflower_germination_rate * sunflower_seeds_planted

    # L3
    total_germinated_plants = germinated_daisy_plants + germinated_sunflower_plants

    # L4
    flower_production_rate = Fraction(80, 100) # 80% of the resulting plants produce flowers
    plants_producing_flowers = flower_production_rate * total_germinated_plants

    # FA
    answer = plants_producing_flowers
    return answer
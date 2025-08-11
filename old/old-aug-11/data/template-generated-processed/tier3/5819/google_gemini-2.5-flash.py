from fractions import Fraction

def solve():
    """Index: 5819.
    Returns: the total number of minutes Casey needs to spend pumping water.
    """
    # L1
    plants_per_row = 15 # 15 corn plants each
    num_rows = 4 # 4 rows
    total_corn_plants = plants_per_row * num_rows

    # L2
    water_per_corn_plant_fraction = Fraction(1, 2) # half a gallon of water
    total_water_for_corn = total_corn_plants * water_per_corn_plant_fraction

    # L3
    num_pigs = 10 # 10 pigs
    water_per_pig = 4 # each need 4 gallons of water
    total_water_for_pigs = num_pigs * water_per_pig

    # L4
    num_ducks = 20 # 20 ducks
    water_per_duck_fraction = Fraction(1, 4) # a quarter of a gallon of water
    total_water_for_ducks = num_ducks * water_per_duck_fraction

    # L5
    total_water_needed = total_water_for_ducks + total_water_for_pigs + total_water_for_corn

    # L6
    pumping_rate = 3 # pump 3 gallons a minute
    time_pumping_minutes = total_water_needed / pumping_rate

    # FA
    answer = time_pumping_minutes
    return answer
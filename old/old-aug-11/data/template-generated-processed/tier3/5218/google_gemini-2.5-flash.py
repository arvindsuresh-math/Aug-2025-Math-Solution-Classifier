from fractions import Fraction

def solve():
    """Index: 5218.
    Returns: the total number of fish caught by Brian and Chris.
    """
    # L1
    brian_fish_per_trip = 400 # Brian caught 400 fish every time he went fishing
    brian_trips_multiplier_for_calc = 2 # Brian goes fishing twice as often as Chris
    brian_fish_in_two_trips = brian_fish_per_trip * brian_trips_multiplier_for_calc

    # L2
    fewer_fish_fraction = Fraction(2, 5) # 2/5 times fewer fish than Chris per trip
    chris_additional_fish_per_trip = fewer_fish_fraction * brian_fish_per_trip

    # L3
    chris_fish_per_trip = brian_fish_per_trip + chris_additional_fish_per_trip

    # L4
    chris_total_trips = 10 # Chris went fishing 10 times
    chris_total_fish = chris_fish_per_trip * chris_total_trips

    # L5
    brian_total_fish = brian_fish_in_two_trips * chris_total_trips

    # L6
    total_fish_caught = brian_total_fish + chris_total_fish

    # FA
    answer = total_fish_caught
    return answer
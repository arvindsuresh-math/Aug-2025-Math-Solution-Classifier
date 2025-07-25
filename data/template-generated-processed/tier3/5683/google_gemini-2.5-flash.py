def solve():
    """Index: 5683.
    Returns: the number of miles Harriet ran.
    """
    # L1
    total_miles = 195 # combined total of 195 miles
    katarina_miles = 51 # Katarina ran 51 miles
    remaining_miles = total_miles - katarina_miles

    # L2
    num_other_runners = 3 # Tomas, Tyler, and Harriet all ran the same distance
    harriet_miles = remaining_miles / num_other_runners

    # L3
    harriet_final_miles = harriet_miles

    # FA
    answer = harriet_final_miles
    return answer
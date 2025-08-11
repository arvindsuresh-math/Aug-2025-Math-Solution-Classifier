def solve():
    """Index: 5448.
    Returns: the difference in miles run per hour between Frank and Jim.
    """
    # L1
    jim_total_miles = 16 # Jim ran 16 miles
    jim_total_hours = 2 # in 2 hours
    jim_miles_per_hour = jim_total_miles / jim_total_hours

    # L2
    frank_total_miles = 20 # Frank ran 20 miles
    frank_total_hours = 2 # in 2 hours
    frank_miles_per_hour = frank_total_miles / frank_total_hours

    # L3
    difference_miles_per_hour = frank_miles_per_hour - jim_miles_per_hour

    # FA
    answer = difference_miles_per_hour
    return answer
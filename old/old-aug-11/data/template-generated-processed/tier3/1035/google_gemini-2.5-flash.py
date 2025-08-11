from fractions import Fraction

def solve():
    """Index: 1035.
    Returns: 60% of the total number of boys and girls at the event.
    """
    # L1
    boys_count = 600 # 600 boys at the event
    difference_boys_girls = 400 # difference between the number of boys and girls in a tree planting event is 400
    girls_count = boys_count + difference_boys_girls

    # L2
    total_attendees = girls_count + boys_count

    # L3
    percentage_of_total = Fraction(60, 100) # 60% of the total number
    sixty_percent_of_total = percentage_of_total * total_attendees

    # FA
    answer = sixty_percent_of_total
    return answer
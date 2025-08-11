def solve():
    """Index: 1629.
    Returns: the number of visitors that go to the gorilla exhibit in one day.
    """
    # L1
    visitors_per_hour = 50 # 50 new visitors entering the zoo every hour
    hours_open = 8 # zoo is open for 8 hours in one day
    total_visitors = visitors_per_hour * hours_open

    # L2
    gorilla_exhibit_percent = 0.80 # 80% of the total visitors go to the gorilla exhibit
    gorilla_visitors = total_visitors * gorilla_exhibit_percent

    # FA
    answer = gorilla_visitors
    return answer
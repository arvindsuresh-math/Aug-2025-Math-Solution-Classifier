def solve():
    """Index: 6191.
    Returns: the number of fans who attended the show.
    """
    # L1
    percent_seats_sold = 0.75 # 75% of the seats
    total_seats = 60000 # seats 60,000 fans
    seats_sold = percent_seats_sold * total_seats

    # L2
    fans_stayed_home = 5000 # 5,000 fans stayed home
    attended_show = seats_sold - fans_stayed_home

    # FA
    answer = attended_show
    return answer
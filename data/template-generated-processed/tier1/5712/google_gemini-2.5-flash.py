def solve():
    """Index: 5712.
    Returns: the total number of passengers the airline company can accommodate each day.
    """
    # L1
    rows_per_airplane = 20 # 20 rows
    seats_per_row = 7 # 7 seats in each row
    seats_per_airplane = rows_per_airplane * seats_per_row

    # L2
    num_airplanes = 5 # 5 airplanes
    total_seats_all_airplanes = seats_per_airplane * num_airplanes

    # L3
    flights_per_day_per_airplane = 2 # 2 flights a day
    total_passengers_per_day = total_seats_all_airplanes * flights_per_day_per_airplane

    # FA
    answer = total_passengers_per_day
    return answer
def solve():
    """Index: 3648.
    Returns: the number of dishes Billy needs to wash.
    """
    # L1
    billy_laundry_loads = 2 # Billy does two loads of laundry
    minutes_per_load = 9 # doing laundry takes 9 minutes per load
    billy_laundry_time = billy_laundry_loads * minutes_per_load

    # L2
    minutes_per_room = 3 # Sweeping takes 3 minutes per room
    anna_sweeping_rooms = 10 # Anna does the sweeping for 10 rooms
    anna_sweeping_time = minutes_per_room * anna_sweeping_rooms

    # L3
    time_difference = anna_sweeping_time - billy_laundry_time

    # L4
    minutes_per_dish = 2 # washing the dishes takes 2 minutes per dish
    dishes_to_wash = time_difference / minutes_per_dish

    # FA
    answer = dishes_to_wash
    return answer
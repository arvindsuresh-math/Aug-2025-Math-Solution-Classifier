def solve():
    # Number of floors in the hotel
    total_floors = 10
    # Number of identical rooms on each floor
    rooms_per_floor = 10
    # Number of floors unavailable for guests
    unavailable_floors = 1

    # Calculate the total number of rooms in the hotel
    total_rooms = total_floors * rooms_per_floor

    # Calculate the number of rooms on the unavailable floor(s)
    rooms_on_unavailable_floor = unavailable_floors * rooms_per_floor

    # Calculate the number of available rooms
    available_rooms = total_rooms - rooms_on_unavailable_floor

    return available_rooms

# Execute the function to get the answer
answer = solve()
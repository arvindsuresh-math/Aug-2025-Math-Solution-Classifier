def solve_51():
    # Original bolt dimensions
    bolt_length = 16
    bolt_width = 12
    
    # Living room curtain dimensions
    living_room_length = 4
    living_room_width = 6
    
    # Bedroom curtain dimensions
    bedroom_length = 2
    bedroom_width = 4
    
    # Calculate the area of the original bolt of fabric
    total_fabric_area = bolt_length * bolt_width
    
    # Calculate the area of fabric used for the living room curtains
    living_room_fabric_area = living_room_length * living_room_width
    
    # Calculate the area of fabric used for the bedroom curtains
    bedroom_fabric_area = bedroom_length * bedroom_width
    
    # Calculate the total fabric used
    total_fabric_used = living_room_fabric_area + bedroom_fabric_area
    
    # Calculate the remaining fabric
    remaining_fabric = total_fabric_area - total_fabric_used
    
    return remaining_fabric
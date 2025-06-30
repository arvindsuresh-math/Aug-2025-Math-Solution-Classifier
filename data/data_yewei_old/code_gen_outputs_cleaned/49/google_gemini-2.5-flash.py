def solve_49():
    """
    Calculates the number of shells Alan collected based on the given information.
    """
    laurie_shells = 36
    
    # Ben collected a third of what Laurie did
    ben_shells = laurie_shells / 3
    
    # Alan collected four times as many shells as Ben did
    alan_shells = ben_shells * 4
    
    return int(alan_shells)

# Execute the function to get the answer
alan_collected_shells = solve_49()
def solve():
    # Gumballs given to Todd
    gumballs_todd = 4

    # Gumballs given to Alisha: twice as many as Todd
    gumballs_alisha = 2 * gumballs_todd

    # Gumballs given to Bobby: 5 less than four times as many as Alisha
    gumballs_bobby = (4 * gumballs_alisha) - 5

    # Gumballs remaining with Hector
    gumballs_remaining = 6

    # Total gumballs purchased by Hector
    total_gumballs = gumballs_todd + gumballs_alisha + gumballs_bobby + gumballs_remaining

    return total_gumballs

# Execute the function to get the answer
answer = solve()
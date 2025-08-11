def solve():
    """Index: 3484.
    Returns: the shortest time after which the three bulbs will be on at the same time.
    """
    # Helper functions for LCM
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // gcd(a, b)

    # L4
    red_light_interval = 2 # a red light bulb which comes on every 2 seconds
    green_light_interval = 3 # a green one every 3 seconds
    blue_light_interval = 4 # a blue one every 4 seconds
    lcm_of_first_two = lcm(red_light_interval, green_light_interval)
    shortest_time = lcm(lcm_of_first_two, blue_light_interval)

    # FA
    answer = shortest_time
    return answer
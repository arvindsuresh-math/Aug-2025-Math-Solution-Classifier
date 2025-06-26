def solve(initial_balls: int = 175, # He loads up the machine with 175 tennis balls to start with
    first_batch_size: int = 100, # Out of the first 100 balls
    fraction_hit_first_batch: float = 2/5, # he manages to hit 2/5 of them
    second_batch_size: int = 75, # Of the next 75 tennis balls
    fraction_hit_second_batch: float = 1/3 # he manages to hit 1/3 of them
):
    """Index: 25.
Returns: the total number of tennis balls Ralph did not hit."""
    #: L1
    fraction_not_hit_first_batch = 1 - fraction_hit_first_batch
    not_hit_first_batch = fraction_not_hit_first_batch * first_batch_size

    #: L2
    fraction_not_hit_second_batch = 1 - fraction_hit_second_batch
    not_hit_second_batch = fraction_not_hit_second_batch * second_batch_size

    #: L3
    total_not_hit = not_hit_first_batch + not_hit_second_batch

    answer = total_not_hit # FINAL ANSWER
    return answer

# --- EXECUTION TRACE (value_dict) ---
"""
{
    "initial_balls": "175/1",
    "first_batch_size": "100/1",
    "fraction_hit_first_batch": "2/5",
    "second_batch_size": "75/1",
    "fraction_hit_second_batch": "1/3",
    "fraction_not_hit_first_batch": "3/5",
    "not_hit_first_batch": "60/1",
    "fraction_not_hit_second_batch": "2/3",
    "not_hit_second_batch": "50/1",
    "total_not_hit": "110/1",
    "answer": "110/1"
}
"""

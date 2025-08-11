def solve():
    """Index: 602.
    Returns: the amount of money each writer from fourth place onwards will earn.
    """
    # L1
    first_prize = 200 # First place will get $200
    second_prize = 150 # second place will get $150
    third_prize = 120 # third place $120
    sum_top_three = first_prize + second_prize + third_prize

    # L2
    total_prize = 800 # award a total of $800 in prizes
    remaining_prize = total_prize - sum_top_three

    # L3
    total_awards = 18 # to the 18 novels with the most votes
    top_three_awards = 3 # First, second, third place
    remaining_awards = total_awards - top_three_awards

    # L4
    per_writer_award = remaining_prize / remaining_awards

    # FA
    answer = per_writer_award
    return answer
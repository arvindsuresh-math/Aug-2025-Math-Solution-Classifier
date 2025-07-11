def solve():
    """Index: 602.
    Returns: the amount of money each writer earns from fourth place onwards.
    """
    # L1
    first_place_prize = 200 # First place will get $200
    second_place_prize = 150 # second place will get $150
    third_place_prize = 120 # third place $120
    sum_first_three_prizes = first_place_prize + second_place_prize + third_place_prize

    # L2
    total_prize_money = 800 # award a total of $800 in prizes
    remaining_prize_money = total_prize_money - sum_first_three_prizes

    # L3
    total_novels_awarded = 18 # 18 novels with the most votes
    num_top_prizes = 3 # first, second, third place
    remaining_novels_to_award = total_novels_awarded - num_top_prizes

    # L4
    prize_per_writer_fourth_onwards = remaining_prize_money / remaining_novels_to_award

    # FA
    answer = prize_per_writer_fourth_onwards
    return answer
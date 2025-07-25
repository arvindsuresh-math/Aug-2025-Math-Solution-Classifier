def solve():
    """Index: 7294.
    Returns: the total number of envelopes Micah needed to buy.
    """
    # L1
    num_light_envelopes = 6 # 6 envelopes that weigh less than 5 pounds
    stamps_per_light_envelope = 2 # it will only need 2 stamps
    stamps_for_light_envelopes = num_light_envelopes * stamps_per_light_envelope

    # L2
    total_stamps_bought = 52 # bought 52 stamps
    remaining_stamps = total_stamps_bought - stamps_for_light_envelopes

    # L3
    stamps_per_heavy_envelope = 5 # he will need 5 stamps
    num_heavy_envelopes = remaining_stamps / stamps_per_heavy_envelope

    # L4
    total_envelopes = num_heavy_envelopes + num_light_envelopes

    # FA
    answer = total_envelopes
    return answer
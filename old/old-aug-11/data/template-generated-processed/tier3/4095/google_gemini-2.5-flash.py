def solve():
    """Index: 4095.
    Returns: the combined length of time, in minutes, that the three entertainers stand on their back legs.
    """
    # L1
    polly_multiplier = 3 # three times as long as Pulsar
    pulsar_time = 10 # Pulsar stands on his two back legs for a total of 10 minutes
    polly_time = polly_multiplier * pulsar_time

    # L2
    petra_divisor = 6 # one-sixth as long as Polly
    petra_time = polly_time / petra_divisor

    # L3
    total_time = pulsar_time + polly_time + petra_time

    # FA
    answer = total_time
    return answer
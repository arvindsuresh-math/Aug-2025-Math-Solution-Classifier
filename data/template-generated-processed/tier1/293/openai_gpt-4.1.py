def solve():
    """Index: 293.
    Returns: the total combined amount of time Carlotta spends practicing, throwing tantrums, and singing in the final stage performance.
    """
    # L1
    performance_minutes = 6 # her final stage performance is 6 minutes long
    practice_per_minute = 3 # spends an additional 3 minutes practicing per minute on stage
    practice_minutes = performance_minutes * practice_per_minute

    # L2
    tantrum_per_minute = 5 # spends 5 minutes throwing temper tantrums per minute on stage
    tantrum_minutes = performance_minutes * tantrum_per_minute

    # L3
    total_minutes = practice_minutes + tantrum_minutes + performance_minutes

    # FA
    answer = total_minutes
    return answer
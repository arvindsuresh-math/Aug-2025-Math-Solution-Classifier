def solve():
    """Index: 4702.
    Returns: how long, in seconds, Buffy held her breath underwater.
    """
    # L1
    kelly_minutes = 3 # Kelly held her breath underwater for 3 minutes
    seconds_per_minute = 60 # WK
    kelly_seconds = kelly_minutes * seconds_per_minute

    # L2
    brittany_less_than_kelly = 20 # 20 seconds less time than than Kelly did
    brittany_seconds = kelly_seconds - brittany_less_than_kelly

    # L3
    buffy_less_than_brittany = 40 # 40 seconds less time than Brittany did
    buffy_seconds = brittany_seconds - buffy_less_than_brittany

    # FA
    answer = buffy_seconds
    return answer
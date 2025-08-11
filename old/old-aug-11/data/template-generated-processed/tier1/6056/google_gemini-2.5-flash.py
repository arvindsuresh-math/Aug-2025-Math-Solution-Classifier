def solve():
    """Index: 6056.
    Returns: how late, in minutes, Ingrid was to the party.
    """
    # L1
    paul_arrival_time_minutes_representation = 825 # Paul arrived at 8:25
    party_start_time_minutes_representation = 800 # party planned to start at 8:00 a.m.
    paul_late_minutes = paul_arrival_time_minutes_representation - party_start_time_minutes_representation

    # L2
    amoura_delay_from_paul = 30 # Amoura arrived 30 minutes later than Paul
    amoura_late_minutes = paul_late_minutes + amoura_delay_from_paul

    # L3
    ingrid_multiplier = 3 # Ingrid was three times later than Amoura
    ingrid_late_minutes = ingrid_multiplier * amoura_late_minutes

    # FA
    answer = ingrid_late_minutes
    return answer
def solve():
    """Index: 7394.
    Returns: the total number of tents in the recreation area.
    """
    # L1
    northernmost_tents = 100 # 100 tents in the northernmost part of the campsite
    east_multiplier = 2 # twice that number on the east side
    eastern_tents = east_multiplier * northernmost_tents

    # L2
    northern_and_eastern_tents = eastern_tents + northernmost_tents

    # L3
    central_multiplier = 4 # four times the number of tents in the northernmost part
    central_tents = central_multiplier * northernmost_tents

    # L4
    total_three_parts = central_tents + northern_and_eastern_tents

    # L5
    southern_tents = 200 # 200 tents in the southern part of the campsite
    total_campsite_tents = total_three_parts + southern_tents

    # FA
    answer = total_campsite_tents
    return answer
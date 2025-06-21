def solve(
    total_skeletons: int = 20, # In a graveyard, there are 20 skeletons
    bones_per_woman: int = 20, # an adult woman has 20 bones in their body
    extra_bones_per_man: int = 5 # a male has 5 more than this
):
    """Index: 1205.
    Returns: the total number of bones in the graveyard.
    """
    #: L1
    num_women = total_skeletons / 2

    #: L2
    num_men = (total_skeletons - num_women) / 2
    num_children = (total_skeletons - num_women) / 2 # The remaining number are split evenly

    #: L3
    total_bones_women = bones_per_woman * num_women

    #: L4
    bones_per_man = bones_per_woman + extra_bones_per_man

    #: L5
    total_bones_men = bones_per_man * num_men

    #: L6
    bones_per_child = bones_per_woman / 2

    #: L7
    total_bones_children = bones_per_child * num_children

    #: L8
    total_bones_graveyard = total_bones_women + total_bones_men + total_bones_children

    answer = total_bones_graveyard # FINAL ANSWER
    return answer
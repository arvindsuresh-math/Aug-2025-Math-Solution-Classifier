def solve(
    total_skeletons: int = 20,  # "In a graveyard, there are 20 skeletons."
    adult_women_fraction: float = 0.5,  # "Half of these skeletons are adult women"
    bones_adult_woman: int = 20,  # "an adult woman has 20 bones in their body"
    additional_bones_male: int = 5,  # "a male has 5 more than this"
    child_fraction: float = 0.5  # "a child has half as many as an adult woman"
):
    """Index: 1205.
    Returns: the total number of bones in the graveyard.
    """
    #: L1
    adult_women_count = total_skeletons * adult_women_fraction  # 20/2 = 10

    #: L2
    remaining_skeletons = total_skeletons - adult_women_count  # 20 - 10 = 10
    adult_men_count = remaining_skeletons / 2  # 10/2 = 5
    children_count = remaining_skeletons / 2  # 10/2 = 5

    #: L3
    total_bones_women = bones_adult_woman * adult_women_count  # 20*10 = 200

    #: L4
    bones_adult_man = bones_adult_woman + additional_bones_male  # 20+5 = 25

    #: L5
    total_bones_men = bones_adult_man * adult_men_count  # 25*5 = 125

    #: L6
    bones_child = bones_adult_woman * child_fraction  # 20*0.5 = 10

    #: L7
    total_bones_children = children_count * bones_child  # 5*10 = 50

    #: L8
    total_bones = total_bones_women + total_bones_men + total_bones_children  # 200+125+50 = 375

    answer = total_bones  # FINAL ANSWER
    return answer
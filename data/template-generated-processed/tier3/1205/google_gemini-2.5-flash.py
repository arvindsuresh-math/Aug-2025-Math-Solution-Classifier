def solve():
    """Index: 1205.
    Returns: the total number of bones in the graveyard.
    """
    # L1
    total_skeletons = 20 # there are 20 skeletons
    half_divisor = 2 # Half of these skeletons
    adult_women_skeletons = total_skeletons / half_divisor

    # L2
    split_divisor = 2 # split evenly between adult men and children
    men_children_skeletons_each = adult_women_skeletons / split_divisor

    # L3
    bones_per_adult_woman = 20 # an adult woman has 20 bones
    total_bones_women = bones_per_adult_woman * adult_women_skeletons

    # L4
    extra_bones_men = 5 # a male has 5 more than this
    bones_per_adult_man = bones_per_adult_woman + extra_bones_men

    # L5
    total_bones_men = bones_per_adult_man * men_children_skeletons_each

    # L6
    child_bone_divisor = 2 # a child has half as many as an adult woman
    bones_per_child = bones_per_adult_woman / child_bone_divisor

    # L7
    total_bones_children = men_children_skeletons_each * bones_per_child

    # L8
    total_bones_graveyard = total_bones_children + total_bones_men + total_bones_women

    # FA
    answer = total_bones_graveyard
    return answer
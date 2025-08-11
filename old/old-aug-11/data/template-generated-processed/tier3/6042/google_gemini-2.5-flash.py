def solve():
    """Index: 6042.
    Returns: the total number of craft supply items Allison bought.
    """
    # L1
    more_glue_sticks_allison = 8 # Allison bought 8 more glue sticks than Marie
    marie_glue_sticks = 15 # Marie bought 15 glue sticks
    allison_glue_sticks = more_glue_sticks_allison + marie_glue_sticks

    # L2
    marie_construction_paper = 30 # 30 packs of construction paper
    marie_times_more_paper = 6 # Marie bought six times as many packs of construction paper as Allison
    allison_construction_paper = marie_construction_paper / marie_times_more_paper

    # L3
    total_allison_items = allison_glue_sticks + allison_construction_paper

    # FA
    answer = total_allison_items
    return answer
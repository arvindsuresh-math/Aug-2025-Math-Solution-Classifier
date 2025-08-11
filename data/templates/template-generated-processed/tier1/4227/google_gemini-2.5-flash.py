def solve():
    """Index: 4227.
    Returns: the total number of metal rods needed for the fence.
    """
    # L1
    sheets_per_panel = 3 # 3 metal sheets
    rods_per_sheet = 10 # 10 metal rods
    rods_from_sheets_per_panel = sheets_per_panel * rods_per_sheet

    # L2
    beams_per_panel = 2 # 2 metal beams
    rods_per_beam = 4 # 4 metal rods
    rods_from_beams_per_panel = beams_per_panel * rods_per_beam

    # L3
    total_rods_per_panel = rods_from_sheets_per_panel + rods_from_beams_per_panel

    # L4
    num_fence_panels = 10 # 10 fence panels
    total_rods_for_fence = total_rods_per_panel * num_fence_panels

    # FA
    answer = total_rods_for_fence
    return answer
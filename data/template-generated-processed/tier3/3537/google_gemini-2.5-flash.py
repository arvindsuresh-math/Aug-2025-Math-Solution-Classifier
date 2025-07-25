def solve():
    """Index: 3537.
    Returns: the total yards of material required to make the target number of quilts.
    """
    # L1
    total_material_initial = 21 # 21 yards of material
    num_quilts_initial = 7 # 7 quilts
    material_per_quilt = total_material_initial / num_quilts_initial

    # L2
    num_quilts_target = 12 # 12 quilts
    total_material_required = num_quilts_target * material_per_quilt

    # FA
    answer = total_material_required
    return answer
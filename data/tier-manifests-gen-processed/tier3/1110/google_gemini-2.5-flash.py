def solve():
    """Index: 1110.
    Returns: the amount of medicine in each part of the dose in ml.
    """
    # L1
    child_weight = 30 # child weighs 30 kilograms
    medicine_per_kg = 5 # 5 ml of medicine
    total_medicine_ml = child_weight * medicine_per_kg

    # L2
    num_parts = 3 # given in 3 equal parts
    medicine_per_part_ml = total_medicine_ml / num_parts

    # FA
    answer = medicine_per_part_ml
    return answer
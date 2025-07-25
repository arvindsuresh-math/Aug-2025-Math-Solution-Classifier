def solve():
    """Index: 3907.
    Returns: the number of feet of the field that will not be fenced.
    """
    # L1
    total_money = 120000 # she had $120000
    cost_per_foot = 30 # one foot of wire mesh is sold at $30
    feet_of_wire_mesh_bought = total_money / cost_per_foot

    # L2
    field_length = 5000 # fence a 5000 feet square field
    unfenced_length = field_length - feet_of_wire_mesh_bought

    # FA
    answer = unfenced_length
    return answer
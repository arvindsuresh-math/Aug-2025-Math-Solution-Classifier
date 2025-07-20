def solve():
    """Index: 6529.
    Returns: the number of additional boxes of flooring Tom needs.
    """
    # L1
    length = 16 # 16' long
    width = 20 # 20' wide
    total_room_sq_ft = length * width

    # L2
    already_put_down = 250 # he has already put down 250 sq ft of flooring
    remaining_sq_ft = total_room_sq_ft - already_put_down

    # L3
    sq_ft_per_box = 10 # 10 sq ft per box
    boxes_needed = remaining_sq_ft / sq_ft_per_box

    # FA
    answer = boxes_needed
    return answer
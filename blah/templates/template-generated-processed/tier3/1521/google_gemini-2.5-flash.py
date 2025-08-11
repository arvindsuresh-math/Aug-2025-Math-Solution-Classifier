from fractions import Fraction

def solve():
    """Index: 1521.
    Returns: the total amount Selene pays.
    """
    # L1
    num_instant_cameras = 2 # two instant cameras
    cost_per_instant_camera = 110 # at $110
    cost_instant_cameras = num_instant_cameras * cost_per_instant_camera

    # L2
    num_photo_frames = 3 # three digital photo frames
    cost_per_photo_frame = 120 # at $120 each
    cost_photo_frames = num_photo_frames * cost_per_photo_frame

    # L3
    subtotal_cost = cost_instant_cameras + cost_photo_frames

    # L4
    discount_percentage = Fraction(5, 100) # 5% discount
    discount_amount = discount_percentage * subtotal_cost

    # L5
    final_cost = subtotal_cost - discount_amount

    # FA
    answer = final_cost
    return answer
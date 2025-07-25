def solve():
    """Index: 3046.
    Returns: the total number of m&m packs Kekai uses.
    """
    # L1
    sundaes_monday = 40 # 40 sundaes
    mms_per_sundae_monday = 6 # 6 m&ms on each sundae
    mms_monday = sundaes_monday * mms_per_sundae_monday

    # L2
    sundaes_tuesday = 20 # 20 sundaes
    mms_per_sundae_tuesday = 10 # 10 m&ms on each sundae
    mms_tuesday = sundaes_tuesday * mms_per_sundae_tuesday

    # L3
    total_mms_used = mms_monday + mms_tuesday

    # L4
    mms_per_pack = 40 # each m&m pack contains 40 m&ms
    total_mms_packs = total_mms_used / mms_per_pack

    # FA
    answer = total_mms_packs
    return answer
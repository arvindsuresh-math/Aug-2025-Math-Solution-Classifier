def solve(
    laurie_shells: int = 36,  # Laurie collected 36 shells
    ben_shell_fraction: float = 1/3,  # Ben collected a third of what Laurie did
    alan_shell_multiplier: int = 4  # Alan collected four times as many shells as Ben
):
    """Index: 49.
    Returns: the number of shells Alan collected."""

    #: L1
    ben_shells = laurie_shells * ben_shell_fraction # eval: 12.0 = 36 * 0.3333333333333333

    #: L2
    alan_shells = ben_shells * alan_shell_multiplier # eval: 48.0 = 12.0 * 4

    #: FA
    answer = alan_shells
    return answer # eval: return 48.0

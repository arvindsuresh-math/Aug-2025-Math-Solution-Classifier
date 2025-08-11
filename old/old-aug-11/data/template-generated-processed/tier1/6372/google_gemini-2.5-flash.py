def solve():
    """Index: 6372.
    Returns: the total time Mary spent downloading Zoom and talking.
    """
    # L1
    mac_download_time = 10 # 10 minutes downloading the Mac version
    windows_download_multiplier = 3 # three times as long to download
    windows_download_time = mac_download_time * windows_download_multiplier

    # L2
    audio_glitch_duration = 4 # 4 minutes each time
    num_audio_glitches = 2 # twice for 4 minutes each time
    total_audio_glitch_time = audio_glitch_duration * num_audio_glitches

    # L3
    video_glitch_duration = 6 # video glitched once for 6 minutes
    total_glitch_time = total_audio_glitch_time + video_glitch_duration

    # L4
    glitch_free_multiplier = 2 # twice as long talking without glitches as with glitches
    total_glitch_free_time = total_glitch_time * glitch_free_multiplier

    # L5
    total_time_spent = windows_download_time + mac_download_time + total_glitch_time + total_glitch_free_time

    # FA
    answer = total_time_spent
    return answer
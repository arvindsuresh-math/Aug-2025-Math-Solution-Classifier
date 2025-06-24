def solve_0():
  """
  Calculates the total number of clips Natalia sold in April and May.

  Natalia sold clips to 48 friends in April.
  She sold half as many clips in May.
  """
  clips_april = 48
  
  # Calculate clips sold in May (half of April's sales)
  clips_may = clips_april / 2
  
  # Calculate total clips sold
  total_clips = clips_april + clips_may
  
  return int(total_clips)
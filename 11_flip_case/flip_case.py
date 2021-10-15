def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lowered_to_swap = to_swap.lower()
    new_phrase = ''
    for char in phrase:
      if char.lower() == lowered_to_swap:
        char = char.swapcase()
      new_phrase += char
    return new_phrase
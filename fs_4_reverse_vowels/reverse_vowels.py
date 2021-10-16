def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set('aeiou')
    string = list(s)
    starting = 0
    ending = len(s) - 1

    while starting < ending:
      if string[starting].lower() not in vowels:
        starting += 1
      elif string[ending].lower() not in vowels:
        ending -= 1
      else:
        string[starting], string[ending] = string[ending], string[starting]
        starting += 1
        ending -= 1

    return ''.join(string)
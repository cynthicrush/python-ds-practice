def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    new_dict = {}
    for num in nums:
        new_dict[num] = new_dict.get(num, 0) + 1

    max_value = max(new_dict.values())

    for(k, v) in new_dict.items():
      if v == max_value:
        return k

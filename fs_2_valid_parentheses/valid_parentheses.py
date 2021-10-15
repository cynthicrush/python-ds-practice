def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    parens_list = list(parens)
    if parens_list[0] != '(':
      return False
    elif parens_list.count('(') == parens_list.count(')'):
      return True
    return False
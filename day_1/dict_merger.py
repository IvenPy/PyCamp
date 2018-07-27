"""
Module provide merging 2 dicts

Example:
    dict_1 = {1: 2, 3: 4}
    dict_2 = {3: 5, 5: 6}

    merge_dicts(dict_1, dict_2) == {1: 2, 3: 5, 5: 6}

Pretty easy, right?
"""

def merge_dicts(dict_1, dict_2):
    """
    Updates 2 dicts, if intersection occurs
    keys will be updated to dict_2's values

    Args:
        dict_1:
        dict_2:

    Returns:
        dict: merged dict

    """
    intersect = set(dict_1) & set(dict_2)
    for x in intersect:
        print("Key {} updated from - {} to - {}"
              .format(x, dict_1[x], dict_2[x]))
    if not intersect:
        print("Keys updated successfully, no intersection")

    dict_1.update(dict_2)
    return dict_1


if __name__ == '__main__':
    print(merge_dicts({1: 2, 2: 3}, {1: 4, 5: 6}))

def compare_lists(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for item in lst1:
        if lst1.count(item) != lst2.count(item):
            return False
    return True

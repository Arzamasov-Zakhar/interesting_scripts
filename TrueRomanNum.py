def true_roman_num(romannum: str) -> bool:
    check_list = ["IIII", "VVVV", "XXXX", "LLLL", "CCCC", "DDDD", "MMMM"]
    for isinst in check_list:
        if isinst in romannum:
            return False
    for index, let in enumerate(romannum):
        if let == "I":
            for i in ["IV", "VV", "X", "L", "C", "D", "M"]:
                if i in romannum[index + 1:]:
                    return False
        elif let == "V":
            for i in ["VX", "XX", "L", "C", "D", "M"]:
                if i in romannum[index + 1:]:
                    return False
        elif let == "X":
            for i in ["XL", "LL", "C", "D", "M"]:
                if i in romannum[index + 1:]:
                    return False
        elif let == "L":
            for i in ["LC", "CC", "D", "M"]:
                if i in romannum[index + 1:]:
                    return False
        elif let == "C":
            for i in ["CD", "DD", "M"]:
                if i in romannum[index + 1:]:
                    return False
        elif let == "D":
            for i in ["DM", "MM"]:
                if i in romannum[index + 1:]:
                    return False
    return True


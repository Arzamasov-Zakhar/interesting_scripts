from TrueRomanNum import true_roman_num

def translator(romannum: str) -> [int, str]:
    """Калькулятор перевода из римских чисел в арабские в десятичной СИ"""
    try:
        if type(romannum) is not str:
            raise TypeError
        if not true_roman_num(romannum):
            raise ValueError
        single_translator: dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        subtractively: dict = {"II": 2, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        number: int = 0
        flag: bool = True

        for index in range(len(romannum) - 1):
            if flag:
                if romannum[index] == "I":
                    number += subtractively[romannum[index] + romannum[index + 1]]
                    flag = False

                elif (romannum[index] == "X" and romannum[index + 1] == "L") or \
                        (romannum[index] == "X" and romannum[index + 1] == "C") or \
                        (romannum[index] == "C" and romannum[index + 1] == "D") or \
                        (romannum[index] == "C" and romannum[index + 1] == "M"):
                    number += subtractively[romannum[index] + romannum[index + 1]]
                    flag = False

                else:
                    number += single_translator[romannum[index]]
            else:
                flag = True
        if flag:
            number += 1

        return number
    except (KeyError, TypeError):
        return "Введите число, записанное римскими цифрами в формате 'MDCLXVI' "
    except ValueError:
        return """Проверьте правильность написания римских чисел: необходимо сначала 
записать число тысяч, затем сотен, затем десятков и, наконец, единиц"""







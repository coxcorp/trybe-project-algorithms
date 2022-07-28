def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_list = list(first_string.upper())
    second_list = list(second_string.upper())
    letter_qtd = 0
    for letter in first_list:
        if letter in second_list:
            letter_qtd += 1
            second_list.remove(letter)
        else:
            return False
    if letter_qtd == len(first_list):
        return True
    return False

def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif low_index > high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

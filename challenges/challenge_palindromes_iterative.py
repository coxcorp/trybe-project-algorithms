def is_palindrome_iterative(word):
    if not word:
        return False
    lista = list(word)
    invertida = lista.copy()
    invertida.reverse()
    return lista == invertida

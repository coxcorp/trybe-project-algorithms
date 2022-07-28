def is_palindrome_iterative(word):
    if word:
        lista = list(word)
        invertida = lista.copy()
        invertida.reverse()
        return lista == invertida
    return False

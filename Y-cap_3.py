# Дана строка, Определить, можно ли перестановкой символо сделать из нее палиндром

# шалаш
# аbbcbba
# eeeqqee

def is_palindrom(string):
    char_count = {}

    for char in string:
        if char in string:
            char_count[char] += 1
        else:
            char_count[char] = 1

    nechet_count = 0

    for count in char_count.values():
        if count % 2 == 1:
            nechet_count += 1

    if nechet_count <= 1:
        return True
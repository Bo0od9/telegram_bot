def get_dict():  # создаем словарь используемых символов
    d = [' ', '.', ',', '?' '!', ':', ';']
    i = 0
    for i in range(48, 58):
        d.append(chr(i))
    for i in range(65, 91):
        d.append(chr(i))
    for i in range(97, 123):
        d.append(chr(i))
    return ''.join(d)


def caesar_encode(shift, text):
    alpha = get_dict()
    n = shift
    s = text.strip()
    res = ''
    for c in s:
        res += alpha[(alpha.index(c) + n) % len(alpha)]
    return res


def caesar_decode(shift, text):
    alpha = get_dict()
    n = shift * -1
    s = text.strip()
    res = ''
    for c in s:
        res += alpha[(alpha.index(c) + n) % len(alpha)]
    return res

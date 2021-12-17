def get_dict():
    '''
    Создает словарь используемых символов.
    '''
    d = [' ', '.', ',', '?' '!', ':', ';']
    i = 0
    for i in range(48, 58):
        d.append(chr(i))
    for i in range(65, 91):
        d.append(chr(i))
    for i in range(97, 123):
        d.append(chr(i))
    return ''.join(d)


def caesar_encode(text, shift):
    '''
    Зашифровывает текст.
    '''
    dictionary = get_dict()
    user_text = text.strip()
    res = ''
    for c in user_text:
        res += dictionary[(dictionary.index(c) + shift) % len(dictionary)]
    return res


def caesar_decode(text, shift):
    '''
    Расшифровывает текст.
    '''
    dictionary = get_dict()
    shift = shift * -1
    user_text = text.strip()
    res = ''
    for c in user_text:
        res += dictionary[(dictionary.index(c) + shift) % len(dictionary)]
    return res

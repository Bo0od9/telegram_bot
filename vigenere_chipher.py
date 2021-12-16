def main(user_text, user_key):
    def get_dict():  # создаем словарь используемых символов
        d = [' ', '.', ',', '?' '!', ':', ';']
        i = 0
        for i in range(48, 58):
            d.append(chr(i))
        for i in range(65, 91):
            d.append(chr(i))
        for i in range(97, 123):
            d.append(chr(i))
        return d

    def char_to_index(word):  # сопоставляем буква заданного слова их номера в используемом словаре
        list_code = []
        d = get_dict()
        for i in range(len(word)):
            for j in range(len(d)):
                if word[i] == d[j]:
                    list_code.append(j)
        return list_code

    def form_gamma_by_userkey(text, key):  # формируем гамму на основе ключа
        key_code = char_to_index(key)
        text_code = char_to_index(text)
        gamma = key_code
        iterr = 2
        while len(gamma) < len(text_code):
            gamma = gamma * iterr
            iterr += 1
        while len(gamma) > len(text_code):
            gamma.pop()
        return gamma

    def encode(text, gamma):  # накладываем гамму на исходный текст
        text_code = char_to_index(text)
        crypt_code = []
        mod = len(get_dict())
        for i in range(len(text_code)):
            crypt_code.append((gamma[i] + text_code[i]) % mod)
        return crypt_code

    def index_to_char(word):  # переводим номер символа в словаре в символ
        d = get_dict()
        list_char = []
        for i in range(len(word)):
            list_char.append(d[word[i]])
        return list_char

    def decode(text, gamma):  # расшифровывает полученную строку, убирает гамму
        mod = len(get_dict())
        text_code = char_to_index(text)
        decrypt_text = []
        for i in range(len(text)):
            decrypt_text.append((text_code[i] - gamma[i] + mod) % mod)
        return decrypt_text

    user_text = user_text
    user_key = user_key
    gamma = form_gamma_by_userkey(user_text, user_key)
    gamma_plus_usertext = encode(user_text, gamma)
    return 'Шифр текст:', ''.join(index_to_char(gamma_plus_usertext))

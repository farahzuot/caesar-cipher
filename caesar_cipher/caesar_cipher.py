import nltk 
nltk.download('words')
english_words = nltk.corpus.words.words()


def count_words(sentence):
    '''
    >>> count_words('sentence three two hi')
    4
    '''
    words_list = sentence.split()
    counter = 0
    for i in words_list:
        if i in english_words or i.lower() in english_words or i.upper() in english_words:
            counter+=1

    return counter

def encrypt(text,num):
    '''
    input: plain text phrase and a numeric shift
    output: the phrase will be shifted that many letters.
    >>> encrypt('abCd',29)
    defg
    '''
    try:
        new_text=''
        if num > 26:
            num = num%26
        for i in text.lower():
            if ord(i) == 32:
                new_text+=i
                continue
            if ord(i) > 32 and ord(i) < 65:
                continue
            new = ord(i)+num
            new_text+=chr(new)
        return new_text
    except AttributeError:
        return 'invalid input'


def decrypt(sec_text,de_num):
    '''
    input: plain text phrase and a numeric shift
    output: the phrase will be shifted to it's original state.
    >>> decrypt('defg',29)
    abcd
    '''
    try:
        if de_num > 26:
            de_num = de_num%26
        return encrypt(sec_text,-de_num)
    except AttributeError:
        return 'invalid input'


def hack(text):
    '''
    input: plain text
    output: original state of the meaningful words.
    >>> hack('ifmmp xpsme')
    hello world
    '''
    textTwo=''
    new_text=text.split()
    # print(new_text)
    arr =[]
    for i in new_text:
        for j in range(26):
            encrypted = encrypt(i,j)
            decrypted = decrypt(i,j)
            # print(decrypted)
            if encrypted in english_words:
                arr.append(encrypted)
            if decrypted in english_words:
                arr.append(decrypted)
    for i in arr:
        textTwo+=i+' '
    return textTwo.strip()
    



if __name__ == "__main__":

    print(encrypt('hello,,,',7))
    # print(encrypt('z',1))
    print(hack('olssv'))
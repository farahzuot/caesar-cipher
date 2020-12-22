from caesar_cipher.caesar_cipher import encrypt,decrypt,hack


def test_ecrypt():
    '''
    encrypt a string with a given shift
    '''
    actual = encrypt('abcd',29)
    expected = 'defg'
    assert actual == expected

def test_decrypt():
    '''
    decrypt a previously encrypted string with the same shift
    '''
    actual = decrypt('defg',29)
    expected = 'abcd'
    assert actual == expected

def test_encrypt_upper_lower():
    '''
    encryption should handle upper and lower case letters
    '''
    actual = encrypt('aBCd',29)
    expected = 'defg'
    assert actual == expected

def test_encrypt_white_space():
    '''
    encryption should allow non-alpha characters but ignore them, including white space
    '''
    actual = encrypt('aBCd abcd',29)
    expected = 'defg defg'
    assert actual == expected

def test_encrypt_special_char_hack():
    '''
    decrypt encrypted WITHOUT knowing the shift used.
    '''
    encrypted = encrypt('hello,,,',7)
    actual = hack(encrypted)
    expected = 'hello'
    assert actual == expected


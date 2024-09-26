import string


def run_length_encoding(s):
    if not s:
        return ''
    elif len(s) == 1:
        return '1' + s

    encoded_string = ''

    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        next_char = s[i]

        if current_char == next_char:
            count += 1
        else:
            encoded_string += str(count) + current_char
            current_char = next_char
            count = 1

    encoded_string += str(count) + current_char

    return encoded_string


def run_length_decoding(s):
    if not s:
        return ''

    decoded_string = ''

    last_decoded_index = 0

    for i in range(len(s)):
        if s[i] in string.ascii_lowercase or s[i] in string.ascii_uppercase:
            decoded_string += int(s[last_decoded_index:i]) * s[i]

            last_decoded_index = i + 1

    return decoded_string


if __name__ == '__main__':
     print(run_length_encoding(''))
     print(run_length_encoding(None))
     print(run_length_encoding('abcd'))
     print(run_length_encoding('aaaaabbbccda'))
     print(run_length_encoding('aabcc'))
     print(run_length_encoding('aaaaaaaaaaaaaaaaaaaa'))
     print(run_length_encoding('ABCD'))

     print(run_length_decoding(''))
     print(run_length_decoding(None))
     print(run_length_decoding('1a1b1c1d'))
     print(run_length_decoding('5a3b2c1d1a'))
     print(run_length_decoding('2a1b2c'))
     print(run_length_decoding('20a'))
     print(run_length_decoding('1A1B1C1D'))
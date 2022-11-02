card_pub_key = 15335876
door_pub_key = 15086442


def find_loop_size(subject_num, pub_key):
    value = 1
    loops = 0

    while value != pub_key:
        value *= subject_num
        value %= 20201227
        loops += 1

    return loops


def find_enc_key(pub_key, loop_size):
    value = 1

    for i in range(loop_size):
        value *= pub_key
        value %= 20201227

    return value


card_loop_size = find_loop_size(7, card_pub_key)
door_loop_size = find_loop_size(7, door_pub_key)

print(find_enc_key(door_pub_key, card_loop_size))
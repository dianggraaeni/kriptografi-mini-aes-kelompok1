# utils.py

def s_box(state):
    box = [0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5,
           0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7]
    return [box[nibble] for nibble in state]

def inverse_s_box(state):
    inv_box = [0xA, 0x5, 0x9, 0xB, 0x1, 0x7, 0x8, 0xF,
               0x6, 0x0, 0x2, 0x3, 0xC, 0x4, 0xD, 0xE]
    return [inv_box[nibble] for nibble in state]

def shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def inverse_shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def mix_columns(state):
    return [state[0] ^ state[2], state[1] ^ state[3],
            state[2] ^ state[0], state[3] ^ state[1]]

def inverse_mix_columns(state):
    return [state[0] ^ state[2], state[1] ^ state[3],
            state[2] ^ state[0], state[3] ^ state[1]]

def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

def key_expansion(key):
    # Key: 4 nibble (16 bit) input
    w = [0] * 12
    w[0:4] = key

    for i in range(4, 12, 4):
        temp = s_box([w[i - 1]])[0]
        w[i]     = w[i - 4] ^ temp ^ 0x1  # round constant sederhana
        w[i + 1] = w[i - 3] ^ w[i]
        w[i + 2] = w[i - 2] ^ w[i + 1]
        w[i + 3] = w[i - 1] ^ w[i + 2]

    return [w[0:4], w[4:8], w[8:12], w[8:12]]  # Final round pakai kunci terakhir ulang

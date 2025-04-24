# utils.py
# Fungsi pembantu Mini-AES

def s_box(state):
    box = [0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5, 0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7]
    return [box[nibble] for nibble in state]

def inverse_s_box(state):
    inv_box = [0xA, 0x5, 0x9, 0xB, 0x1, 0x7, 0x8, 0xF, 0x6, 0x0, 0x2, 0x3, 0xC, 0x4, 0xD, 0xE]
    return [inv_box[nibble] for nibble in state]

def shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def inverse_shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def mix_columns(state):
    return [state[0] ^ state[2], state[1] ^ state[3], state[2] ^ state[0], state[3] ^ state[1]]

def inverse_mix_columns(state):
    return [state[0] ^ state[2], state[1] ^ state[3], state[2] ^ state[0], state[3] ^ state[1]]

def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

def key_expansion(key):
    return [key, [k ^ 0x1 for k in key], [k ^ 0x2 for k in key], [k ^ 0x3 for k in key]]
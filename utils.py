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
    # Swap second row: [s0 s1]     -> [s0 s1]
    #                   [s2 s3]    -> [s3 s2]
    return [state[0], state[1], state[3], state[2]]

def inverse_shift_rows(state):
    # Same as shift_rows because it's its own inverse
    return [state[0], state[1], state[3], state[2]]

def mix_columns(state):
    # Reversible mix column transformation
    # Based on simple reversible XOR + move scheme
    return [
        state[0] ^ state[2],  # s0' = s0 ^ s2
        state[1] ^ state[3],  # s1' = s1 ^ s3
        state[0],             # s2' = s0
        state[1],             # s3' = s1
    ]

def inverse_mix_columns(state):
    # Inverse of the above mix_columns
    return [
        state[2],             # s0 = s2'
        state[3],             # s1 = s3'
        state[0] ^ state[2],  # s2 = s0' ^ s2'
        state[1] ^ state[3],  # s3 = s1' ^ s3'
    ]

def add_round_key(state, key):
    return [s ^ k for s, k in zip(state, key)]

def key_expansion(key):
    # Expand 16-bit key into 3 round keys (4 nibbles each)
    w = [0] * 12
    w[0:4] = key

    for i in range(4, 12, 4):
        temp = s_box([w[i - 1]])[0]
        w[i]     = w[i - 4] ^ temp ^ 0x1  # simple round constant
        w[i + 1] = w[i - 3] ^ w[i]
        w[i + 2] = w[i - 2] ^ w[i + 1]
        w[i + 3] = w[i - 1] ^ w[i + 2]

    return [w[0:4], w[4:8], w[8:12], w[8:12]]  # last round reuses last key

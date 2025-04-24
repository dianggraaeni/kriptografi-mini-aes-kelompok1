# mini_aes.py
from utils import (
    s_box, inverse_s_box,
    shift_rows, inverse_shift_rows,
    mix_columns, inverse_mix_columns,
    add_round_key, key_expansion
)

class MiniAES:
    def __init__(self, key):
        self.round_keys = key_expansion(key)

    def encrypt(self, plaintext):
        state = add_round_key(plaintext, self.round_keys[0])

        for i in range(1, 3):
            state = s_box(state)
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_key(state, self.round_keys[i])

        state = s_box(state)
        state = shift_rows(state)
        state = add_round_key(state, self.round_keys[3])
        return state

    def decrypt(self, ciphertext):
        state = add_round_key(ciphertext, self.round_keys[3])
        state = inverse_shift_rows(state)
        state = inverse_s_box(state)

        for i in range(2, 0, -1):
            state = add_round_key(state, self.round_keys[i])
            state = inverse_mix_columns(state)
            state = inverse_shift_rows(state)
            state = inverse_s_box(state)

        state = add_round_key(state, self.round_keys[0])
        return state

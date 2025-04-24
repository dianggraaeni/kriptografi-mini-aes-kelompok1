# mini_aes.py
# Implementasi Mini-AES 16-bit

from utils import (
    s_box, inverse_s_box,
    shift_rows, inverse_shift_rows,
    mix_columns, inverse_mix_columns,
    add_round_key, key_expansion
)

class MiniAES:
    def __init__(self, key):
        self.round_keys = key_expansion(key)  # key expansion menghasilkan 4 round keys untuk 3 ronde + 1 akhir

    def encrypt(self, plaintext):
        state = add_round_key(plaintext, self.round_keys[0])  # Initial round

        # 2 round utama (karena total round = 3, final round tanpa MixColumns)
        for i in range(1, 3):
            state = s_box(state)
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_key(state, self.round_keys[i])

        # Final round
        state = s_box(state)
        state = shift_rows(state)
        state = add_round_key(state, self.round_keys[3])
        return state

    def decrypt(self, ciphertext):
        state = add_round_key(ciphertext, self.round_keys[3])  # Initial step untuk dekripsi (kunci terakhir)
        state = inverse_shift_rows(state)
        state = inverse_s_box(state)

        # 2 round utama (urutan terbalik dari enkripsi)
        for i in range(2, 0, -1):
            state = add_round_key(state, self.round_keys[i])
            state = inverse_mix_columns(state)
            state = inverse_shift_rows(state)
            state = inverse_s_box(state)

        # Final add round key
        state = add_round_key(state, self.round_keys[0])
        return state

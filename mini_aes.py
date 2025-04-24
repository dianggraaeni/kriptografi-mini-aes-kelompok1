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

    def encrypt(self, plaintext, show_rounds=False):
        state = add_round_key(plaintext, self.round_keys[0])
        
        if show_rounds:
            print(f"Setelah AddRoundKey (Ronde 0): {[f'{x:02x}' for x in state]}")

        for i in range(1, 3):
            state = s_box(state)
            if show_rounds:
                print(f"Setelah SubNibbles (Ronde {i}): {[f'{x:02x}' for x in state]}")
                
            state = shift_rows(state)
            if show_rounds:
                print(f"Setelah ShiftRows (Ronde {i}): {[f'{x:02x}' for x in state]}")
                
            state = mix_columns(state)
            if show_rounds:
                print(f"Setelah MixColumns (Ronde {i}): {[f'{x:02x}' for x in state]}")
                
            state = add_round_key(state, self.round_keys[i])
            if show_rounds:
                print(f"Setelah AddRoundKey (Ronde {i}): {[f'{x:02x}' for x in state]}")

        state = s_box(state)
        if show_rounds:
            print(f"Setelah SubNibbles (Ronde final): {[f'{x:02x}' for x in state]}")
            
        state = shift_rows(state)
        if show_rounds:
            print(f"Setelah ShiftRows (Ronde final): {[f'{x:02x}' for x in state]}")
            
        state = add_round_key(state, self.round_keys[3])
        if show_rounds:
            print(f"Setelah AddRoundKey (Ronde final): {[f'{x:02x}' for x in state]}")
            
        return state

    def decrypt(self, ciphertext, show_rounds=False):
        state = add_round_key(ciphertext, self.round_keys[3])
        if show_rounds:
            print(f"Setelah AddRoundKey (Ronde final): {[f'{x:02x}' for x in state]}")
            
        state = inverse_shift_rows(state)
        if show_rounds:
            print(f"Setelah InverseShiftRows (Ronde final): {[f'{x:02x}' for x in state]}")
            
        state = inverse_s_box(state)
        if show_rounds:
            print(f"Setelah InverseSubNibbles (Ronde final): {[f'{x:02x}' for x in state]}")

        for i in range(2, 0, -1):
            state = add_round_key(state, self.round_keys[i])
            if show_rounds:
                print(f"Setelah AddRoundKey (Ronde {i}): {[f'{x:02x}' for x in state]}")
                
            state = inverse_mix_columns(state)
            if show_rounds:
                print(f"Setelah InverseMixColumns (Ronde {i}): {[f'{x:02x}' for x in state]}")
                
            state = inverse_shift_rows(state)
            if show_rounds:
                print(f"Setelah InverseShiftRows (Ronde {i}): {[f'{x:02x}' for x in state]}")
                
            state = inverse_s_box(state)
            if show_rounds:
                print(f"Setelah InverseSubNibbles (Ronde {i}): {[f'{x:02x}' for x in state]}")

        state = add_round_key(state, self.round_keys[0])
        if show_rounds:
            print(f"Setelah AddRoundKey (Ronde 0): {[f'{x:02x}' for x in state]}")
            
        return state
        
    def ecb_encrypt(self, plaintext_blocks, show_rounds=False):
        """
        Electronic Codebook mode encryption
        """
        return [self.encrypt(block, show_rounds) for block in plaintext_blocks]
    
    def ecb_decrypt(self, ciphertext_blocks, show_rounds=False):
        """
        Electronic Codebook mode decryption
        """
        return [self.decrypt(block, show_rounds) for block in ciphertext_blocks]
    
    def cbc_encrypt(self, plaintext_blocks, iv, show_rounds=False):
        """
        Cipher Block Chaining mode encryption
        """
        result = []
        previous = iv
        for block in plaintext_blocks:
            xored = [p ^ c for p, c in zip(block, previous)]
            encrypted = self.encrypt(xored, show_rounds)
            result.append(encrypted)
            previous = encrypted
        return result
    
    def cbc_decrypt(self, ciphertext_blocks, iv, show_rounds=False):
        """
        Cipher Block Chaining mode decryption
        """
        result = []
        previous = iv
        for block in ciphertext_blocks:
            decrypted = self.decrypt(block, show_rounds)
            plaintext = [d ^ p for d, p in zip(decrypted, previous)]
            result.append(plaintext)
            previous = block
        return result
        
    def split_into_blocks(self, data):
        """
        Split data into 16-bit blocks (4 nibbles each)
        """
        blocks = []
        for i in range(0, len(data), 4):
            block = data[i:i+4]
            # Pad the last block if needed
            if len(block) < 4:
                block = block + [0] * (4 - len(block))
            blocks.append(block)
        return blocks
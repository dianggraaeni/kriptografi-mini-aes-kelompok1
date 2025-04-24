# avalanche_analysis.py
from mini_aes import MiniAES

def avalanche_effect():
    key = [0x1, 0x2, 0x3, 0x4]
    base_plain = [0x1, 0x2, 0x3, 0x4]
    aes = MiniAES(key)
    base_cipher = aes.encrypt(base_plain)
    print("Base Cipher:", [f"{x:02x}" for x in base_cipher])
    
    for i in range(4):  # Ubah tiap byte di plaintext
        for b in range(8):  # Ubah setiap bit
            modified = base_plain[:]
            modified[i] ^= (1 << b)
            modified_cipher = aes.encrypt(modified)
            diff = sum([bin(a ^ b).count('1') for a, b in zip(base_cipher, modified_cipher)])
            mod_str = [f"{x:02x}" for x in modified]
            cipher_str = [f"{x:02x}" for x in modified_cipher]
            print(f"Modified bit [{i},{b}] ({mod_str}) -> Cipher: {cipher_str}, Difference: {diff} bits")

if __name__ == '__main__':
    avalanche_effect()

# avalanche_analysis.py
from mini_aes import MiniAES

def avalanche_effect():
    key = [0x1, 0x2, 0x3, 0x4]
    base_plain = [0x1, 0x2, 0x3, 0x4]
    aes = MiniAES(key)
    base_cipher = aes.encrypt(base_plain)
    print("Base Cipher:", [f"{x:02x}" for x in base_cipher])
    
    total_bit_changes = 0
    total_tests = 0
    
    print("\n=== PENGUJIAN EFEK AVALANCHE ===")
    print("Mengukur perubahan bit di ciphertext ketika 1 bit di plaintext diubah\n")
    
    for i in range(4):  # Ubah tiap byte di plaintext
        for b in range(4):  # Ubah setiap bit (nibble hanya 4 bit)
            modified = base_plain[:]
            modified[i] ^= (1 << b)
            modified_cipher = aes.encrypt(modified)
            
            # Hitung jumlah bit yang berbeda
            diff = 0
            for a, b in zip(base_cipher, modified_cipher):
                xor_result = a ^ b
                diff += bin(xor_result).count('1')
            
            total_bit_changes += diff
            total_tests += 1
            
            percentage = (diff / 16) * 100  # 16 bit total di ciphertext
            
            mod_str = [f"{x:01x}" for x in modified]
            cipher_str = [f"{x:01x}" for x in modified_cipher]
            print(f"Ubah bit [{i},{b}] ({mod_str}) -> Cipher: {cipher_str}, Perbedaan: {diff} bits ({percentage:.1f}%)")
    
    avg_percentage = (total_bit_changes / (total_tests * 16)) * 100
    print(f"\nRata-rata perubahan: {avg_percentage:.2f}% dari total bit")
    print(f"Total pengujian: {total_tests} perubahan bit")

def key_avalanche_effect():
    base_key = [0x1, 0x2, 0x3, 0x4]
    plaintext = [0x5, 0x6, 0x7, 0x8]
    
    aes = MiniAES(base_key)
    base_cipher = aes.encrypt(plaintext)
    print("Base Cipher dengan Key Awal:", [f"{x:02x}" for x in base_cipher])
    
    total_bit_changes = 0
    total_tests = 0
    
    print("\n=== PENGUJIAN EFEK AVALANCHE PADA KEY ===")
    print("Mengukur perubahan bit di ciphertext ketika 1 bit di key diubah\n")
    
    for i in range(4):  # Ubah tiap byte di key
        for b in range(4):  # Ubah setiap bit (nibble hanya 4 bit)
            modified_key = base_key[:]
            modified_key[i] ^= (1 << b)
            
            aes_modified = MiniAES(modified_key)
            modified_cipher = aes_modified.encrypt(plaintext)
            
            # Hitung jumlah bit yang berbeda
            diff = 0
            for a, b in zip(base_cipher, modified_cipher):
                xor_result = a ^ b
                diff += bin(xor_result).count('1')
            
            total_bit_changes += diff
            total_tests += 1
            
            percentage = (diff / 16) * 100  # 16 bit total di ciphertext
            
            mod_str = [f"{x:01x}" for x in modified_key]
            cipher_str = [f"{x:01x}" for x in modified_cipher]
            print(f"Ubah bit key [{i},{b}] ({mod_str}) -> Cipher: {cipher_str}, Perbedaan: {diff} bits ({percentage:.1f}%)")
    
    avg_percentage = (total_bit_changes / (total_tests * 16)) * 100
    print(f"\nRata-rata perubahan untuk key: {avg_percentage:.2f}% dari total bit")
    print(f"Total pengujian: {total_tests} perubahan bit")

if __name__ == '__main__':
    print("=== ANALISIS EFEK AVALANCHE PADA PLAINTEXT ===")
    avalanche_effect()
    
    print("\n\n=== ANALISIS EFEK AVALANCHE PADA KEY ===")
    key_avalanche_effect()
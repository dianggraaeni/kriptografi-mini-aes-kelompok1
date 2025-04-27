# kode setelah test_cases.py

# test_cases.py
from mini_aes import MiniAES

def run_test_case(plaintext, key, expected_cipher=None, show_rounds=True):
    aes = MiniAES(key)
    print(f"\nTest Case: Plaintext={[f'{x:01x}' for x in plaintext]}, Key={[f'{x:01x}' for x in key]}")
    
    # Enkripsi
    print("\n--- ENKRIPSI ---")
    cipher = aes.encrypt(plaintext, show_rounds)
    print(f"Hasil Enkripsi: {[f'{x:01x}' for x in cipher]}")
    
    if expected_cipher:
        if cipher == expected_cipher:
            print("✓ BENAR: Hasil sesuai ekspektasi")
        else:
            print(f"✗ SALAH: Ekspektasi {[f'{x:01x}' for x in expected_cipher]}, hasil {[f'{x:01x}' for x in cipher]}")
    
    # Dekripsi
    print("\n--- DEKRIPSI ---")
    decrypted = aes.decrypt(cipher, show_rounds)
    print(f"Hasil Dekripsi: {[f'{x:01x}' for x in decrypted]}")
    
    if decrypted == plaintext:
        print("✓ BENAR: Dekripsi mengembalikan plaintext awal")
    else:
        print(f"✗ SALAH: Plaintext awal {[f'{x:01x}' for x in plaintext]}, hasil dekripsi {[f'{x:01x}' for x in decrypted]}")
    
    return cipher

def run_all_tests():
    print("=== MENJALANKAN TEST CASES MINI-AES ===")
    
    # Test Case 1: Semua nilai 0
    test1_plain = [0x0, 0x0, 0x0, 0x0]
    test1_key = [0x0, 0x0, 0x0, 0x0]
    expected1 = [0xA, 0xA, 0x9, 0x9]  # Nilai yang diharapkan (harus diubah sesuai algoritma)
    
    # Test Case 2: Nilai plaintext dan key acak
    test2_plain = [0x1, 0x2, 0x3, 0x4]
    test2_key = [0x5, 0x6, 0x7, 0x8]
    expected2 = [0xB, 0x9, 0x6, 0x4]  # Nilai yang diharapkan (harus diubah sesuai algoritma)
    
    # Test Case 3: Nilai plaintext dan key maksimum
    test3_plain = [0xF, 0xF, 0xF, 0xF]
    test3_key = [0xF, 0xF, 0xF, 0xF]
    expected3 = [0x5, 0x5, 0x7, 0x7]  # Nilai yang diharapkan (harus diubah sesuai algoritma)
    
    # Jalankan semua test case
    print("\n--- TEST CASE 1 ---")
    result1 = run_test_case(test1_plain, test1_key, expected1)
    
    print("\n--- TEST CASE 2 ---")
    result2 = run_test_case(test2_plain, test2_key, expected2)
    
    print("\n--- TEST CASE 3 ---")
    result3 = run_test_case(test3_plain, test3_key, expected3)
    
    # Ringkasan hasil
    print("\n=== RINGKASAN HASIL TEST ===")
    print(f"Test 1: Plaintext={[f'{x:01x}' for x in test1_plain]}, Key={[f'{x:01x}' for x in test1_key]}")
    print(f"       Hasil: {[f'{x:01x}' for x in result1]}")
    
    print(f"Test 2: Plaintext={[f'{x:01x}' for x in test2_plain]}, Key={[f'{x:01x}' for x in test2_key]}")
    print(f"       Hasil: {[f'{x:01x}' for x in result2]}")
    
    print(f"Test 3: Plaintext={[f'{x:01x}' for x in test3_plain]}, Key={[f'{x:01x}' for x in test3_key]}")
    print(f"       Hasil: {[f'{x:01x}' for x in result3]}")

def test_block_modes():
    print("\n=== TEST MODE OPERASI BLOK ===")
    
    # Test data
    plaintext = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]
    key = [0xA, 0xB, 0xC, 0xD]
    iv = [0x1, 0x2, 0x3, 0x4]
    
    aes = MiniAES(key)
    blocks = aes.split_into_blocks(plaintext)
    
    print(f"Plaintext: {[f'{x:01x}' for x in plaintext]}")
    print(f"Key: {[f'{x:01x}' for x in key]}")
    print(f"IV: {[f'{x:01x}' for x in iv]}")
    print(f"Plaintext Blocks: {[[f'{x:01x}' for x in block] for block in blocks]}")
    
    # Test ECB Mode
    print("\n--- ECB MODE ---")
    ecb_cipher = aes.ecb_encrypt(blocks)
    print(f"ECB Ciphertext: {[[f'{x:01x}' for x in block] for block in ecb_cipher]}")
    ecb_decrypted = aes.ecb_decrypt(ecb_cipher)
    print(f"ECB Decrypted: {[[f'{x:01x}' for x in block] for block in ecb_decrypted]}")
    
    # Test CBC Mode
    print("\n--- CBC MODE ---")
    cbc_cipher = aes.cbc_encrypt(blocks, iv)
    print(f"CBC Ciphertext: {[[f'{x:01x}' for x in block] for block in cbc_cipher]}")
    cbc_decrypted = aes.cbc_decrypt(cbc_cipher, iv)
    print(f"CBC Decrypted: {[[f'{x:01x}' for x in block] for block in cbc_decrypted]}")

if __name__ == '__main__':
    run_all_tests()
    test_block_modes()

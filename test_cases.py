# test_cases.py
from mini_aes import MiniAES

def run_tests():
    aes = MiniAES([0x1, 0x2, 0x3, 0x4])
    tests = [
        ([0x0, 0x0, 0x0, 0x0], 'Test 1'),
        ([0xF, 0xE, 0xD, 0xC], 'Test 2'),
        ([0x1, 0x2, 0x3, 0x4], 'Test 3')
    ]
    for plain, name in tests:
        encrypted = aes.encrypt(plain)
        decrypted = aes.decrypt(encrypted)
        print(f"{name}: {plain} -> {encrypted} -> {decrypted}")

if __name__ == '__main__':
    run_tests()
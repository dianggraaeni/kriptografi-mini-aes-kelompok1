# kriptografi-mini-aes-kelompok8

Anggota Kelompok
|  Nama  |  NRP  |
|--------|-------|
| Dian Anggraeni Putri | 5027231016 |
| Acintya Edria Sudarsono | 5027231020 |
| Tsaldia Hukma Cita | 5027231036 |
| Rafika Az Zahra Kusumastuti | 5027231050 |
| Nisrina Atiqah Dwiputri Ridzki | 5027231075 |

# Implementasi Mini-AES
## Deskripsi Algoritma Mini-AES
Mini-AES adalah versi sederhana dari algoritma AES (Advanced Encryption Standard), yang digunakan untuk mengenkripsi data menggunakan kunci 16-bit (4 nibble). Algoritma ini terdiri dari beberapa tahap, yaitu SubNibbles, ShiftRows, MixColumns, dan AddRoundKey, dengan tambahan fungsi dekripsi dan pengujian efek avalanche.

## Struktur Project
kriptografi-mini-aes-kelompok8/
```
├── mini_aes.py             # Implementasi algoritma Mini-AES
├── utils.py                # Fungsi-fungsi utilitas dan operasi dasar
├── gui_app.py              # Aplikasi GUI
├── test_cases.py           # Pengujian algoritma
├── avalanche_analysis.py   # Analisis efek avalanche
└── README.md               # Dokumentasi
```

## Spesifikasi Algoritma Mini-AES
Mini-AES memiliki karakteristik utama sebagai berikut
- **Ukuran Blok** : 16 bit (4 nibble).
- **Ukuran Kunci** : 16 bit (4 nibble).
- **Jumlah Ronde** : 3 ronde penuh + ronde final.
- **Representasi State** : Matriks 2x2 (diimplementasikan sebagai array linear).

### Operasi Dasar
1. **SubNibbles** : Substitusi setiap nibble (4 bit) menggunakan S-Box 4 bit.
2. **ShiftRows** : Pengacakan posisi dengan menukar posisi elemen tertentu.
3. **MixColumns** : Transformasi linear yang mencampur kolom-kolom state.
4. **AddRoundKey** : XOR state dengan round key.

## Struktur Kode
### 1. Modul `mini_aes.py`
Modul ini berisi implementasi algoritma **Mini-AES** dengan berbagai operasi dasar seperti SubNibbles, ShiftRows, MixColumns, dan AddRoundKey.

#### Fungsi Enkripsi (`encrypt`)
- **Input** : Plaintext 16 bit dan kunci 16 bit.
- **Proses**
  - Menambahkan kunci ronde pertama menggunakan AddRoundKey.
  - Melakukan 2 ronde yang terdiri dari SubNibbles, ShiftRows, MixColumns, dan AddRoundKey.
  - Ronde terakhir hanya melibatkan SubNibbles, ShiftRows, dan AddRoundKey.
- **Output** : Ciphertext yang terenkripsi.

#### Flowchart Enkripsi
![enkripsi drawio](https://github.com/user-attachments/assets/c1153afb-00ca-4111-820a-11fb01c9a7e6)

**Penjelasan alur flowchart Enkripsi**
1. **Mulai**
  - Proses enkripsi dimulai dengan menerima plaintext dan key sebagai input.
3. **Key Expansion**
  - Langkah pertama dalam proses enkripsi adalah melakukan key expansion untuk menghasilkan round keys yang digunakan di setiap ronde.
  - **Key Expansion** mengambil kunci utama 16 bit dan memperluasnya menjadi 4 round keys yang masing-masing digunakan dalam setiap ronde enkripsi.
3. **Add RoundKey (Ronde 0)**
  - Pada ronde pertama, dilakukan **AddRoundKey** yang merupakan operasi XOR antara plaintext dan round key pertama.
  - Tahap pertama dalam proses enkripsi dan memastikan data terenkripsi.
4. **Ronde 1 (Proses Enkripsi)**
  - **SubNibbles** : Tahap pertama dalam ronde 1 adalah substitusi menggunakan S-Box untuk menggantikan setiap nibble (4 bit) dengan nilai yang sudah ditentukan dalam tabel S-Box.
  - **ShiftRows** : Langkah selanjutnya adalah **ShiftRows** yang menggeser baris-baris matriks state untuk menciptakan pencampuran data lebih lanjut.
  - **MixColumns** : Setelah itu, **MixColumns** digunakan untuk mencampur nilai di setiap kolom state, menciptakan lebih banyak difusi.
  - **AddRoundKey** : Setelah langkah-langkah ini, kunci ronde kedua ditambahkan menggunakan operasi XOR lagi pada state yang telah diubah.
5. **Ronde 2 (Proses Enkripsi)**
  - Tahap yang sama diulang untuk ronde kedua, namun kali ini **MixColumns** dihapus dan hanya **SubNibbles**, **ShiftRows**, dan **AddRoundKey** yang dilakukan pada ronde ini.
6. **Ronde 3 (Ronde Akhir)**
  - **SubNibbles** : Proses substitusi nibble.
  - **ShiftRows** : Proses pergeseran baris matriks state.
  - **AddRoundKey (Final)** : Pada ronde terakhir, dilakukan AddRoundKey menggunakan kunci ronde ketiga, tetapi langkah MixColumns diabaikan.
7. **Ciphertext**
  - Setelah ronde ketiga, hasil akhirnya adalah ciphertext, yaitu hasil enkripsi dari plaintext yang diinputkan.
  - Proses enkripsi selesai.

#### Fungsi Key Expansion
- **Inisialisasi Kunci** : Kunci 16-bit yang diberikan dipecah menjadi empat elemen awal (w[0], w[1], w[2], w[3]).
- **Proses Ekspansi Kunci**
   - Setiap elemen kunci yang ada diproses dengan **S-Box** (substitusi nibble) untuk mengubah nilai-nilai yang ada.
   - Setelah substitusi, dilakukan operasi **XOR** antara elemen kunci yang sudah diproses dan elemen kunci sebelumnya, serta penambahan **Round Constant (RC)** untuk menghasilkan nilai kunci ronde berikutnya.
   - Dengan cara ini, kunci ronde selanjutnya dibentuk secara berurutan.
- **Pengulangan**: Proses ini diulang hingga mencapai jumlah kunci yang diperlukan untuk setiap ronde enkripsi (hingga i < 16).

#### Flowchart Key Expansion
![keyexpansions](https://github.com/user-attachments/assets/39552885-8436-4ee9-afbc-2be63869ebb6)

**Penjelasan alur flowchart Key Expension**
1. **Mulai**
  - Proses **Key Expansion** dimulai dengan menerima key utama yang berukuran 16 bit (4 nibble).
2. **Inisialisasi Key**
  - Key utama dipecah menjadi empat elemen (w[0] hingga w[3]) yang digunakan untuk ronde pertama.
3. **Proses Ekspansi Kunci**
  - **S-Box** : Proses pertama dalam key expansion adalah menerapkan **S-Box** pada elemen kunci untuk mengubah nilai-nilai yang ada.
  - **XOR dengan Kunci Sebelumnya** : Kemudian, elemen kunci diperluas dengan XOR antara elemen kunci yang sudah ada, yang menggabungkan hasil **S-Box** dengan konstanta ronde (RC, round constant).
  - **Penambahan Kunci** : Dengan proses ini, kunci ronde berikutnya dihitung dan disalin ke variabel yang relevan.
4. **Cek Jika i < 16**
  - Setelah langkah ini, dicek apakah indeks kunci (i) sudah mencapai nilai 16. Jika belum, proses ekspansi kunci dilanjutkan untuk menghasilkan round key lebih banyak. Jika ya, maka proses key expansion selesai.
5. **Selesai**
  - Setelah proses **Key Expansion** selesai, round keys untuk setiap ronde telah siap digunakan untuk proses enkripsi.

#### Fungsi Dekripsi (`decrypt`)
- **Input** : Ciphertext 16 bit dan kunci 16 bit.
- **Proses**
  - Melakukan operasi dekripsi dengan urutan kebalikan dari enkripsi: InverseSubNibbles, InverseShiftRows, InverseMixColumns, dan AddRoundKey.
- **Output**: Plaintext yang didekripsi.

#### Mode ECB dan CBC
- **ECB (Electronic Codebook)**
  - Setiap blok plaintext dienkripsi secara independen.
  - Mode ini sangat sederhana, namun memiliki kelemahan karena pola pada plaintext dapat terlihat pada ciphertext.
- **CBC (Cipher Block Chaining)**
  - Menggunakan **Initialization Vector (IV)** dan hasil enkripsi blok sebelumnya.
  - Setiap blok plaintext di-XOR dengan ciphertext blok sebelumnya sebelum enkripsi.
  - Memberikan keamanan lebih baik karena blok-blok saling terkait.

### 2. Modul `test_cases.py`
Modul ini berfungsi untuk menjalankan beberapa **test case** untuk memastikan fungsi enkripsi dan dekripsi bekerja dengan benar. Setiap test case akan mencetak hasil enkripsi dan dekripsi, serta membandingkan hasilnya dengan nilai ekspektasi.

#### Contoh Test Case
- **Test 1** (Semua nilai 0)
  - **Plaintext** = [0x0, 0x0, 0x0, 0x0]
  - **Key** = [0x0, 0x0, 0x0, 0x0]
  - **Ciphertext yang diharapkan** = [0xA, 0xA, 0x9, 0x9]
- **Test 2** (Nilai plaintext dan key acak)
  - **Plaintext** = [0x1, 0x2, 0x3, 0x4]
  - **Key** = [0x5, 0x6, 0x7, 0x8]
  - **Ciphertext yang diharapkan** = [0xB, 0x9, 0x6, 0x4]
- **Test 3** (Nilai plaintext dan key maksimum)
  - **Plaintext** = [0xF, 0xF, 0xF, 0xF]
  - **Key** = [0xF, 0xF, 0xF, 0xF]
  - **Ciphertext yang diharapkan** = [0x5, 0x5, 0x7, 0x7]

![Screenshot 2025-04-27 212329](https://github.com/user-attachments/assets/eb90a375-0ec7-485b-ad71-9b7704838f93)
![Screenshot 2025-04-27 212348](https://github.com/user-attachments/assets/ed658df0-4dd8-4256-9fe3-73c746a529e8)
![Screenshot 2025-04-27 212403](https://github.com/user-attachments/assets/973d152f-dbe3-4e27-a0a7-ba0e5593a381)

#### Cara Menjalankan
1. Buka terminal.
2. **Jalankan `python test_cases.py`** untuk menguji efek perubahan bit pada plaintext dan kunci.
3. Setelah dijalankan akan menjalankan semua test case yang ada dan mencetak hasil enkripsi dan dekripsi beserta perbandingannya dengan nilai yang diharapkan.

### 3. Modul `avalanche_analysis.py`
Modul ini digunakan untuk menguji **efek avalanche** yang mengukur bagaimana perubahan kecil dalam plaintext atau kunci (1 bit) dapat mempengaruhi perubahan di ciphertext.

#### Fungsi `avalanche_effect`
- Menguji perubahan bit di ciphertext ketika satu bit di plaintext diubah.
- **Proses** : Mengubah setiap bit dalam plaintext dan menghitung jumlah bit yang berubah di ciphertext.

#### Fungsi `key_avalanche_effect`
- Menguji perubahan bit di ciphertext ketika satu bit di kunci diubah.
- **Proses** : Mengubah setiap bit dalam kunci dan menghitung jumlah bit yang berubah di ciphertext.

#### Cara Menjalankan
1. Buka terminal.
2. **Jalankan `python avalanche_analysis.py`** untuk menguji efek perubahan bit pada plaintext dan kunci.
3. Setelah dijalankan akan terlihat seberapa banyak bit pada ciphertext berubah setiap kali satu bit diubah pada input.

#### Pengujian
#### Efek Avalanche pada Plaintext
- Setiap kali 1 bit di plaintext diubah, jumlah bit yang berubah pada ciphertext dihitung. Pengujian ini menunjukkan seberapa sensitif algoritma terhadap perubahan kecil di plaintext.

#### Efek Avalanche pada Key
- Begitu pula dengan perubahan kecil pada key, yang juga menghasilkan perubahan yang besar di ciphertext. Ini menunjukkan kuatnya sifat algoritma terhadap perubahan input yang kecil.

![Screenshot 2025-04-27 213224](https://github.com/user-attachments/assets/c14e3944-93c1-48b4-aa12-689a8b9bea34)

### 4. Modul `utils.py`
Modul ini berisi beberapa fungsi utilitas yang digunakan oleh algoritma Mini-AES, seperti:
- **S-Box dan Inverse S-Box** : Fungsi untuk melakukan substitusi dan inversinya.
- **ShiftRows dan InverseShiftRows** : Fungsi untuk menggeser baris dan inversinya.
- **MixColumns dan InverseMixColumns** : Fungsi untuk mengubah kolom dan inversinya.
- **AddRoundKey** : Fungsi untuk menambahkan kunci ronde ke state.

### 5. Modul `gui_app.py`
Modul ini menyediakan **GUI (Graphical User Interface)** menggunakan Tkinter untuk memudahkan pengguna dalam melakukan enkripsi dan dekripsi dengan Mini-AES. Pengguna dapat memilih mode operasi (Single Block, ECB, CBC), memasukkan plaintext, key, dan IV (untuk CBC), serta melihat hasil enkripsi dan dekripsi.

#### Fitur GUI
- **Mode Operasi** : Pengguna dapat memilih antara mode Single Block, ECB, atau CBC.
- **Input** : Pengguna dapat memasukkan nilai plaintext dan key dalam format hex.
- **Output** : Hasil enkripsi dan dekripsi ditampilkan dalam bentuk hex.

#### Implementasi Program
Program ini diimplementasikan dalam bahasa Python dengan fitur
- GUI menggunakan Tkinter.
- Dukungan untuk enkripsi dan dekripsi.
- Mode operasi block ECB dan CBC.
- Analisis efek avalanche.
- Kemampuan menyimpan dan memuat data.
- Tampilan output proses tiap ronde.

#### Cara Menggunakan Program
1. Buka terminal.
2. **Jalankan `python gui_app.py`** untuk memulai aplikasi GUI.
3. Pilih mode operasi (Single Block, ECB, CBC).
4. Masukkan plaintext/ciphertext dan key dalam format hex.
5. Untuk **CBC**, tambahkan **Initialization Vector (IV)**.
6. Klik tombol "Encrypt" atau "Decrypt" untuk melakukan operasi.
7. Lihat hasil dan log pada tab **Log**.
8. Anda dapat **menyimpan/memuat data dan log ke file**.

![Screenshot 2025-04-27 212545](https://github.com/user-attachments/assets/b34ce7ec-5f5d-420a-80ee-280685ddf959)
![Screenshot 2025-04-27 212852](https://github.com/user-attachments/assets/0576a7db-09e4-48dd-8b37-296f74a211d0)
![Screenshot 2025-04-27 212906](https://github.com/user-attachments/assets/c454dcdd-57e8-4722-9871-b7cb8931c0ba)
![Screenshot 2025-04-27 212942](https://github.com/user-attachments/assets/4c6c121e-337a-403e-9074-0ef1e51ac5ea)
![Screenshot 2025-04-27 213047](https://github.com/user-attachments/assets/66095fd9-376e-4de9-9dfe-b48a61ac843d)
![Screenshot 2025-04-27 213108](https://github.com/user-attachments/assets/f4b5c1b8-ef09-4709-ad0d-c007747fd754)
![Screenshot 2025-04-27 213132](https://github.com/user-attachments/assets/ce1323a4-0fdb-4181-8556-e665d99e3c7e)

## Kelebihan dan Keterbatasan Mini-AES
### Kelebihan Mini-AES
- **Kesederhanaan** : Mudah dipahami dan diimplementasikan sebagai bahan pembelajaran.
- **Komputasi Ringan** : Membutuhkan daya komputasi yang rendah karena ukuran block dan kunci yang kecil.
- **Demonstratif** : Menunjukkan konsep dasar algoritma AES seperti substitusi, permutasi, dan diffusion.
- **Efek Avalanche** : Meskipun sederhana, tetap menunjukkan efek avalanche yang baik, dimana perubahan 1 bit input menyebabkan perubahan signifikan pada output.

### Keterbatasan Mini-AES
- **Keamanan Rendah** : Dengan ukuran kunci dan block yang sangat kecil (16 bit), Mini-AES sangat rentan terhadap serangan brute force.
- **Ruang Kunci Terbatas** : Hanya memiliki 2^16 (65, 536) kemungkinan kunci yang sangat mudah untuk dicoba satu per satu.
- **Struktur Sederhana** : MixColumns dan ShiftRows yang disederhanakan mengurangi difusi yang terjadi pada algoritma.
- **Tidak Praktis** : Tidak cocok untuk penggunaan nyata karena ukuran block yang sangat terbatas (hanya 2 Bit).

## Kesimpulan
- Mini-AES berhasil diimplementasikan dengan baik dan pengujian efek avalanche menunjukkan bahwa algoritma ini sensitif terhadap perubahan input, yang merupakan sifat penting dalam kriptografi untuk memastikan keamanan.
- GUI memudahkan penggunaan Mini-AES tanpa memerlukan interaksi langsung dengan kode.

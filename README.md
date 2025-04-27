# kriptografi-mini-aes-kelompok8

Anggota Kelompok
|  Nama  |  NRP  |
|--------|-------|
| Dian Anggraeni Putri | 5027231016 |
| Acintya Edria Sudarsono | 5027231020 |
| Tsaldia Hukma Cita | 5027231036 |
| Rafika Az Zahra Kusumastuti | 5027231050 |
| Nisrina Atiqah Dwiputri Ridzki | 5027231075 |

## Alur Flowchart

Penjelasan Alur Flowchart Mini-AES

1. 
2. 

## A. Spesifikasi Dasar
### Implementasi Dasar Mini-AES
#### Representasi Plaintext dan Key
- **Plaintext** dan **Key** yang digunakan memiliki panjang **16 bit** atau **4 nibble**.
- Keduanya harus diinput dalam format heksadesimal dan representasi disesuaikan dengan standar untuk algoritma Mini-AES.

#### Operasi yang Harus Diimplementasikan
- **SubNibbles**
  - Setiap **4 bit** dari plaintext digantikan menggunakan **S-Box 4 bit** yang merupakan tabel substitusi yang digunakan untuk mengenkripsi data.
  - Tujuan : menambah kebingungan dalam hubungan antara plaintext dan ciphertext.

- **ShiftRows**
  - Proses ini menggeser baris data dalam blok **2x2** untuk meningkatkan **diffusion**.
  - Baris kedua dan ketiga dari blok akan digeser satu posisi ke kiri untuk menyebarkan perubahan bit pada data ke seluruh ciphertext.

- **MixColumns**
  - Operasi ini menggunakan matriks sederhana pada **GF(2⁴)** atau field untuk bilangan biner **4 bit**. 
  - Tujuan : mencampur data dalam kolom untuk meningkatkan efek **diffusion** dimana perubahan kecil pada plaintext akan mempengaruhi banyak bit ciphertext.

- **AddRoundKey**
  - Pada setiap ronde **AddRoundKey** melakukan **XOR** antara state dan kunci ronde yang sesuai. 
  - Tujuan : memastikan bahwa kunci berubah setiap ronde dan memberi lapisan keamanan tambahan untuk algoritma ini.

#### Jumlah Round
- Mini-AES terdiri dari **3 ronde** dengan setiap ronde melibatkan proses SubNibbles, ShiftRows, MixColumns, dan AddRoundKey.
- Setelah ronde ketiga, proses enkripsi selesai dan ciphertext dihasilkan.

#### Bahasa Pemrograman
- Program ini diimplementasikan menggunakan **Python** yang direkomendasikan karena sintaksisnya yang mudah dibaca dan kemampuan debugging yang kuat.

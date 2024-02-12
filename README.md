# Cyberpunk 2077 Breach Protocol with Brute Force
Program Cyberpunk 2077 Breach Protocol adalah minigame meretas pada permainan video Cyberpunk 2077.
Minigame ini merupakan simulasi peretasan jaringan local dari ICE (Intrusion Countermeasures
Electronics) pada permainan Cyberpunk 2077. Program ini diselesaikan dengan Brute Force Algorithm untuk memenuhi Tugas Kecil 1 IF2211 Strategi Algoritma

### Komponen dan Aturan Permainan
Komponen pada permainan ini antara lain adalah:
1. Token – terdiri dari dua karakter alfanumerik seperti E9, BD, dan 55.
2. Matriks – terdiri atas token-token yang akan dipilih untuk menyusun urutan kode.
3. Sekuens – sebuah rangkaian token (dua atau lebih) yang harus dicocokkan.
4. Buffer – jumlah maksimal token yang dapat disusun secara sekuensial.
   
Aturan permainan Breach Protocol antara lain:
1. Pemain bergerak dengan pola horizontal, vertikal, horizontal, vertikal (bergantian) hingga
semua sekuens berhasil dicocokkan atau buffer penuh.
IF2211 Strategi Algoritma – Tugas Kecil 1 1
2. Pemain memulai dengan memilih satu token pada posisi baris paling atas dari matriks.
3. Sekuens dicocokkan pada token-token yang berada di buffer.
4. Satu token pada buffer dapat digunakan pada lebih dari satu sekuens.
5. Setiap sekuens memiliki bobot hadiah atau reward yang variatif.
6. Sekuens memiliki panjang minimal berupa dua token.

### Requirement
Untuk dapat menjalankan program ini, anda perlu menginstall **Python** di device yang Anda gunakan.

### Cara Menjalankan dan Menggunakan Program
1. Clone repository ini ``$ git clone  https://github.com/shulhajws/Tucil1_13522087.git``
2. Jalankan program pada `main.py`
3. Anda dapat memasukkan kebutuhan yang diinginkan melalui file .txt maupun digenerasi otomatis berdasarkan masukan Anda pada CLI. Jika ingin menggunakan file.txt, letakkan file.txt pada folder yang sama dengan folder program.

### Pembuat Program
| NIM       | Nama   | Kelas |
|-----------|--------|-------|
| 13521087  | Shulha | K01   |

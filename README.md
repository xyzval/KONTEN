# 📜 PANDUAN LENGKAP & TEMPLATE CAROUSEL TIKTOK (PINDAH CHAT)

Dokumen ini berisi seluruh standar desain, aturan tipografi, formula visual, daftar proyek yang telah dibuat, serta teks siap pakai (*prompt*) untuk disalin saat memulai sesi obrolan baru.

---

## 📋 TEKS SIAP PAKAI (COPY-PASTE KE CHAT BARU)

Salin teks di dalam blok berikut dan tempelkan sebagai pesan pertama saat Anda membuka chat baru:

```text
Halo! Saya ingin melanjutkan pembuatan konten carousel TikTok bertema Dark Quotes, Harsh Truth, Realita Kehidupan, & Filsafat Islam.

Mohon gunakan standar dan format berikut untuk setiap slide yang akan dibuat:

1. STANDAR GAYA VISUAL (ART STYLE):
   - Aliran Seni: Renaissance / Baroque Chiaroscuro Oil Painting (pencahayaan dramatis gaya Rembrandt & Caravaggio, hangat cahaya lilin temaram, bayangan gelap pekat, detail lukisan klasik tinggi).
   - Rasio Gambar: Vertical Portrait 3:4 (optimal untuk carousel TikTok & Instagram).
   - Karakter Utama:
     * Slide 1 (Penanya / Hook): Dark Shadow Demon bertanduk obsidian, mata merah menyala, berjubah kegelapan kuno (atau sosok Cendekiawan/Manusia sesuai tema).
     * Slide 2 (Penjawab / Inti): Tengkorak klasik (bisa versi elegan merokok dengan rompi / versi menyedihkan berbalut kain lusuh sesuai konteks kalimat), atau sosok Ustadz/Cendekiawan bersahaja untuk tema keagamaan/hadits.

2. STANDAR TIPOGRAFI & DESAIN SLIDE:
   - Font Latin: Roboto-Bold / Roboto-Medium.
   - Font Arab: Amiri-Bold (dengan rendering RTL & ligature yang benar).
   - Box Teks: Kotak hitam transparan membulat (rounded dark semi-transparent card) di bagian tengah/bawah dengan padding rapi agar tulisan sangat kontras dan mudah dibaca.
   - Ikon: Tanda kutip (“) putih di sudut kiri atas kotak teks.
   - Preservasi Teks: 100% mempertahankan kata-kata asli tanpa diubah atau dikurangi.

3. OPTIMASI TIKTOK (FYP & ANTI-DETEKSI AI):
   - Hook Slide 1 yang memancing rasa penasaran tinggi / perdebatan rasional.
   - Rekomendasi sound trending (Memory Reboot, Solitude M83, Snowfall) & hashtag niche.
   - Tips anti-deteksi AI TikTok (pembersihan metadata & penambahan film grain).

Silakan bantu saya membuatkan slide-slide berikutnya dengan standar di atas!
```

---

## 🎨 STANDAR SPESIFIKASI DESAIN & KODE

### 1. Spesifikasi Visual AI
* **Rasio:** `3:4` (Vertical Portrait - e.g. 1086 x 1448 px)
* **Pencahayaan:** *Chiaroscuro* (sumber cahaya lilin temaram, bayangan gelap pekat)
* **Tone Warna:** *Dark Gothic Warm Amber, Deep Charcoal, Muted Gold*

### 2. Parameter Tipografi (Python Pillow)
* **Warna Box:** `RGBA(0, 0, 0, 185)` (Hitam transparan ~75%)
* **Radius Sudut Box:** `14 - 16 px`
* **Warna Teks:** `RGB(255, 255, 255)` (Putih solid)
* **Ikon Kutip:** Tanda `“` di pojok kiri atas box
* **Tata Letak:**
  * Slide 1: Box berada di tengah vertikal (`y ~ 48-52%`)
  * Slide 2: Box berada di area tengah-bawah (`y ~ 54-60%`)

---

## 🗂️ RIWAYAT TEMPLATE & KARYA YANG TELAH DIBUAT

| No | Tema / Kutipan Utama | Slide 1 (Hook / Penanya) | Slide 2 (Jawaban / Inti) | File Hasil |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Ihya' Ulumuddin (Beban Suami & Tekanan Finansial)** | Pria lelah terbaring sendiri di ranjang | Bayangan jubah bertudung hitam (*Shrouded Shadow*) + Teks Arab & Terjemahan lengkap | `slide1_konsep_tudung_bayangan.jpg`<br>`slide2_revisi_final.jpg` |
| **2** | **Kehilangan Ibu & Kesendirian Keluarga** | Iblis bertanduk bertanya di meja lilin: *"apa yang kamu rasakan setelah ibumu sudah tiada ??"* | Tengkorak berompi vintage merokok: *"tidak ada lagi keluarga yang peduli kepadaku..."* | `slide1_iblis_tengkorak_kotak.jpg`<br>`slide2_iblis_tengkorak_kotak.jpg` |
| **3** | **Realita Karma & Tindakan** | Iblis menunjuk provokatif: *"karma itu tidak ada"* | Tengkorak berompi / Pria berbelati: *"itu hanyalah konsep untuk menghibur korban... bertindaklah!"* | `slide1_karma_iblis_tengkorak.jpg`<br>`slide2_karma_iblis_tengkorak.jpg` |
| **4** | **Takdir vs Doa (Filsafat Teologi)** | Iblis menantang: *"berikan aku jawaban untuk pertanyaan ini"* | Ustadz/Kyai bersorban memegang tasbih & kitab kuno menjawab: *"jika takdir sudah diatur..."* | `slide1_ustadz_takdir.jpg`<br>`slide2_ustadz_takdir.jpg`<br>`slide3_ustadz_takdir.jpg` |
| **5** | **Harta Tidak Dibawa Mati vs Kotak Amal** | Saudagar kaya memasukkan uang ke kotak amal: *"kotak amal saja mintanya uang bukan Do'a"* | Iblis merenungi tumpukan koin emas & jam pasir (*hourglass*): *"lantas kenapa banyak orang bilang harta tidak dibawa mati ?"* | `slide1_saudagar_harta.jpg`<br>`slide2_iblis_harta.jpg` |
| **6** | **Topeng Kesucian vs Perlakuan Baik** | Pria melepas topeng emas suci: *"mengapa manusia lebih sibuk terlihat suci daripada menjadi baik ??"* | Iblis memegang topeng emas & kitab: *"memperlakukan orang lain dengan baik jauh lebih bernilai..."* | `slide1_filsafat_kesucian.jpg`<br>`slide2_iblis_topeng_suci.jpg` |
| **7** | **Larangan Mengagungkan Manusia (Hadits Ghuluw)** | Orang-orang bersujud berlebihan pada tahta manusia | Cendekiawan bersorban menatap kubah hijau masjid + Teks Arab Hadits Ibnu Majah | `slide1_ghuluw_manusia.jpg`<br>`slide2_ghuluw_hadits_final.jpg` |
| **8** | **Fakta Menyakitkan Kemiskinan Pria** | Iblis menuntut: *"berikan aku satu fakta yang menyakitkan"* | Tengkorak lusuh tertunduk lesu menopang kepala: *"kemiskinan membuat seorang pria kehilangan haknya..."* | `slide1_fakta_menyakitkan.jpg`<br>`slide2_kemiskinan_tengkorak.jpg` |

---

## 🚀 PANDUAN UPLOAD TIKTOK (OPTIMASI FYP & ANTI-DETEKSI AI)

### 1. Cara Menghilangkan Deteksi Otomatis AI TikTok:
1. **Screenshot Ulang:** Buka gambar di HP, lakukan *screenshot*, lalu upload hasil screenshot tersebut. Ini otomatis menghapus seluruh metadata C2PA / SynthID bawaan AI generator.
2. **Tambahkan Film Grain:** Tambahkan sedikit efek *grain / noise* tipis (**5%**) di CapCut atau editor foto agar algoritma TikTok membacanya sebagai olahan manual.
3. **Matikan Toggle AI:** Pada menu upload TikTok $\rightarrow$ *More options* $\rightarrow$ pastikan opsi *AI-generated content* dalam posisi nonaktif (OFF).

### 2. Rekomendasi Sound Musik:
* **Memory Reboot (Slowed + Reverb)** – *VØJ, Narvent*
* **Solitude (Felsmann + Tiley Reinterpretation)** – *M83*
* **Snowfall** – *Øneheart & Reidenshi*
* **Past Lives (Slowed Instrumental)** – *sapientdream*

### 3. Kumpulan Hashtag Utama:
`#harshtruth #realitahidup #darkquotes #quoteskehidupan #mindset #stoikisme #selfreminder #fyp #fypシ #masukberanda`

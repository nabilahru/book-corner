# Tugas Individu 

Nama    : Nabilah Roslita Utami,
NPM     : 2306223446,
Kelas   : PBP B

## Link Deployment PWS

http://nabilah-roslita-bookcorner.pbp.cs.ui.ac.id/

## Jawaban pertanyaan Tugas Individu 2

****1. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).****
Pertama adalah membuat sebuah direktori bernama book-corner. Kemudian mengaktifkan virtual environment pada cmd untuk mengisolasi aplikasi agar tidak bertabrakan dengan versi lainnya. Lalu membuat file requirements.txt di dalam direktori book-corner yang berisi dependencies untuk di-install dengan perintah “pip install -r requirements.txt” pada cmd. Selanjutnya beri perintah “django-admin startproject book-corner .” untuk membuat proyek Django. Setelah itu, melakukan konfigurasi proyek dengan menambahkan allowed_host pada settings.py. Kemudian cek proyek, dengan menjalankan proyeknya dan mengecek di  http://localhost:8000. Hentikan server dengan ctrl+C dan deactive mode virtual environment.
Selanjutnya membuat repository github bernama book-corner. Lalu lakukan inisiasi direktori lokal book-corner dengan menjalankan perintah git init, lalu git remote. Kemudian tambahkan file .gitignore dalam direktori book-corner untuk menentukan berkas serta direktori yang harus diabaikan git. Setelah itu, lakukan git add, commit, dan push pengerjaan. 
Dalam mengimplementasikan MVT, pertama adalah membuka cmd dan pastikan berada pada direktori utama book-corner serta nyalakan virtual environment. Kemudian, membuat aplikasi baru bernama main dalam proyek dan jalankan “python [manage.py] startapp main”. Lalu daftarkan aplikasi main dengan menambahkan ‘main’ di INSTALLED_APPS pada settings.py. Selanjutnya main.html yang berisi nama toko, nama, kelas. Kemudian, mengubah berkas [models.py] dengan atribut yang dibutuhkan toko. Setelah itu, lakukan migrasi model dengan perintah “python [manage.py] makemigrations” dan “python [manage.py] migrate”. Lalu mengintegrasikan komponen MVT dengan membuat fungsi di [views.py] yang berisi dictionary yang akan diimport ke main.html. Selanjutnya ubah main.html dengan memanggil key untuk mengembalikan nama dan kelas. Lalu melakukan konfigurasi routing URL. Sebelum melakukan deployment kita perlu test dengan unit test apakah program berjalan sesuai keinginan. Lalu git add, commit, push untuk menyimpan perubahan.
Terakhir melakukan deployment ke PWS. Pertama lakukan create new project bernama book-corner dan menyimpan credential. Lalu hubungkan pws dengan direktori menggunakan perintah ke cmd “git remote add pws http://pbp.cs.ui.ac.id/nabilah.roslita/bookcorner”. Kemudian “git branch -M master”, “git push pws master”. Setelah itu, proyek sudah ada pada pws dan dapat diakses secara online.

****2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.****
![alt text](https://github.com/nabilahru/book-corner/blob/main/Bagan%20Request%20Client%C2%A0ke%20Web%20Aplikasi%20Django.png?raw=true)

****3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak!****
git berfungsi sebagai alat untuk menyimpan, mengelola, mengontrol, serta berkolaborasi kode yang dikerjakan secara bersama atau banyak orang (DCloud, 2024).

****4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?****
Framework Django menggunakan bahasa pemograman python yang biasanya merupakan bahasa yang sudah dipelajari oleh pemula. Framework Django juga mempermudah developer untuk tidak perlu coding dari awal, karena Django sudah menyediakan berbagai modul, library, dan API yang lengkap (Biznetgio, 2023).

****5. Mengapa model pada Django disebut sebagai *ORM*?****
Django memiliki kerangka kerja yang memetakan suatu objek python ke struktur database relasional (Fazry, 2024). Sehingga Django disebut sebagai ORM atau object Relational mapping.

Referensi:
Biznetgio. (2023). Django, Framework Python untuk Mempermudah Kustomisasi Website. Retrieved September 10, 2024, from https://www.biznetgio.com/news/django
DCloud. (2024). Mengenal Apa Itu Git dan Fungsinya dalam Software Development. Retrieved September 10, 2024, from https://dcloud.co.id/blog/apa-itu-git.html#:~:text=Git%20adalah%20alat%20software%20development,code
Fazry. (2024). Pengantar Django ORM: Memahami dan Menggunakan Model dalam Django. Retrieved September 10, 2024, from https://rumahcoding.co.id/pengantar-django-orm-memahami-dan-menggunakan-model-dalam-django/


## Jawaban pertanyaan Tugas Individu 3
****1. Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?****
Karena suatu platform pastinya butuh pertukaran data dan biasanya data-data dikirimkan dalam stack ke stack lain. Butuh pengelolaan dan pengoptimalan dalam pengirimannya.

****2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?****
Mana yang lebih baik dapat dinilai dari tujuan penggunaannya. Misalnya, penggunaan XML lebih baik ketika ingin menyimpan, mengelola data dengan tipe data yang bervariasi (Kompleks), karena penyimpanan data format XML mudah untuk dibaca oleh mesin dan mendukung semua tipe data JSON (Boolean, waktu, biner dll). Namun, Penggunaan JSON bisa lebih baik ketika ingin melakukan pertukaran data, karena format JSON memakai pasangan kunci-nilai, dimana kunci berupa string yang akan mengakses nilainya. Syntax JSON juga lebih mudah ditulis dan dibaca sehingga dapat mendefinisikan objek dengan mudah. Dalam pertukaran data JSON juga lebih cepat di sisi server.

Kenapa JSON lebih populer? karena JSON lebih baru, lebih fleksibel dan lebih populer. JSON bersifat independen di setiap bahasa pemograman dan merupakan output API yang relevan dengan berbagai aplikasi (Amazon, n. d).

****3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?****
Untuk memvalidasi input dari form apakah sesuai dengan tipe data pada field fungsi membuat objek di models.py.

****4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?****
`csrf_token` berfungsi sebagai security/keamanan demi mencegah serangan cyber. cara kerjanya yaitu dengan mengenerate token secara acak untuk otorisasi setiap pengguna. Jika tidak ada, penyerang dapat menyamar sebagai pengguna dan mengirim request ke web. Penyerang memanfaatkannya untuk melakukan eksploitasi web atau kejahatan cyber lainnya tanpa diketahui pengguna aslinya.  

****5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)****
Membuat file base.html pada direktori templates baru sebagai kerangka umum pada template dasar. Lalu daftarkan kerangka terebut pada TEMPLATES di settings.py. Kemudian, tambahkan uuid sebagai enumerate ID setiap objek yang dibuat di models.py. dan migrate pertambahan atribut ID tersebut. 

Selanjutnya adalah membuat form input dan menampilkannya pada html. Pertama, buat file [forms.py](http://forms.py) untuk membuat field di modelnya. Lalu, pada views.py, buat fungsi entry untuk memvalidasi input dan memsubmitnya dari forms.py. Kemudian tambahkan entries di show_main pada context agar terlihat saat adanya request. Setelah itu, tambahkan variabel entry tadi ke urlpatterns di [urls.py](http://urls.py) agar fungsi dapat diakses. Kemudian, pada main/templates buat create_product_entry.html untuk POST submit product input. Tambahkan juga kode pada main.html untuk menampilkan form input yang sudah dibuat. 

Selanjutnya adalah menampilkan data dalam bentuk XML dan JSON dan juga berdasarkan ID datanya. Pada [views.py](http://views.py) tambahkan fungsi yang membuat suatu object yang me-return HTTP dalam bentuk XML dan JSON. Lalu, fungsi yang sama namun mereturn juga berdasarkan ID. Sehingga totalnya ada 4 fungsi yaitu, show_xml, show_json, show_xml_by_id, show_json,_by_id. Kemudian daftarkan ke path URL ke urlpatterns di [urls.py](http://urls.py) untuk rounting URL.

Selanjutnya adalah postman sebagai data viewer. caranya adalah send link data yang ingin dilihat. Misalnya melihat data format XML by IDnya [http://localhost:8000/xml/[id]]. maka akan terlihat objek-objek yang sudah dibuat.

****Screenshoot Postman:****

Referensi:
Amazon. (n. d). Apa Perbedaan antara JSON dan XML? Retrieved September 17, 2024, from https://aws.amazon.com/id/compare/the-difference-between-json-xml/
Codingstudio. (2023). CSRF (Cross Site Request Forgery): Pengertian, Jenis dan Cara Mencegahnya. Retrieved September 17, 2024, from https://codingstudio.id/blog/csrf-adalah/

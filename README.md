# Tugas Individu 

Nama    : Nabilah Roslita Utami,
NPM     : 2306223446,
Kelas   : PBP B

## Link Deployment PWS

http://nabilah-roslita-bookcorner.pbp.cs.ui.ac.id/

## Tugas Individu 2

****1. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).****
Pertama adalah membuat sebuah direktori bernama book-corner. Kemudian mengaktifkan virtual environment pada cmd untuk mengisolasi aplikasi agar tidak bertabrakan dengan versi lainnya. Lalu membuat file requirements.txt di dalam direktori book-corner yang berisi dependencies untuk di-install dengan perintah “pip install -r requirements.txt” pada cmd. Selanjutnya beri perintah “django-admin startproject book-corner .” untuk membuat proyek Django. Setelah itu, melakukan konfigurasi proyek dengan menambahkan allowed_host pada settings.py. Kemudian cek proyek, dengan menjalankan proyeknya dan mengecek di  http://localhost:8000. Hentikan server dengan ctrl+C dan deactive mode virtual environment.
Selanjutnya membuat repository github bernama book-corner. Lalu lakukan inisiasi direktori lokal book-corner dengan menjalankan perintah git init, lalu git remote. Kemudian tambahkan file .gitignore dalam direktori book-corner untuk menentukan berkas serta direktori yang harus diabaikan git. Setelah itu, lakukan git add, commit, dan push pengerjaan. 
Dalam mengimplementasikan MVT, pertama adalah membuka cmd dan pastikan berada pada direktori utama book-corner serta nyalakan virtual environment. Kemudian, membuat aplikasi baru bernama main dalam proyek dan jalankan “python [manage.py] startapp main”. Lalu daftarkan aplikasi main dengan menambahkan ‘main’ di INSTALLED_APPS pada settings.py. Selanjutnya main.html yang berisi nama toko, nama, kelas. Kemudian, mengubah berkas [models.py] dengan atribut yang dibutuhkan toko. Setelah itu, lakukan migrasi model dengan perintah “python [manage.py] makemigrations” dan “python [manage.py] migrate”. Lalu mengintegrasikan komponen MVT dengan membuat fungsi di [views.py] yang berisi dictionary yang akan diimport ke main.html. Selanjutnya ubah main.html dengan memanggil key untuk mengembalikan nama dan kelas. Lalu melakukan konfigurasi routing URL. Sebelum melakukan deployment kita perlu test dengan unit test apakah program berjalan sesuai keinginan. Lalu git add, commit, push untuk menyimpan perubahan.
Terakhir melakukan deployment ke PWS. Pertama lakukan create new project bernama book-corner dan menyimpan credential. Lalu hubungkan pws dengan direktori menggunakan perintah ke cmd “git remote add pws http://pbp.cs.ui.ac.id/nabilah.roslita/bookcorner”. Kemudian “git branch -M master”, “git push pws master”. Setelah itu, proyek sudah ada pada pws dan dapat diakses secara online.

****2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.****
![alt text](https://github.com/nabilahru/book-corner/blob/main/picture/Bagan%20Request%20Client%C2%A0ke%20Web%20Aplikasi%20Django.png?raw=true)

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


## Tugas Individu 3
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
XML
![alt text](https://github.com/nabilahru/book-corner/blob/main/picture/XML.png?raw=true)
JSON
![alt text](https://github.com/nabilahru/book-corner/blob/main/picture/json.png?raw=true)
XML by ID
![alt text](https://github.com/nabilahru/book-corner/blob/main/picture/XML%20by%20ID.png?raw=true)
JSON by ID
![alt text](https://github.com/nabilahru/book-corner/blob/main/picture/JSON%20by%20ID.png?raw=true)

Referensi:
Amazon. (n. d). Apa Perbedaan antara JSON dan XML? Retrieved September 17, 2024, from https://aws.amazon.com/id/compare/the-difference-between-json-xml/
Codingstudio. (2023). CSRF (Cross Site Request Forgery): Pengertian, Jenis dan Cara Mencegahnya. Retrieved September 17, 2024, from https://codingstudio.id/blog/csrf-adalah/

## Tugas Individu 4

****1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`****

HttpResponseRedirect() argumen utamanya harus sebuah url, sedangkan Redirect() dapat menerima model, view atau url sebagai argumennya. Redirect() juga dapat mengarahkan pengguna ke halaman web lain dan mengembalikan HttpResponseRedirect(), sehingga redirect lebih fleksibel.

****2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!****

Penghubungan suatu model dengan user melalui suatu relation antara products yang tertaut oleh seorang pengguna atau disebut ForeignKey. Penghubungan dilakukan dengan mengotorisasi objek dengan user (Sebelum disimpan, field user akan mereturn request.user yang sedang login untuk menvalidasi).

****3. Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.****

*Authentication* adalah proses login atau memverifikasi identitas pengguna. Sedangkan *Authorization* adalah izin akses/permission yang diberikan sesuai pengguna/role dalam mengakses data/sistem/fungsi halaman web. Saat pengguna login, sistem akan memverifikasi siapa pengguna dan menentukan hak aksesnya.
Dalam membuat proses login, Django menyediakan fungsi tersendiri yang dapat diimport langsung untuk mempermudah proses *authorization* dan *authentication.* 

****4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua cookies aman digunakan?****

Session ID adalah suatu barisan karakter unik yang menjadi sebuah token untuk mengidentifikasi pengguna. Django akan mengingat pengguna login dengan session ID yang disimpan sebagai cookie pada browser. Selain itu, cookie juga dapat menyimpan sesi login, mengingat preferensi situs, mempersonalisai konten dan menampilkan iklan (Telkomsel, 2022). Akan tetapi, sekalipun cookie disimpan dari sisi perangkat pengguna, terdapat website mencurigakan yang dapat mencuri data-data yang terekam cookie.

****5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).****

Pertama adalah membuat sebuah form untuk pengguna mensubmit suatu data. Buat fungsi register dan fungsi login pada [views.py] untuk membuat akun serta login pengguna. Lalu buatlah register.html dan login.html sebagai templatenya. Kemudian, routing fungsi register dan fungsi login yang sudah dibuat pada urlpatterns di main/[urls.py].  Setelah itu, buat fungsi logout pada views.py serta tambahkan hyperlink tag code html di main.html. Lalu, routing fungsi tersebut di urls.py. 

Selanjutnya merestriksi akses halaman main. Tambahkan @login_required pada fungsi show_main di views.py. Pada step ini menambahkan cookie pada validasi login. Kemudian, memanfaatkan cookies untuk menyimpan sesi login pengguna dengan membuat fungsi validasi saat login dan menyimpan last login. Lalu, tambahkan last login pada context di show_main. Kemudian, pastikan fungsi logout terdapat code yang akan menghapus cookie ketika pengguna logout. Setelah itu, tambahkan last login pada template main.html. 

Selanjutnya, menghubungkan user dan model. Tambahkan atribut user untuk mengotorisasi data dan penggunanya. Lalu, pada views yaitu fungsi create_product_entry buat code validasi user yang mengisi form baru menyimpannya. Kemudian, ubah value dictionary name pada context menjadi request user yang login. Setelah itu, lakukan migration dan migrate.

Referensi: StackOverflow. (2014). What the difference between using Django redirect and HttpResponseRedirect? Retrieved September 23, 2024, from https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect
Telkomsel. (2022). Cookies Adalah? Pengertian, Fungsi, Jenis, dan Cara Kerjanya. Retrieved September 24, 2024, from https://www.telkomsel.com/jelajah/jelajah-lifestyle/cookies-adalah-pengertian-fungsi-jenis-dan-cara-kerjanya
Vivi, S. (2021). Cookies Browser: Fungsi, Keamanan, dan Cara Mengelolanya. Retrieved September 24, 2024, from https://www.exabytes.co.id/blog/cookies-browser-adalah/

## Tugas Individu 5

**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
Urutan prioritas CSS dari yang paling kuat:
- ID Selector (#): Mengelompokkan berdasarkan id yang unik. Biasanya untuk style khusus seperti judul utama.
- Class Selector (.): Mengelompokkan beberapa elemen dengan suatu (.namaclass). Untuk konsistensi desain.
- Element Selector (tanpa # / .): Mengelompokkan elemen berdasarkan jenisnya. Misalnya, p untuk paragraf.
- Universal selector(*): Mengelompokkan semua elemen pada suatu dokumen. Ini akan mengatur style pada seluruh elemen di halaman web.

**2. Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi *web*? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*!**
*Responsive design* adalah suatu website yang designnya otomatis akan selalu menyesuaikan *screensize* dan *viewports*. Jadi, *responsive design* sangat penting bagi suatu *website*, karena *devices* pengguna yang bermacam-macam membutuhkan *website* yang dapat menyesuaikannya. *Responsive design* akan membuat tampilan *website* yang sesuai sehingga tetap bagus diakses di *device* manapun.
Contoh website tidak responsive: Siak-NG
Contoh website responsive: Tailwind

**3. Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut!**
Ketiga hal tersebut merupakan box model pada CSS yang membungkus tiap elemen html, perbedaannya terletak pada tingkatannya:
- *Padding*: Mengosongkan area di sekitar konten dan membungkusnya. (transparan)
- *Border*: Membungkus padding yang berisi konten. Semacam garis tepi padding.
- *Margin*: Area di sekitar border yang kosong. (transparan)

**4. Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!**
*Flex box* adalah pengaturan *layout* pada CSS, digunakan untuk mengatur *container* atau elemen di dalam suatu web. 
*Grid Layout* memberikan modul *grid-based* untuk sistemnya berdasarkan kolom dan baris. Kegunaannya untuk mempermudah letak design suatu website.

**5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!**

Pertama-tama adalah Menambahkan fungsi edit_product dan delete_product pada views.py. Lakukan routing urls untuk mengakses fungsi yang sudah dibuat. Selanjutnya membuat template dengan tailwind. Tambahkan CDN (*Content Delivery Network*) pada bagian head. Kemudian, membuat navbar.html untuk versi desktop dan mobile yang bersifat responsive. Lalu, tambahkankan *middleware* WhiteNoise agar Django dapat mengelola file statis. Styling login.html, register.html, card_product.html, create_product_entry.html, edit_product.html dengan tailwind. Lalu, apabila membutuhkan file statis, tambahkan load static pada awal tiap file yang membutuhkan.

Referensi:
Pratama, M. A. (2021). *Mengenal Flexbox Pada CSS*. Retrieved September 30, 2024, from https://www.gamelab.id/news/817-mengenal-flexbox-pada-css
Revou. (n.d.). *CSS Selectors: Jenis, Cara Membuat, dan Contoh*. Retrieved September 30, 2024, from https://revou.co/panduan-teknis/css-selectors
W3School. (n.d.). *CSS Grid Layout Module*. Retrieved September 30, 2024, from https://www.w3schools.com/CSS/css_grid.asp
W3School. (n.d.). *HTML Responsive Web Design*. Retrieved September 30, 2024, from https://www.w3schools.com/html/html_responsive.asp

## Tugas Individu 5

**1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**
Javascript bermanfaat untuk menjadikan halaman website menjadi lebih dinamis. Browser akan merespon request pengguna dan mengelola tata letak konten pada halaman website sesuai device pengguna.

**2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**
Fungsi `await`dapat memudahkan pengimplementasian AJAX tanpa perlu menggunakan library eksternal. Penggunaannya adalah menunggu hasil fungsi `async`yang menandai fungsi sebagai fungsi yang dapat mengembalikan nilai secara *asyncronus.* Tanpa await, promise yang dihasilkan kemungkinan dapat berupa hasil fetch yang belum selesai.

**3. Mengapa kita perlu menggunakan *decorator***  `csrf_exempt` **pada *view* yang akan digunakan untuk AJAX `POST`?**
`csrf_exempt` dapat membuat Django tidak perlu mengecek  `csrf_token` pada POST request.

**4. Pada tutorial PBP minggu ini, pembersihan data *input* pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?**
Frontend biasanya membantu ux website bagi pengguna. Pada frontend keamanan data sangat krusial, karena memungkinkan orang berniat jahat untuk memanipulasi input data. Adanya celah keamanan ini biasa disebut *Cross Site Scripting* (XSS). Sehingga sebagai pertahanan kita menggunakan backend untuk melakukan pembersihan input data dan memvalidasinya.

**5. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!**
Pertama adalah membuat fungsi pada [views.py] untuk menambahkan produk dan buat fungsi javascript addproduct yang menggunakan AJAX. Lalu lakukan routing path fungsi tersebut. Kemudian, manfaatkan fetch() API untuk mengambil data yang sudah di filter agar milik pengguna yang *logged in* yang datanya ditampilkan. Setelah itu, buat fungsi untuk refreshproduct, modal untuk merefresh data product yang diinput.
Selanjutnya membersihkan data input sebelumnya dan menutup celah keamanan dengan menggunakan strip_tags pada method add di [views.py] dan method clean di form.py. 

**Referensi**: 
Amazon. (n.d.). *Apa Itu JavaScript (JS)?* Retrieved October 7, 2024, from https://aws.amazon.com/id/what-is/javascript/#:~:text=JavaScript muncul sebagai teknologi sisi,letak konten di halaman web.
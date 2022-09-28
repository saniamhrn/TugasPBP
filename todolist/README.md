
# Tugas 4 PBP

#### 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
   Untuk memvalidasi permintaan dari user dan akan menolak permintaan tersebut apabia CSRF token tidak valid. Ketika ada permintaan dari user yang memerlukan validasi maka server harus memverifikasi permintaan tersebut menyertakan token yang cocok dengan nilai yang disimpan di sisi user. Jika permintaan tidak memiliki token yang cocok, maka permintaan akan ditolak. Apabila tidak terdapat potongan kode {% csrf_token %} pada elemen <form> maka kemungkinan akan mudah terkena CSRF karena tidak ada yang memverifikasi permintaan user

#### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
   Bisa dengan merender setiap field secara manual memakai for loop

#### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


#### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
   * membuat aplikasi baru dengan `python manage.py startapp todolist`
   * membuat fungsi di `views.py` kemudian routing dengan menambahkan kode di `urls.py`
      ```
      urlpatterns = [
               path('', show_todolist, name='show_todolist'),
      ]
      ```
   * Daftarkan aplikasi `todolist` ke dalam `urls.py` yang ada pada folder project_django dengan menambahkan potongan kode pada variabel `urlpatterns`
      ```
      ...
      path('todolist/', include('todolist.urls')),
      ...
      ```
   * menambahkan model `Task` di `models.py` kemudian di-migrate dengan cara `python manage.py makemigrations` lalu `python manage.py migrate`
   * membuat form registrasi, login, dan logout dengan langkah seperti di lab 3
   * membuat form addtask dengan langkah seperti membuat form registrasi
   * routing untuk dapat mengakses url
      ```
      urlpatterns = [
         ...
         path('register/', register name='register'),
         path('login/', login_user, name='login'),
         path('logout/', logout_user, name='logout'),
         path('addtask/', add_task, name='addtask'),
         ...
      ]
      
      ```
   * deploy ke heroku dengan add, commit, dan push ke github dan kemudian nanti github akan mendeploy ke heroku
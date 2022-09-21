Link aplikasi Heroku:

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
ans : ketika ada request URL masuk, django akan menerima URL lalu mengecek urls.py dan memanggil views yang cocok dengan URL.
Kemudian views.py akan mengecek models yang cocok dan mengimpornya dari models.py.
Setelah itu, views.py mengirim data ke folder template yang berisi berkas html. Data dan berkas html ini nantinya akan dikirim kembali ke browser

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
ans : virtual environment digunakan untuk menjalankan project yang memiliki kebutuhan/dependencies yang berbeda-beda. Kita dapat mengerjakan beberapa aplikasi atau project dengan modul yang sama namun dengan versi yang berbeda. Apabila tidak menggunakan virtual environment bisa saja aplikasi yang baru dibuat tidak dapat berjalan di modul dengan versi baru

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
ans : 
1. untuk mengambil data dari model menggunakan 
        from katalog.models import CatalogItem
        yaitu mengimport CatalogItem dari models
   untuk mengembalikan ke dalam sebuah HTML menggunakan fungsi
        def show_katalog(request):
        data_barang_katalog = CatalogItem.objects.all()
        context = {
                'list_katalog': data_barang_katalog,
                'nama': 'Sania Rizqi Maharani',
                'student_id': '2006597001'
        }
        return render(request, "katalog.html", context)

2. melakukan routing terhadap fungsi di views dengan cara mengisi urls.py dengan 
        from django.urls import path
        from katalog.views import show_katalog

        app_name = 'katalog'

        urlpatterns = [
                path('', show_katalog, name='show_katalog'),
        ]
dan mendaftarkan aplikasi katalog ke dalam urls.py di dalam folder project_django dengan menambahkan potongan kode pada variabel urlpatterns
        path('katalog/', include('katalog.urls')),

3. membuat table yang berisi list_katalog, mendaftarkan CatalogItem ke admin.py

4. 

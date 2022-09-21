
# Tugas 3 PBP

#### 1. Jelaskan perbedaan antara JSON, XML, dan HTML! 
   HTML hanya untuk menyajikan data, sedangkan JSON dan XML dapat digunakan untuk transfer informasi. Data XML disimpan sebagai tree structure sedangkan data JSON disimpan seperti map dengan pasangan kev dan value. JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.

#### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? ####
   Dengan menggunakan data delivery kita dapat menstandarisasi data-data yang akan diteruskan dari satu komputer ke komputer lain 

#### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. #### 
   * membuat aplikasi baru dengan `python manage.py startapp mywatchlist`
   * membuat fungsi di `views.py` kemudian routing dengan menambahkan kode di `urls.py`
      ```
      urlpatterns = [
               path('', show_mywatchlist, name='show_mywatchlist'),
      ]
      ```
   * Daftarkan aplikasi `mywatchlist` ke dalam `urls.py` yang ada pada folder project_django dengan menambahkan potongan kode pada variabel `urlpatterns`
      ```
      ...
      path('mywatchlist/', include('mywatchlist.urls')),
      ...
      ```
   * menambahkan model di `models.py` kemudian di-migrate dengan cara `python manage.py makemigrations` lalu `python manage.py migrate`
   * menambahkan 10 data untuk objek `MyWatchList` dengan menggunakan `django admin`
   * menyajikan data dengan format html, xml dan json dengan membuat fungsi di `views.py` sebagai berikut
      ```
      def show_mywatchlist(request):
        data_watchlist = MyWatchList.objects.all()
        context = {
                'daftar_watchlist' : data_watchlist,
                'nama': 'Sania Rizqi Maharani',
                'student_id': '2006597001'
        }
        return render(request, "mywatchlist.html", context)

      def show_xml_mywatchlist(request):
            data_xml = MyWatchList.objects.all()
            return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

      def show_json_mywatchlist(request):
            data_json = MyWatchList.objects.all()
            return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")
      ```
   * routing untuk dapat mengakses url dalam format html, xml, dan json
      ```
      urlpatterns = [
         ...
         path('xml/', show_xml_mywatchlist, name='show_xml_mywatchlist'),
         path('json/', show_json_mywatchlist, name='show_json_mywatchlist'),
         ...
      ]
      
      ```
   * deploy ke heroku dengan add, commit, dan push ke github dan kemudian nanti github akan mendeploy ke heroku

#### Akses di postman

<img width="709" alt="Screen Shot 2022-09-21 at 22 57 30" src="https://user-images.githubusercontent.com/71616521/191582880-abe5843e-6d6e-406f-8d6f-3bb8cf2acca5.png">
<img width="709" alt="Screen Shot 2022-09-21 at 22 58 13" src="https://user-images.githubusercontent.com/71616521/191582979-23679566-81b6-4dc1-a685-88df8db778fa.png">
<img width="709" alt="Screen Shot 2022-09-21 at 22 58 24" src="https://user-images.githubusercontent.com/71616521/191582996-0ffbd2b1-8040-48f7-ab17-fb64aa8cdb4f.png">


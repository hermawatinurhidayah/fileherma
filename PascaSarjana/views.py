from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Imu Komunikasi", "Magister Managemen", "Magister Teknik Kimia", "Magister Pendidikan Bahasa Indonesia", "Magister Pendidikan Bahasa Inggris", "Magister Pendidikan Matematika", "Magister Teknologi Pendidikan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexpascasarjana.html', konteks)

from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["Kedokteran", "Sarjana Keperawatan", "Diploma Keperawatan", "Sarjana Gizi", "Ilmu Keolahragaan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfk.html', konteks)
from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judul = ["Teknik Elektro", "Teknik Industri", "Teknik Kimia", "Teknik Mesin", "Teknik Metalurgi", "Teknik Sipil"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexft.html', konteks)
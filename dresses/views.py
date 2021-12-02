from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


from dresses.models import kurta, kurtaset, saree, top, jewellery, handbag


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contactus(request):
    return render(request, 'contactus.html')

def myaccount(request):
    return render(request, 'myaccount.html')

def service(request):
    return render(request, 'service.html')

def shop(request):
    return render(request, 'shop.html')

def shopdetail(request):
    return render(request, 'shopdetail.html')

def wishlist(request):
    return render(request, 'wish_list.html')

def kurtas(request):
    k = kurta.objects.all()
    return render(request, 'kurtacategory.html', {'ob': k})

def kurtasets(request):
    ks = kurtaset.objects.all()
    return render(request, 'kurtasetcategory.html', {'ob': ks})
def sarees(request):
    s = saree.objects.all()
    return render(request, 'sareecategory.html', {'ob': s})

def tops(request):
    t = top.objects.all()
    return render(request, 'topcategory.html', {'ob': t})

def jewellerys(request):
    j = jewellery.objects.all()
    return render(request, 'jewellerycategory.html', {'ob': j})

def handbags(request):
    h = handbag.objects.all()
    return render(request, 'handbagcategory.html', {'ob': h})

def kurtadetails(request, pk):
    obj = kurta.objects.get(id=pk)
    return render(request, 'kurtadetail.html', {'ob': obj})

def kurtasetdetails(request,pk):
    obj = kurtaset.objects.get(id=pk)
    return render(request, 'kurtasetdetail.html', {'ob':obj})

def sareedetails(request, pk):
    obj = saree.objects.get(id=pk)
    return render(request, 'sareedetail.html', {'ob':obj})

def topdetails(request, pk):
    obj = top.objects.get(id=pk)
    return render(request, 'topdetail.html', {'ob':obj})

def handbagdetails(request, pk):
    obj = handbag.objects.get(id=pk)
    return render(request, 'handbagdetail.html', {'ob':obj})

def jewellerydetails(request, pk):
    obj = jewellery.objects.get(id=pk)
    return render(request, 'jewellerydetail.html', {'ob':obj})

def booking(request):
    if request.method=='GET':
        return render(request, 'booking.html')
    else:
        subject = 'RM BOUTIQUE'
        message = 'Your Item Has Been Booked Successfully '
        recipient = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        return HttpResponse("Email send successfully")

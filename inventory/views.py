from django.shortcuts import render

def home(request):
    return render(request,template_name='inventory\home.html')



def products(request):
    return render(request, template_name='inventory\products.html')
def products_details(request):
    return render(request,template_name='inventory\products_details.html')



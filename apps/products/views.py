from django.shortcuts import render, redirect
from .models import Product

def create_product(request):
   if request.method == 'POST':
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        description = request.POST.get('description')
        category = request.POST.get('category')
        #sizes = request.POST.get('size')
        image = request.FILES.get('image')  # Capturando la imagen
        price = request.POST.get('price')

        # Guarda el producto
        product = Product(
            name=name,
            weight=weight,
            description=description,
            category=category,
           # size=sizes,
            image=image,
            price=price
        )
        product.save()
        return redirect('/default/')  # Cambia 'success_url' por la URL a donde quieras redirigir
   return render(request, 'pages/ecommerce/products/new-product.html')

def product_list(request):
    # Obtiene todos los productos
    products = Product.objects.all()  
    
    # Define el contexto
    context = {
        'parent': 'ecommerce',
        'sub_parent': 'products',
        'segment': 'product_list',
        'products': products  # Agrega los productos al contexto
    }
    
    # Renderiza la plantilla con el contexto
    return render(request, 'pages/ecommerce/products/products-list.html', context)

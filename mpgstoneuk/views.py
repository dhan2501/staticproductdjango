from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from mpgstoneuk.models import Product, Category, MenuItem, ProductComment
from django.core.paginator import Paginator
# from .models import ProductComment
from .forms import ProductCommentForm
from django.urls import reverse
# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'core/frontpage.html', {'products':products, 'title': 'My Dynamic Page Title'})


def home(request):
    menu_items = MenuItem.objects.filter(is_active=True, parent__isnull=True)



    return render(request, 'core/base.html', {'menu_items': menu_items})

def shop(request, category_slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    if category_slug:
        # Filter products by the selected category
        category = get_object_or_404(Category, slug=category_slug)
        products = category.product.all()
    else:
        # Show all products if no category is selected
        products = Product.objects.all()

    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))


    paginator = Paginator(products, 2)  # Show 10 products per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products':products, 
        'categories':categories,
        'active_category' : active_category,
        'page_obj': page_obj,
    }
    return render(request, 'core/shop.html',  context)

def product(request):
    products = Product.objects.all()[0:8]
    return render(request, 'core/shop.html', {'products':products})

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'core/product_detail.html', {'product': product})

def product_detail(request, category_slug, product_slug):
    # products = Product.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, category=category, slug=product_slug)

    # product = get_object_or_404(Product, id=product_id)  # Assuming a Product model exists
    comments = ProductComment.objects.filter(product=product).order_by('-created_at')  # Adjust to associate with the product
    if request.method == "POST":
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product  # Associate with the product
            comment.save()
            reverse('product_detail', kwargs={
    'category_slug': product.category.slug,
    'product_slug': product.slug,
})
    else:
        form = ProductCommentForm()

    # return render(request, 'core/product_detail.html', {'product': product, 'comments': comments, 'form': form})


    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Products', 'url': '/shop/'},
        {'name': category.category_name, 'url': f'/categories/{category.slug}/'},
        {'name': product.name, 'url': None},  # Current product, no link 
    ]
    return render(request, 'core/product_detail.html', {'product': product, 'category': category, 'breadcrumbs': breadcrumbs, 'comments': comments, 'form': form})
# Category Page
def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product.all()  # Get all products in this category
    categories = Category.objects.all()
    return render(request, 'core/category_detail.html', {'category': category, 'products': products, 'categories':categories})


def aboutus(request):
    return render(request, 'core/aboutus.html')



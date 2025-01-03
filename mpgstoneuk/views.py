from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from mpgstoneuk.models import Product, Category, MenuItem, ProductComment, PagesTitle, Blog, BlogCategory
from django.core.paginator import Paginator
# from .models import ProductComment
from .forms import ProductCommentForm
from django.urls import reverse
# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]
    context = {
        'title': 'Home Page',
        'meta_title': 'Home',
        'meta_description': 'Contact us for more information or support.',
        'products':products, 
        'title': 'My Dynamic Page Title'
    }
    return render(request, 'core/frontpage.html', context)


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
    breadcrumbs = [
        {'title': 'Home', 'url': '/'},
        {'title': 'Shop', 'url': '/shop/'},  # Link to the Shop page
    ]
    context = {
        'products':products, 
        'categories':categories,
        'active_category' : active_category,
        'page_obj': page_obj,
        'title': 'Shop',
        'meta_title': 'Shop',
        'meta_description': 'Contact us for more information or support.',
        'breadcrumbs' :breadcrumbs
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


    
    return render(request, 'core/product_detail.html', {'product': product, 'category': category, 'breadcrumbs': breadcrumbs, 'comments': comments, 'form': form, 'meta_title': product.meta_title if product.meta_title else product.name,
        'meta_description': product.meta_description if product.meta_description else product.description[:150],})
# Category Page
def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product.all()  # Get all products in this category
    categories = Category.objects.all()
    paginator = Paginator(products, 2)  # Show 10 products per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # context = {
    #     'title': 'About Us',
    #     'meta_title': 'About Us',
    #     'meta_description': 'Contact us for more information or support.',
    #     'category': category, 
    #     'products': products, 
    #     'categories':categories
    # }
    # return render(request, 'core/category_detail.html', {'category': category, 'products': products, 'categories':categories})

    context = {
        'category': category, 
        'page_obj': page_obj,
        'products': products, 
        'categories':categories, 
        # 'meta_title': category.meta_title if category.meta_title else category.category_name,
        'meta_title': category.meta_title if category.meta_title else None,
        'meta_description': category.meta_description if category.meta_description else None,
    }
    return render(request, 'core/category_detail.html', context)


def aboutus(request):
    breadcrumbs = [
        {'title': 'Home', 'url': '/'},
        {'title': 'About Us', 'url': '/about-us/'},  # Link to the Shop page
    ]
    context = {
        'breadcrumbs' : breadcrumbs,
        'title': 'About Us',
        'meta_title': 'About Us',
        'meta_description': 'Contact us for more information or support.',
    }
    
    return render(request, 'core/aboutus.html', context)


def dynamic_page(request, slug):
    # page = get_object_or_404(PagesTitle, slug=slug)
    # return render(request, 'core/base.html', {
    #     'title': page.title,
    #     'meta_title': page.meta_title if page.meta_title else page.title,
    #     'meta_description': page.meta_description,
    #     'content': page.content,
    # })

    page = get_object_or_404(PagesTitle, slug=slug)
    return render(request, 'core/base.html', {'title': page.title, 'content': page.content})

def contactus(request):
    return render(request, 'core/contactus.html')


# def blogpage(request):
#     return render(request, 'core/blog.html')


def blogpage(request):
    blogs = Blog.objects.all().order_by('-date_posted')
    return render(request, 'core/blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    # Increment total views
    blog.total_views += 1
    blog.save()
    return render(request, 'core/blog_detail.html', {'blog': blog})
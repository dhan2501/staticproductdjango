from .models import Logo, MenuItem, Category, SocialMediaLink

def site_logo(request):
    logo = Logo.objects.first()  # Fetch the first logo
    return {'logo': logo}

def dynamic_menu(request):
    menu_items = MenuItem.objects.filter(is_active=True, parent__isnull=True)
    return {'menu_items': menu_items}

def active_categories(request):
    categories = Category.objects.filter(is_active=True)
    return {'categories': categories}


def menu_processor(request):
    header_menu = MenuItem.objects.filter(position__in=['header', 'both'], is_active=True)
    footer_menu = MenuItem.objects.filter(position__in=['footer', 'both'], is_active=True)
    return {
        'header_menu': header_menu,
        'footer_menu': footer_menu,
    }

def social_media_links(request):
    header_links = SocialMediaLink.objects.filter(location__in=['header', 'both'], is_active=True)
    footer_links = SocialMediaLink.objects.filter(location__in=['footer', 'both'], is_active=True)
    return {
        'header_social_media_links': header_links,
        'footer_social_media_links': footer_links,
    }
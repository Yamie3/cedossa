from django.conf import settings


def site_info(request):
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'Cedossa'),
        'site_domain': getattr(settings, 'SITE_DOMAIN', 'cedossa.org'),
        'facebook_page_url': getattr(settings, 'FACEBOOK_PAGE_URL', ''),
    }

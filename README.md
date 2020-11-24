# Django-Tinyblog

Tinyblog is Django application for tiny blog

## Quick Start

1. Add "tinyblog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'tinyblog',
    ]

2. Include the tinyblog URLconf in your project urls.py like this::

    path('blog/', include('tinyblog.urls')),

3. Run ``python manage.py migrate`` to create the tinyblog models.

4. Visit http://127.0.0.1:8000/blog/ to use blog.

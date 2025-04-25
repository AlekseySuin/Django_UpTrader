from django import template
from django.urls import resolve, Resolver404
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info

    try:
        resolved_url = resolve(current_url)
        resolved_url_name = resolved_url.url_name
    except Resolver404:
        resolved_url_name = None

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    # Здесь нужно преобразовать плоский список в дерево и определить активные элементы
    # Это ключевая часть логики, которая требует отдельной реализации

    return {
        'menu_tree': menu_tree,  # Здесь будет древовидная структура
        'current_url': current_url,
        'resolved_url_name': resolved_url_name,
    }
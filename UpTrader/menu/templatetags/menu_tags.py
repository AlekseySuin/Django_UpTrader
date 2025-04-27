from django import template
from django.urls import resolve, Resolver404
from ..models import MenuItem
from ..utils import build_menu_tree

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    print(f"Trying to draw menu: {menu_name}")  # Проверка в консоли
    request = context['request']
    current_url = request.path_info

    expanded_ids = set()
    for exp_id in request.GET.getlist('expanded'):
        if exp_id.isdigit():
            expanded_ids.add(int(exp_id))

    try:
        resolved_url = resolve(current_url)
        resolved_url_name = resolved_url.url_name
    except Resolver404:
        resolved_url_name = None

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    menu_tree = build_menu_tree(menu_items, current_url, expanded_ids)

    return {
        'menu_tree': menu_tree,
        'request': request,
        'current_url': current_url,
    }
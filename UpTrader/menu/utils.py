def build_menu_tree(menu_items, current_url, expanded_ids):
    items_map = {item.id: {'item': item, 'children': [], 'is_active': False} for item in menu_items}
    root_items = []
    active_item = None

    # Строим иерархию
    for item in menu_items:
        if item.parent_id is None:
            root_items.append(items_map[item.id])
        else:
            parent = items_map.get(item.parent_id)
            if parent:
                parent['children'].append(items_map[item.id])

    # Первый проход: определяем активные элементы
    for item_id in items_map:
        item = items_map[item_id]['item']
        if item.get_url() == current_url:
            items_map[item_id]['is_active'] = True
            active_item = item

    # Второй проход: помечаем активных родителей
    if active_item:
        # Добавляем родителей активного элемента
        parent = active_item.parent
        while parent:
            expanded_ids.add(parent.id)
            parent = parent.parent

        # Добавляем детей активного элемента (первый уровень)
        for child in items_map.get(active_item.id, {}).get('children', []):
            expanded_ids.add(child['item'].id)

        # Применяем развернутые состояния
    for item_id in items_map:
        items_map[item_id]['is_expanded'] = item_id in expanded_ids

    return root_items
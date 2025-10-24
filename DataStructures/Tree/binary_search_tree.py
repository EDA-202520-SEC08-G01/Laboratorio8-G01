from DataStructures.Tree import bst_node as bsn
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll


def new_map():
    
    retorno = {
        "root": None
    }
    
    return retorno

def insert_node(root, key, value):
    if root is None:
        return bsn.new_node(key, value)
    if key < bsn.get_key(root):
        root["left"] = insert_node(root["left"], key, value)
    elif key > bsn.get_key(root):
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value  
    
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def get(my_bst, key):
    current = my_bst["root"]
    res = get_node(current, key)
    res = bsn.get_value(res)
    return res

def get_node(node, key):
    if node == None:
        return None
    elif key < bsn.get_key(node):
        return get_node(node["left"], key)
    elif key > bsn.get_key(node):
        return get_node(node["right"], key)
    elif node["key"] == key:
        return node

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def size(my_bst):
    return size_tree(my_bst["root"])

def contains(my_bst, key):
    return get(my_bst, key) is not None

def is_empty(my_bst):
    return size(my_bst) == 0

def key_set_tree(root, keys):
    retorno = sll.new_list()
    if root is not None:
        key_set_tree(root["left"], keys)
        sll.add_last(retorno, bsn.get_key(root))
        key_set_tree(root["right"], keys)
    return retorno

def key_set(my_bst):
    keys = sll.new_list()
    key_set_tree(my_bst["root"], keys)
    return keys

def value_set_tree(root, values):
    retorno = sll.new_list()
    if root is not None:
        value_set_tree(root["left"], values)
        sll.add_last(retorno, bsn.get_value(root))
        value_set_tree(root["right"], values)
    return retorno

def value_set(my_bst):
    values = sll.new_list()
    value_set_tree(my_bst["root"], values)
    return values

def keys_range(root, low_key, high_key, keys):
    if root is None:
        return
    current_key = bsn.get_key(root)
    if low_key < current_key:
        keys_range(root["left"], low_key, high_key, keys)
    if low_key <= current_key <= high_key:
        sll.add_last(keys, current_key)
    if current_key < high_key:
        keys_range(root["right"], low_key, high_key, keys)

def keys(my_bst, low_key, high_key):
    keys_list = sll.new_list()
    keys_range(my_bst["root"], low_key, high_key, keys_list)
    return keys_list

def remove(my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst

def remove_node(node, key):
    if node == None:
        return node
    
    replace = None
    key_node = bsn.get_key(node)

    if key_node > key:
        node["left"] = remove_node(node["left"], key)
        return node
    elif key_node < key:
        node["right"] = remove_node(node["right"], key)
        return node
    elif key_node == key:
        if node["right"] is None and node["left"] is not None:
            replace = get_min_node(node["left"])
        if node["right"] is not None:
            replace = get_min_node(node["right"])
        if replace is not None:
            replace = get_node(node, replace)
        node = replace
        return node
    
def get_min(my_bst):
    resultado = get_min_node(my_bst["root"])
    return resultado

def get_min_node(node):
    if node is None:
        return None
    if node["left"] == None:
        return node["key"]
    return get_min_node(node["left"])

def height_tree(root):
    if root is None:
        return 0
    left_height = height_tree(root["left"])
    right_height = height_tree(root["right"])
    return 1 + max(left_height, right_height)

def height(my_bst):
    return height_tree(my_bst["root"])

def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["key"]
    return get_max_node(root["right"])

def get_max(my_bst):
    return get_max_node(my_bst["root"])


def values_range(root, key_initial, key_final, list_values):
    if root is None:
        return
    current_key = bsn.get_key(root)
    if key_initial < current_key:
        values_range(root["left"], key_initial, key_final, list_values)
    if key_initial <= current_key <= key_final:
        sll.add_last(list_values, bsn.get_value(root))
    if current_key < key_final:
        values_range(root["right"], key_initial, key_final, list_values)

def values(my_bst, key_initial, key_final):
    list_values = sll.new_list()
    values_range(my_bst["root"], key_initial, key_final, list_values)
    return list_values

def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    return root

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    return root

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

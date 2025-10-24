from DataStructures.Tree import rbt_node as rbn

def new_map():
    my_map = {}
    my_map["root"] = None
    my_map["type"] = "RBT"
    return my_map

def default_compare(key1, key2):
    if key1 < key2:
        return -1
    elif key1 > key2:
        return 1
    else:
        return 0
    
def rotate_left(node):
    if node is None or node["right"] is None:
        return node
    
    new_root = node["right"]
    node["right"] = new_root["left"]
    new_root["left"] = node
    return new_root

def rotate_right(node):
    if node is None or node["left"] is None:
        return node
    
    new_root = node["left"]
    node["left"] = new_root["right"]
    new_root["right"] = node
    return new_root

def flip_colors(node):
    if node is None:
        return
    node["color"] = rbn.RED
    if node["left"]:
        node["left"]["color"] = rbn.BLACK
    if node["right"]:
        node["right"]["color"] = rbn.BLACK
        
def flip_node_color(node):
    if node is None:
        return
    if node["color"] == rbn.RED:
        node["color"] = rbn.BLACK
    else:
        node["color"] = rbn.RED
        
def is_red(node):
    if node is None:
        return False
    return node["color"] == rbn.RED

def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def insert_node(root, key, value):
    if root is None:
        return rbn.new_rbt_node(key, value, rbn.RED)
    
    cmp = default_compare(key, root["key"])
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    my_rbt["root"]["color"] = rbn.BLACK
    
    return my_rbt


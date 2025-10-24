from DataStructures.Tree import rbt_node as rbn

def new_map():
    my_map = {}
    my_map["root"] = None
    my_map["type"] = "RBT"
    return my_map

def default_compare(key, element):
    if key == rbn.get_key(element):    
        return 0
    elif key > rbn.get_key(element):
        return 1
    else:
        return -1
    
def rotate_left(node_rbt):
    node1 = node_rbt["right"]
    l_node1 = node1["left"]
    l_rbt   = node_rbt["left"]
    node_rbt["left"] = node_rbt
    node_rbt = node1
    node_rbt["left"]["right"] = l_node1
    node_rbt["left"]["left"] = l_rbt

    rbn.change_color(node_rbt["left"], 0)
    rbn.change_color(node_rbt["right"], 0)
    rbn.change_color(node_rbt["left"], 1)

    return node_rbt


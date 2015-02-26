# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def gen_children_nodes(children_issues):
    children_nodes = []
    for child_issue in children_issues:
        id = child_issue['id']
        subject = child_issue['subject']
        child_node = Node("[%d] %s" % (id, subject))

        children_nodes.append(child_node)
        if 'children' in child_issue:
            child_node.children = gen_children_nodes(child_issue['children'])
    return children_nodes


def show_subtask_tree(children_issues):
    main_node = Node('')
    main_node.children = gen_children_nodes(children_issues)

    return show(main_node)


def show(node, seq_is_last_child = []):
    ret = ""
    if seq_is_last_child:
        for b in seq_is_last_child[:-1]:
            if b:
                ret += u"   "
            else:
                ret += u"│  "
        if seq_is_last_child[-1]:
            ret += u"└── "
        else:
            ret += u"├── "
    ret = ret + node.value
    for idx, c in enumerate(node.children):
        ret = ret + u"\n" + show(c, seq_is_last_child + [idx == len(node.children)-1])
    return ret


"""
-- ID ПОСЫЛКИ - 52257676 --

-- ПРИНЦИП РАБОТЫ --
Алгоритм работает по принципу, изложенному в материалах практикума.
Сперва проверяем - передан ли в качестве корня дерева объект Node. Если нет - возвращаем None.
Потом ищем узел для удаления. Если узел с переданным значением не найден - возвращаем корень дерева.
Если переданное значение найдено в переданном корне дерева, и у корня нет ветвей - значит дерева больше нет, возвращаем None.
Далее ищем подходящую замену - либо крайний правый узел в левом потомке удаляемого узла, либо крайний левый в правом потомке.
Далее заменяем в родительком узле удаляемого элемента ссылку на удаляемый элемент на найденную замену
(замена может быть не найдена, если потомков у удаляемого узла нет - тогда просто заменим на None).
Если замены все таки не было, то на этом все - можно вернуть корень дерева.
Если замена есть - передадим ее дочерний узел ее родителю.
Далее передадим дочерние узлы удаляемого нода заменяющему.
Далее проверим, не удалили ли мы корень дерева. Если удалили - заменим возвращаемое значение корня на нод замены.
Возвращаем корень дерева.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Мы ищем элемент для замены за O(H), где H это высота дерева, если дерево сбалансировано.
Или в худшем случае за O(n), где n это количество вершин, если у каждой вершины один ребенок.
Поиск замены для удаления производится по такой же схеме: O(H) или O(n).
Все замены мы производим за константное время.
Итого общая сложность 2 * O(H) -> O(H) в случае, если дерево сбалансированно;
или 2 * O(n) -> O(n), если не сбалансированно.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Понадобится O(1) доп. памяти.
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def find_node(root, key, parent=None):
    if root is None:
        return None, None
    if root.value == key:
        return root, parent
    if root.value > key:
        return find_node(root.left, key, root)
    else:
        return find_node(root.right, key, root)


def find_substitute(node):
    if node.left:
        parent = node
        node = node.left
        while node.right:
            parent = node
            node = node.right

    elif node.right:
        parent = node
        node = node.right
        while node.left:
            parent = node
            node = node.left

    else:
        node = parent = None

    return node, parent


def replace_child(parent, prev_child, new_child):
    if parent is None or prev_child is None:
        return
    if parent.left and parent.left.value == prev_child.value:
        parent.left = new_child
    elif parent.right and parent.right.value == prev_child.value:
        parent.right = new_child


def reconnect_bounds(parent, node):
    if node.left:
        replace_child(parent, node, node.left)
    elif node.right:
        replace_child(parent, node, node.right)
    else:
        replace_child(parent, node, None)


def is_single_node(node, parent):
    return parent is None and node.left is None and node.right is None


def remove(root, key):
    if root is None:
        return None

    removed, removed_parent = find_node(root, key)

    # If node with searched key wasn't found
    if not removed:
        return root

    # If root without leaves was removed
    if is_single_node(removed, removed_parent):
        return None

    substitute, substitute_parent = find_substitute(removed)

    replace_child(removed_parent, removed, substitute)

    if not substitute:
        return root

    reconnect_bounds(substitute_parent, substitute)

    substitute.left = removed.left
    substitute.right = removed.right

    # If root node was removed
    if not removed_parent:
        root = substitute

    return root
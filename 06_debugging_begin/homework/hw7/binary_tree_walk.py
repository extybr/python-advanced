"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")

counter = itertools.count(random.randint(1, 10 ** 6))


@dataclass
class BinaryTreeNode:
    value: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.value}]>"

    def __getitem__(self, item):
        match item:
            case self.left:
                return self.left
            case self.right:
                return self.right
            case self.value:
                return self.value


def walk(_root: BinaryTreeNode):
    queue = deque([_root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


NODE: {int: BinaryTreeNode} = {}

class Line:
    info: str = "INFO"
    debug: str = "DEBUG"
    tree: str = '<BinaryTreeNode['
    left: str = 'left'
    right: str = 'right'


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    with open(path_to_log_file, 'r', encoding='utf-8') as log:
        for line in log:
            part = line.strip().split(Line.tree)
            match line.split(':')[0]:
                case Line.info:
                    root = BinaryTreeNode(int(part[1][:-2]))
                    NODE[root.value] = root
                case Line.debug:
                    match part[1].split()[1]:
                        case Line.left:
                            root.left = BinaryTreeNode(int(part[2][:-15]))
                            NODE[root.left.value] = root.left
                        case Line.right:
                            root.right = BinaryTreeNode(int(part[2][:-15]))
                            NODE[root.right.value] = root.right
    for first in NODE:
        return NODE[first]


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )
    # root = get_tree(7)
    # walk(root)
    restore = restore_tree('walk_log_3.txt')
    for i in NODE:
        print(NODE[i].__dict__)
    print("Вершина:", restore.value)
    # number = random.choice([i for i in NODE.keys()])
    number = 758124
    print(BinaryTreeNode(number))
    BinaryTreeNode = NODE
    print(BinaryTreeNode[number].left)
    print(BinaryTreeNode[number].right)
    print(BinaryTreeNode)

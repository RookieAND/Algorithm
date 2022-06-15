import sys

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


read = sys.stdin.readline
N = int(read())
tree = {}

# 각 노드에 대한 정보를 입력 받고, Node 객체를 생성하여 트리에 저장.
# left_node 는 해당 트리의 좌측 자식 노드의 값, right 노드는 반대.
for i in range(N):
    data, left_node, right_node = read().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

def pre_order(node):
    print(node.data, end='')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end='')

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
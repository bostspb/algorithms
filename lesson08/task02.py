"""
Задача №2
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'\n[v:{self.value}\nl:{self.left}\nr:{self.right}]'


def get_huffman_tree(msg):
    counter = Counter(msg)

    if len(counter) == 0:
        return {Node(None): 1}
    elif len(counter) == 1:
        node = Node(None)
        node.left = Node([key for key in counter][0])
        return {node: 1}

    while len(counter) > 1:
        couple = counter.most_common()[:-3:-1]
        node = Node(None)

        if isinstance(couple[0][0], str):
            node.left = Node(couple[0][0])
        else:
            node.left = couple[0][0]

        if isinstance(couple[1][0], str):
            node.right = Node(couple[1][0])
        else:
            node.right = couple[1][0]

        counter[node] = couple[0][1] + couple[1][1]
        del counter[couple[0][0]]
        del counter[couple[1][0]]

    return [key for key in counter][0]


def get_chars_dictionary(root, chars=dict(), code=''):
    if root is None:
        return None
    if isinstance(root.value, str):
        chars[root.value] = code
        return chars
    get_chars_dictionary(root.left, chars, code + '0')
    get_chars_dictionary(root.right, chars, code + '1')
    return chars


def encode_message(dictionary, msg):
    encoded_message = ''
    for char in msg:
        encoded_message += dictionary[char] + ' '
    return encoded_message


if __name__ == '__main__':
    message = 'beep boop beer!'
    tree = get_huffman_tree(message)
    chars_dictionary = get_chars_dictionary(tree)
    compressed_message = encode_message(chars_dictionary, message)
    print(compressed_message)

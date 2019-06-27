node_1 = {'val': 5, 'left': None, 'right': None}
node_2 = {'val': 2, 'left': None, 'right': None}
node_3 = {'val': 1, 'left': None, 'right': None}
node_4 = {'val': 3, 'left': node_3, 'right': None}
node_5 = {'val': 4, 'left': node_2, 'right': node_1}
root = {'val': 2, 'left': node_4, 'right': node_5}

from collections import deque

q = deque()


def bfs(root):
    if root is None:
        return
    curr_level = 1
    root['level'] = curr_level
    q.appendleft(root)
    while len(q) > 0:
        _node = q.pop()
        if _node['level'] > curr_level:
            print('\n', end='')
            curr_level += 1
        print(_node['val'], end='')
        if _node['left']:
            _node['left']['level'] = _node['level'] + 1
            q.appendleft(_node['left'])
        if _node['right']:
            _node['right']['level'] = _node['level'] + 1
            q.appendleft(_node['right'])


bfs(root)

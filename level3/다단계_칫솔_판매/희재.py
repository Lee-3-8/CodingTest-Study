def make_tree(enroll, referral):
    tree = {'-': {'pay': 0, 'parent': None}}
    for enr, ref in zip(enroll, referral):
        tree[enr] = {'pay': 0, 'parent': ref}
    return tree

def piramid(tree, node, amount):
    if not amount:
        return 
    amount_10 = amount // 10
    tree[node]['pay'] += amount - amount_10
    if tree[node]['parent']:
        piramid(tree, tree[node]['parent'], amount_10)
    else:
        tree[node]['pay'] += amount_10

def solution(enroll, referral, seller, amount):
    tree = make_tree(enroll, referral)
    for node, amount in zip(seller, amount):
        piramid(tree, node, amount * 100)
    return [tree[i]['pay'] for i in enroll]
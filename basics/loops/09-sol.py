items = ['apple', 'banana', 'apple', 'mango', 'pineapple']

unq_items = set()
for item in items:
    if item in unq_items:
        print('Duplicate', item)
        break
    unq_items.add(item)
# lecture sol
# add, set methods implementation
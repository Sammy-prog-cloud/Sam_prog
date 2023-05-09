import math

word = ["cat", "defenestrate", "window"]
for w in word:
    print(w, len(w))

users = {'Hans': 'active', 'Eleonore': 'inactive', 'Mary': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(active_users)

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print(a[1][0])
print(a[0][1])
print(a[1][2])

# instead of the using the above, it is better to use the enumerate() function as in below:
for i, v in enumerate(['Tic', 'Tac', 'Toe']):
    print(i, v)


# Using the zip function to get two values together
question = ['name', 'quest', 'favorite - color']
answer = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answer):
    print('What is your {0}? It is {1}'.format(q, a))


# To reverse set of numbers, we use the reversed() function
for i in reversed(range(1, 10, 2)):
    print(i, end='   ')

# Using the sorted function, we sort out the list of items
basket = ['Apple', 'Banana', 'Pineapple', 'Pear', 'Orange', 'Apple']
for i in sorted(basket):
    print("\n", i, end='  ')

# Using the set() function with the sorted() function to eliminate duplicates in a list
for i in sorted(set(basket)):
    print("\n", i, end=" ")

# For creating a new list of datas
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_list = []
for value in raw_data:
    if not math.isnan(value):
        filtered_list.append(value)
print("\n", filtered_list)

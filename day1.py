from collections import Counter

list1 = []
list2 = []

with open('day1.txt', 'r') as file:
    for line in file:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

distance = sum(abs(num1 - num2) for num1, num2 in zip(list1, list2))

print('total distance:', distance)

counter = Counter(list2)
similarity = sum(counter[num1] * num1 for num1 in list1)

print('similarity score:', similarity)
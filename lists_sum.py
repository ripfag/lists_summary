list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12]
lists_summary = []
for number in range(list1.__len__()):
    lists_summary.append(list1[number]+list2[number])

print(lists_summary)
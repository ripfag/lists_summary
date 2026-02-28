def lists_sum():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    list2 = [7, 8, 9, 10, 11, 12, 13, 14, 15]
    lists_summary = []
    biggest_list = max(len(list1), len(list2))

    for number in range(biggest_list):
        num1 = list1[number] if number < len(list1) else 0
        num2 = list2[number] if number < len(list2) else 0
        lists_summary.append(num1 + num2)
    print(lists_summary)


lists_sum()

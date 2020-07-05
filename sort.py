def selection_sort(list_):
    print("List in sort function before sorting : ", list_)
    for i in range(0, len(list_)):
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[i]:
                tmp = list_[j]
                list_[j] = list_[i]
                list_[i] = tmp
    print("List in sort function after sorting : ", list_)


myList1 = [5, 4, 3, 2, 1]

selection_sort(myList1)
print("List in the main context after sort function is finished : ", myList1)

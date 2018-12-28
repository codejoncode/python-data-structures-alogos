def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if not data[mid]:
            left = mid - 1
            right = mid + 1
            while(True):
                if left < first and right > last:
                    print("{0} is not in the dataset".format(search_val))
                    return
                elif right <= last and data[right]:
                    mid = right
                    break
                elif left >= first and data[left]:
                    mid = left
                    break
                else:
                    right += 1
                    left -= 1
        # end of second while
        if data[mid] == search_val:
            print("{0} found at position {1}".format(search_val, mid))
            return
        if search_val < data[mid]:
            last = mid - 1
        if search_val > data[mid]:
            first = mid + 1
    # end of first while
    print("{0} is not in the dataset".format(search_val))


search_1 = ["A", "", "", "", "B", "", "", "", "C", "", "", "D"]
target_1 = "C"

sparse_search(search_1, target_1)

search_2 = ["A", "B", "", "", "E"]
target_2 = "A"

sparse_search(search_2, target_2)

search_3 = ["", "X", "", "Y", "Z"]
target_3 = "Z"

sparse_search(search_3, target_3)

search_4 = ["A", "", "", "", "B", "", "", "", "C"]
target_4 = "D"

sparse_search(search_4, target_4)

search_5 = ["Apple", "", "Banana", "", "", "", "", "Cow"]
target_5 = "Banana"

sparse_search(search_5, target_5)

search_6 = ["Alex", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"]
target_6 = "Parth"

sparse_search(search_6, target_6)


if __name__ == '__main__':
    list1 = []
    list2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
        list2.append(score)
        
    second_lowest = (sorted(set(list2))[1])
    for i in sorted(list1):
        if i[1] == second_lowest:
            print(i[0])

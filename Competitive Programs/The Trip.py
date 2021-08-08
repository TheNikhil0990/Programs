def calculation_trip(list_students):
    new_list = []
    total_avg = 0
    money_give = 0
    for i in range(0,len(list_students)):
        total_avg += list_students[i]
    total_avg = (total_avg /len(list_students))

    for j in list_students:
        temp = total_avg - j
        new_list.append(temp)
    print(new_list)

    for k in new_list:
        if(k > 0):
            money_give += k
    return money_give



def main():
    n = int(input("Enter the no of student: "))
    list_students = []
    for i in range(0,n):
        s = float(input())
        list_students.append(s)
    print(list_students)

    s = calculation_trip(list_students)
    print(s)
main()

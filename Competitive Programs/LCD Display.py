def horizontal(n1,main_list,ph):
    h = "-"
    s = " "
    #s2 ="  "
    str_printed = ""
    for so in main_list:
        if(int(so) == 0):
            if(ph == 0 or ph == 4):
                str_printed += s
                for s_5 in range(0, int(n1)):
                    str_printed += h
                str_printed += s
            else:
                str_printed += s
                for s_7 in range(0, int(n1)):
                    str_printed += s
                str_printed += s

        if(int(so) == 1):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for k in range(0,int(n1)):
                    str_printed += s
                str_printed += s
        if(int(so) == 2):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for k in range(0,int(n1)):
                    str_printed += h
                str_printed += s
        if(int(so) == 3):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for s_4 in range(0,int(n1)):
                    str_printed += h
                str_printed += s
        if(int(so) == 4):
            if(ph == 0 or ph == 4):
                str_printed += s
                for s_8 in range(0,int(n1)):
                    str_printed += s
                str_printed += s
            else:
                str_printed += s
                for s_9 in range(0,int(n1)):
                    str_printed += h
                str_printed += s

        if(int(so) == 5):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for s_12 in range(0,int(n1)):
                    str_printed += h
                str_printed += s

        if(int(so) == 6):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for s_12 in range(0,int(n1)):
                    str_printed += h
                str_printed += s
        if(int(so) == 7):
            if(ph == 0):
                str_printed += s
                for s_12 in range(0,int(n1)):
                    str_printed += h
                str_printed += s
            else:
                str_printed += s
                for s_15 in range(0,int(n1)):
                    str_printed += s
                str_printed += s
        if(int(so) == 8):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for s_13 in range(0,int(n1)):
                    str_printed += h
                str_printed += s
        if(int(so) == 9):
            if(ph == 0 or ph == 2 or ph == 4):
                str_printed += s
                for s_14 in range(0,int(n1)):
                    str_printed += h
                str_printed += s


        str_printed += s
    print(str_printed)

def vertical(n1,main_list,ph):
    v = "|"
    sp = " "
    str_vertical = ""
    #no = (int(n1)+int(n1))
    for h in range(0,int(n1)):
        for j in main_list:
            if(int(j) == 0):
                if(ph == 1 or ph == 3):
                    str_vertical += v
                    for s_6 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v

            if(int(j) == 1):
                if(ph == 1 or ph == 3):
                    str_vertical += sp
                    for f in range(0,int(n1)):
                        str_vertical += sp
                    str_vertical += v
            if(int(j) == 2):
                if(ph == 1):
                    str_vertical += sp
                    for s_2 in range(0,int(n1)):
                        str_vertical += sp
                    str_vertical += v
                else:
                    str_vertical += v
                    for s_3 in range(0,int(n1)):
                        str_vertical += sp
                    str_vertical += sp
            if(int(j) == 3):
                if(ph == 1 or ph == 3):
                    str_vertical += sp
                    for s_4 in range(0,int(n1)):
                        str_vertical += sp
                    str_vertical +=v
            if(int(j) == 4):
                if(ph == 1):
                    str_vertical += v
                    for s_10 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v
                else:
                    str_vertical += sp
                    for s_11 in range(0,int(n1)):
                        str_vertical += sp
                    str_vertical += v

            if(int(j) == 5):
                if(ph == 1):
                    str_vertical += v
                    for s_16 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += sp
                else:
                    str_vertical += sp
                    for s_17 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v

            if(int(j) == 6):
                if(ph == 1):
                    str_vertical += v
                    for s_18 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += sp
                else:
                    str_vertical += v
                    for s_19 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v

            if(int(j) == 7):
                if(ph == 1 or ph == 3):
                    str_vertical += sp
                    for s_20 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v

            if(int(j) == 8):
                if(ph == 1 or ph == 3):
                    str_vertical += v
                    for s_21 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v

            if(int(j) == 9):
                if(ph == 1 ):
                    str_vertical += v
                    for s_22 in range(0, int(n1)):
                        str_vertical += sp
                    str_vertical += v
                else:
                    str_vertical += sp
                    for s_23 in range(0,int(n1)):
                        str_vertical += sp
                    str_vertical += v


            str_vertical += sp
        print(str_vertical)
        str_vertical =""







def main():
    n = input()
    l = []
    l = n.split(" ")
    #print(l)
    main_list = []
    n1 = l[0]
    #print(n1)
    for i in l[1]:
        main_list.append(i)
    #print(main_list)
    #there are five phases
    #horizontal - 0,2,4
    #vertical - 1,3
    for ph in range(0,5):
        if(ph == 0 or ph == 2 or ph == 4):
            horizontal(n1,main_list,ph)
        else:
            vertical(n1,main_list,ph)


main()

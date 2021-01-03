#
t = int(input())

for testcase in range(t):
    string = "()?????"

    resource = 0
    flag = True
    for i in range (len(string)):
        if (resource < 0):
            flag = False
            break
        if (string[i] == '('):
            resource += 1
        elif (string[i] == ')'):
            resource -= 1
        else:
            if resource == 0:
                resource += 1
            else:
                resource -= 1

    if (flag and (resource == 0 or resource == 1)):
        print("Yes")
    else:
        print("NO")
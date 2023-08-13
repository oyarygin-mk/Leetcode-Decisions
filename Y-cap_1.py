n = int(input())

for _ in range(n):

    str1 = input()
    str2 = input()

    replace_dict = {}
    flag = False

    for i in range(0, len(str2)):
        if not str1[i] in replace_dict:
            replace_dict[str1[i]] = str2[i]
        else:
            if not replace_dict[str1[i]] == str2[i]:
                print("NO")
                flag = True
                break
        if not str2[i] in replace_dict:
            replace_dict[str2[i]] = str1[i]
        else:
            if not replace_dict[str2[i]] == str1[i]:
                print("NO")
                flag = True
                break

    if not flag:
        print("YES")

def check_for_beautifull(s):

    if len(s) <= 2:
        return "NO"

    mid = len(s) // 2
    for i in range(mid):
        flag = False
        sub_string = s[: i + 1]
        first_number = int(sub_string)
        temp = int(sub_string)
        while len(sub_string) < len(s):
            temp += 1
            sub_string += str(temp)
        if sub_string == s:
            flag = True
            break
    if flag is True:
        return ("YES", str(first_number))
    elif flag is False:
        return "NO"

n = int(input())
output = []

for _ in range(n):

    output.append(check_for_beautifull(input()))

for answer in output:

    if answer == "NO":
        print("NO")
    else:
        output_string = " ".join(answer)
        print(output_string)
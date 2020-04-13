# Questions 1
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


# Questions 2
n = int(input())
mid = n // 2
mid += 1

for i in range(1, n + 2):

    if i <= mid:

        print("*" * i)

    else:
        mid -= 1
        print("*" * mid)


# Question 3

n = int(input())

for i in range(n, 0, -1):

    temp = i
    for j in range(n):

        if temp <= n:

            print(temp, end=" ")
        
        else:

            print(n, end=" ")
        
        temp += 1

    print()


# Question 4
def frequency(input_string):

    # hash map of all digits with 0 count (initial case)
    frequency_map = {i:0 for i in range(10)}
    # filter out the digts in string_digits which is a list
    string_digits = list((filter(lambda charecter: int(charecter.isdigit()), input_string)))
    # convert the elements to integer for the better
    string_digits = list(map(int, string_digits))
    for number in string_digits:

        frequency_map[number] += 1

    return frequency_map
    




input_string = input()
fm = frequency(input_string)

for key in fm:

    print(fm[key], end=" ")


# Question 5

def calculate_area(list_of_sides):

    global area_map
    a = list_of_sides[0]
    b = list_of_sides[1]
    c = list_of_sides[2]
    p = (a + b + c) / 2
    s = (p*(p - a)*(p - b)*(p - c)) ** 0.5
    area_map[s] = [a, b, c]


area_map = {}

n = int(input())

for _ in range(n):

    calculate_area(list(map(int, input().split())))
for area in sorted(area_map):
    for element in area_map[area]:
        print(element, end=" ")
    print()

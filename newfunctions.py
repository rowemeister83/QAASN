#1st task


def max3(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num3):
        return num2
    else:
        return num3
print(max3(59,69,99))


#2nd task

def find_sum(numbers_list):
    result=0
    for i in numbervar:
        result += i
    return result


numbervar = [205, 11, 66, 1, 47, 19]
print(find_sum(numbervar))

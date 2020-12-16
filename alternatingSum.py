
# For example, if n = 52134, the answer should be 5 - 2 + 1 - 3 + 4 = 5.

def alternateSum(num):

    str_num = str(num)
    alt_sum = 0
    plus = True

    for char in str_num:
        if plus:
            alt_sum += int(char)
            plus = False
        else:
            alt_sum -= int(char)
            plus = True

    print(alt_sum)
    return alt_sum

alternateSum(52134)
alternateSum(12345)
alternateSum(104956)

def next_smaller(n):
    number = [int(i) for i in str(n)]
    f_num = len(number)-1
    s_num = float("-inf")
    next_s_num = float("-inf")

    if len(number) == 1 or number == sorted(number):
        return -1
    for i in range(len(number)-1,0,-1):
        if number[i] < number[i-1]:
            f_num -=1
            break
        f_num -=1
    for i in range(f_num, len(number)):
        if (number[i] < number[f_num] and number[i] > s_num):
            s_num = number[i]
            next_s_num = i
    number[f_num], number[next_s_num] =  number[next_s_num], number[f_num]
    numbers2  = number[f_num+1:]
    numbers2.sort(reverse=True)
    for i in range(len(numbers2)):
        number[i+f_num+1] = numbers2[i]
    number = [str(x) for x in number]
    s = "".join(number)
    return int(s) if s[0] != "0" else -1
print(next_smaller(2071))

"""
__________________________________________________________________
4 kyu
Next smaller number with the same digits:

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."

"""
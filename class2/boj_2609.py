num1, num2 = map(int, input().split())
nums = [num1, num2]
divisors = []
num = 2
while 1:
    if nums[0] % num == 0 and nums[1] % num == 0:
        divisors.append(num)
        nums[0] = nums[0] // num
        nums[1] = nums[1] // num
        num = 2
    else:
        if nums[0] // num == 0 or nums[1] // num == 0:
            break
        num += 1

a = 1
for i in divisors:
    a *= i
b = (num1 // a) * (num2 // a) * a

print(a)
print(b)

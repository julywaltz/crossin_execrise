#生成水仙花数
n_nums = []
for num in range(100, 1000):
    num_b = num // 100
    num_s = (num - num_b * 100) // 10
    num_g = num - num_b * 100 - num_s * 10
    if num_b**3 + num_s**3 + num_g**3 == num:
        n_nums.append(num)
print(n_nums)

#生成完全数
from math import sqrt
primes = []
for num in range(1, 10000):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        primes.append(num)
p_nums = []
for x in primes:
    if 2 ** x -1 in primes:
        p_num = (2 ** x - 1) * 2 ** ( x - 1)
        p_nums.append(p_num)
print(p_nums)

#百钱百鸡问题
ans = []
for cock in range(0,100):
    for hen in range(0,100):
        if 5 * cock + 3 * hen + (100 - cock - hen)/3 == 100:
            ans.append({'公鸡':cock, '母鸡':hen, '小鸡':100- cock- hen})
print(ans)


#生成斐波拉切数列
a = 0
b = 1
for _ in range(20):
    (b, a) = (a, a+b)
    print(a,end=' ')




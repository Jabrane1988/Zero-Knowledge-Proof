import random

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count + 1
    return count == 1

def largest_diviser(x):
    largest_divisor = 0
    for i in range(2, x):
        if x % i == 0 and isPrime(i):
            largest_divisor = i
    return largest_divisor

def find_number_with_order(p, q, limit):
    num1 = 0
    num2 = 0
    for i in range(2, limit):
        if pow(i, q)%p == 1:
            num1 = i
            break
    
    for j in range(num1+1, limit):
        if pow(j, q)%p == 1:
            num2 = j
            break

    return num1, num2





# Let's define the random prime number q
minPrime = 0
maxPrime = 25

cached_prime = [i for i in range(minPrime, maxPrime) if isPrime(i)]
p = cached_prime[len(cached_prime)-1]
q = largest_diviser(p-1)

print("p, q = ", p, q)


g, h = find_number_with_order(p, q, p)
print("g, h = ", g, h)

# secret key
x = 10
 
y1 = pow(g,x)%p
y2 = pow(h,x)%p

print("y1 = ", y1)
print("y2 = ", y2)


k = random.randint(1,100)
 
r1 = pow(g, k)%p
print("r1 = ", r1)
r2 = pow(h, k)%p
print("r2 = ", r2)

# Challenge
c = random.randint(1,10)
print("c = ", c)
 
s = (k-c*x)%q
print("s = ", s)
# 

print("result11 = ", pow(g,s))
print("result22 = ", pow(y1, c))

# 
print(r1 == (pow(g,s)*pow(y1, c))%p)
print(r2 == (pow(h,s)*pow(y2, c))%p)
# 
# 
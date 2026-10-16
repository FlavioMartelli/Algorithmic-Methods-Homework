#problem 1
print("Hello, World!")

#problem 2
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2 == 1):
        print("Weird")
    elif (n%2 == 0 and n <= 5 and n >= 2):
        print("Not Weird")
    elif (n%2 == 0 and n <= 20 and n >= 6):
        print("Weird")
    else:
        print("Not Weird")

#problem 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#problem 4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

#problem 5
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i**2)

#problem 6
def is_leap(year):
    leap = False
    if (year%4 == 0):
        leap = True
    if (year%100 == 0):
        leap = False
    if (year% 400 == 0):
        leap = True
    return leap

year = int(input())
print(is_leap(year))

#problem 7
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, sep="", end="")

#problem 8
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = [[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1)if i+j+k!=n]
    print(res)

#problem 9
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = second = float("-inf")
    for number in arr:
        if (number > first):
            first, second = number, first
        elif (number < first and number > second):
            second = number
    print(second)

#problem 10
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = sorted(set(record[1] for record in records))
    sls = scores[1]
    nms = sorted([record[0] for record in records if record[1] == sls])
    for n in nms:
        print(n)

#problem 11
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name])/3
    print(f"{avg:.2F}")

#problem 12
if __name__ == '__main__':
    N = int(input())
    list = []
    for n in range (N):
        parts = input().split()
        command = parts[0]
        
        if "insert" == command:
            list.insert(int(parts[1]), int(parts[2]))
        if "print" == command:
            print(list)
        if "remove" == command:
            list.remove(int(parts[1]))
        if "append" == command:
            list.append(int(parts[1]))
        if "sort" == command:
            list.sort()
        if "pop" == command:
            list.pop()
        if "reverse" == command:
            list.reverse()    

#problem 13
N = int(input())
nlist = map(int, input().split())
t = tuple(nlist)
print(hash(t))

#problem 14
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#problem 15
def split_and_join(line):
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#problem 16
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#problem 17
def mutate_string(string, position, character):
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#problem 18
def count_substring(string, sub_string):
    return

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#problem 19
if __name__ == '__main__':
    s = input()
    q = [False]*5
    for c in s:
        q[0] |= c.isalnum()
        q[1] |= c.isalpha()
        q[2] |= c.isdigit()
        q[3] |= c.islower()
        q[4] |= c.isupper()
    for r in q:
        print(r)

#problem 20
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#problem 21
import textwrap

def wrap(string, max_width):
    result = ""
    for i, c in enumerate(string):
        if i%max_width == 0 and i != 0:
            result += "\n"
        result += c
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#problem 22
N,M = map(int, input().split())
pattern = ".|."
result = "\n".join((pattern*(2*(N//2-abs(N//2-i))+1)).center(M, "-") if i!= N//2 else "WELCOME".center(M, "-") for i in range(N))
print(result)

#problem 23
def print_formatted(number):
    w = len(bin(number)[2:])
    res = "\n".join(f"{str(i).rjust(w)} {oct(i)[2:].rjust(w)} {hex(i)[2:].upper().rjust(w)} {bin(i)[2:].rjust(w)}" for i in range(1, number+1))
    print(res)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#problem 24
def substring(c, n):
    if n != 1:
        a = chr(ord(c)-1)
        res = substring(a, n-1)
        res = f"{c}-" + res + f"-{c}"
    else:
        res = f"{c}"
    return res
    

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    N = 2 * size - 1
    w = (size-1)*4 + 1
    for i in range(N):
        v = size - abs(size - 1 - i)
        result = substring(alphabet[size - 1], v)
        print(result.center(w,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#problem 25
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join(w[0].upper() + w[1:] if w else "" for w in s.split(" "))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#problem 26
def minion_game(string):
    l = len(string)
    stuart = 0
    kevin = 0
    c = set()
    v = set()
    vowels = ["A", "E", "I", "O", "U"]
    for i, letter in enumerate(string):
        if letter in vowels:
            kevin += l-i
        else:
            stuart += l-i
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin == stuart:
        print("Draw")
    else:
        print(f"Stuart {stuart}")
                

if __name__ == '__main__':
    s = input()
    minion_game(s)

#problem 27
def merge_the_tools(string, k):
    l = len(string)
    lis = []
    for i in range(0, l, k):
        j = i + k
        lis.append(string[i:j])
    for element in lis:
        print("".join(dict.fromkeys(element)))     

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#problem 28
def average(array):
    s = set(array)
    avg = sum(s)/len(s)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#problem 29
n,m = map(int, input().split())
lis = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
h = 0
for num in lis:
    if num in A:
        h += 1
    elif num in B:
        h -= 1
print(h)

#problem 30
l1 = int(input())
M = set(map(int,input().split()))
l2 = int(input())
N = set(map(int, input().split()))
res = (M.difference(N)).union(N.difference(M))
for e in sorted(res):
    print(e)

#problem 31
N = int(input())
s = set()
for _ in range(N):
    country = input()
    s.add(country)
print(len(s))

#problem 32
N = int(input())
s = set(map(int, input().split()))
Ops = int(input())
for _ in range(Ops):
    args = input().split()
    if args[0] == "pop":
        s.pop()
    if args[0] == "remove":
        s.remove(int(args[1]))
    if args[0] == "discard":
        s.discard(int(args[1]))
print(sum(s))

#problem 33
N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = set(map(int, input().split()))
res = a.union(b)
print(len(res))

#problem 34
N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = set(map(int, input().split()))
res = a.intersection(b)
print(len(res))

#problem 35
N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = set(map(int, input().split()))
res = a.difference(b)
print(len(res))

#problem 36
N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = set(map(int, input().split()))
t1 = a.difference(b)
t2 = b.difference(a)
res = t1.union(t2)
print(len(res))

#problem 37
N = int(input())
s = set(map(int, input().split()))

sets = int(input())

for _ in range(sets):
    args = input().split()
    s1 = set(map(int, input().split()))

    if args[0] == "intersection_update":
        s.intersection_update(s1)
    elif args[0] == "update":
        s.update(s1)
    elif args[0] == "symmetric_difference_update":
        s.symmetric_difference_update(s1)
    elif args[0] == "difference_update":
        s.difference_update(s1)

print(sum(s))

#problem 38
K = int(input())
numbers = list(map(int,input().split()))
d = dict()
for n in numbers:
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1
for e in d.keys():
    if d[e] == 1:
        print(e)

#problem 39
T = int(input())
for t in range(T):
    N = int(input())
    A = set(map(int,input().split()))
    M = int(input())
    B = set(map(int,input().split()))
    if len(A) > len(B):
        print(False)
    else:
        if A.difference(B) == set():
            print(True)
        else:
            print(False)

#problem 40
s = set(map(int, input().split()))
N = int(input())
res = True
for n in range(N):
    a = set(map(int, input().split()))
    if len(a) >= len(s):
        res = False
    else:
        if a.difference(s) != set():
            res = False
print(res)

#problem 41
from collections import Counter

X = int(input())
sizes = Counter(map(int, input().split()))
customers = int(input())
gain = 0
for customer in range(customers):
    size, cost = map(int,input().split())
    if sizes[size] > 0:
        gain += cost
        sizes[size] -= 1
print(gain)

#problem 42
from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for n in range(N):
    e = input()
    d[e].append(n+1)
for m in range(M):
    e = input()
    print(*d[e] if d[e] else [-1])

#problem 43
from collections import namedtuple

N = int(input())
fields = list(input().split())
t = namedtuple("Student", [fields[0], fields[1], fields[2], fields[3]])
s = 0
for n in range(N):
    infos = list(input().split())
    stu = t(infos[0], infos[1], infos[2], infos[3])
    s += int(stu.MARKS)
print(f"{s/N : .2f}")

#problem 44
from collections import OrderedDict

N = int(input())
d = OrderedDict()
for _ in range(N):
    n, p = (input().rsplit(" ", 1))
    if n in d:
        d[n] += int(p)
    else:
        d[n] = int(p)
for n,p in d.items():
    print(f"{n} {p}")

#problem 45
from collections import OrderedDict

n = int(input())
d = OrderedDict()
for _ in range(n):
    w = input()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
print(len(d))
print(" ".join(str(v) for v in d.values()))

#problem 46
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    inst = list(input().split())
    if inst[0] == "append":
        q.append(inst[1]) 
    elif inst[0] == "appendleft":
        q.appendleft(inst[1])
    elif inst[0] == "pop":
        q.pop()
    elif inst[0] == "popleft":
        q.popleft()
print(" ".join(r for r in q))

#problem 47
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    res = {k:v for k,v in sorted(d.items(), key=lambda x: (-x[1], x[0]))[:3]}

for k,v in res.items():
    print(f"{k} {v}")

#problem 48
def ispossible(blocks):
    left = 0
    right = len(blocks) - 1
    previous = float("inf")
    res = "Yes"
    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1
        if current > previous:
            res = "No"
            return res
        previous = current
    return res
    
T = int(input())
res = []
for _ in range(T):
    N = int(input())
    blocks = list(map(int, input().split()))
    res.append(ispossible(blocks))
for r in res:
    print(r)

#problem 49
import calendar

infos = list(map(int,input().split()))
print(calendar.day_name[calendar.weekday(infos[2], infos[0], infos[1])].upper())

#problem 50
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    return str(abs(int((t1 - t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        time1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")

        t2 = input()
        time2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
        
        delta = time_delta(time1, time2)

        fptr.write(delta + '\n')

    fptr.close()

#problem 51
T = int(input())
for _ in range(T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError):
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)

#problem 52
N, X = map(int, input().split())
everyone = []
for _ in range(X):
    everyone.append(list(map(float, input().split())))
for s in zip(*everyone):
    print(f"{sum(s)/X : .1f}")

#problem 53
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

#problem 54
s = input()
print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isupper(), x.isdigit() and int(x) % 2 == 0, x))))

#problem 55
cube = lambda x: x**3 

def fibonacci(n):
    res = []
    a,b = 0,1
    for _ in range(n):
        res.append(a)
        a,b = b, a + b
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#problem 56
T = int(input())
for _ in range(T):
    n = input()
    try:
        float(n)
        print(n.count(".") == 1)
    except ValueError as e:
        print(False)

#problem 57
regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#problem 58
import re
s = input()

m = re.search(r"([a-zA-Z0-9])\1",s)
if m:
    print(m.group(1))
else:
    print(-1)

#problem 59
import numpy

def arrays(arr):
    res = numpy.array(arr, float)
    return res[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#problem 60
import numpy as np
arr = np.array(input().split(), int)
result = np.reshape(arr, (3, 3))
print(result)

#problem 61
import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
print(np.transpose(arr))
print(arr.flatten())

#problem 62
import numpy as np
n, m, p = map(int, input().split())
array_1 = np.array([input().split() for _ in range(n)], int)
array_2 = np.array([input().split() for _ in range(m)], int)
result = np.concatenate((array_1, array_2), axis=0)
print(result)

#problem 63
import numpy as np
shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))

#problem 64
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m))

#problem 65
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)

#problem 66
import numpy as np
np.set_printoptions(legacy='1.13')
a = np.array(input().split(), float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

#problem 67
import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
sum_axis_0 = np.sum(arr, axis=0)
print(np.prod(sum_axis_0))

#problem 67
import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
min_along_axis_1 = np.min(arr, axis=1)
print(np.max(min_along_axis_1))

#problem 68
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))

#problem 69
import numpy as np
n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(np.dot(a, b))

#problem 70
import numpy as np
A = np.array(input().split(), int)
B = np.array(input().split(), int)
print(np.inner(A, B))
print(np.outer(A, B))

#problem 71
import numpy as np
poly = list(map(float, input().split()))
x = float(input())
print(np.polyval(poly, x))

#problem 72
import numpy as np
n = int(input())
a = np.array([input().split() for _ in range(n)], float)
det = np.linalg.det(a)
print(round(det, 2))

#problem 73
def wrapper(f):
    def fun(l):
        l = ['+91 ' + x[-10:-5] + ' ' + x[-5:] for x in l]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#problem 74
import operator

def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return map(f, people)
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#problem 75
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)

    for child in node:
        score += get_attr_number(child)

    return score


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#problem 76
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth

    level += 1
    maxdepth = max(maxdepth, level)

    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#problem 77
import re

s = input()

vowels = 'aeiouAEIOU'
consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'

pattern = r'(?<=[%s])([%s]{2,})(?=[%s])' % (consonants, vowels, consonants)

matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)
else:
    print("-1")

#problem 78
import re

S = input()
k = input()

pattern = re.compile(re.escape(k))
match = pattern.search(S)

if not match:
    print((-1, -1))
else:
    while match:
        print((match.start(), match.end() - 1))
        
        match = pattern.search(S, match.start() + 1)

#problem 79
import re

N = int(input())

for _ in range(N):
    line = input()
    modified = re.sub(
        r'(?<= )(&&|\|\|)(?= )', 
        lambda match: 'and' if match.group() == '&&' else 'or', 
        line
    )
    print(modified)

#problem 80
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$" # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#problem 81
import re

n = int(input())

pattern = re.compile(r"^[789]\d{9}$")

for _ in range(n):
    if pattern.match(input()):
        print("YES")
    else:
        print("NO")

#problem 82
import re
import email.utils

n = int(input())

pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")

for _ in range(n):
    line = input()
    name, email_addr = email.utils.parseaddr(line)
    
    if pattern.match(email_addr):
        print(email.utils.formataddr((name, email_addr)))

#problem 83
import re

n = int(input())

pattern = re.compile(r'(?<!^)(#(?:[\da-fA-F]{3}){1,2})')

for _ in range(n):
    line = input()
    matches = pattern.findall(line)
    for match in matches:
        print(match)

#problem 84
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())

html_snippet = ""
for _ in range(n):
    html_snippet += input() + "\n"

parser = MyHTMLParser()
parser.feed(html_snippet)

#problem 85
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#problem 86
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())
html_code = ""
for _ in range(n):
    html_code += input() + "\n"

parser = MyHTMLParser()
parser.feed(html_code)

#problem 87
def is_valid_uid(uid):
    if len(uid) != 10 or not uid.isalnum():
        return False

    if len(set(uid)) != 10:
        return False

    uppercase_count = sum(1 for c in uid if c.isupper())
    if uppercase_count < 2:
        return False

    digits_count = sum(1 for c in uid if c.isdigit())
    if digits_count < 3:
        return False

    return True

t = int(input())
for _ in range(t):
    uid = input().strip()
    print("Valid" if is_valid_uid(uid) else "Invalid")

#problem 88
import re

structure_pattern = re.compile(r'^[456](\d{15}|\d{3}(-\d{4}){3})$')

consecutive_pattern = re.compile(r'(\d)\1{3}')

n = int(input())
for _ in range(n):
    card_number = input().strip()
    
    if structure_pattern.match(card_number):
        cleaned_number = card_number.replace('-', '')
        
        if consecutive_pattern.search(cleaned_number):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")

#problem 89
regex_integer_in_range = r"^[1-9][0-9]{5}$" 
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#problem 90
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_string = "".join(["".join(col) for col in zip(*matrix)])

result = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded_string)

print(result)

#problem 91
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#problem 92
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#problem 93
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    cumulative_likes = 0
    
    for _ in range(n):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3
        
    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#problem 94
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    initial_sum = sum(int(d) for d in n) * k
    if initial_sum < 10:
        return initial_sum
    return superDigit(str(initial_sum), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#problem 95
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    target = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#problem 96
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        target = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

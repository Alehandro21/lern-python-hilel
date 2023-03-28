#1
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for fib in fibonacci(10):
    print(fib)
#2
def word_gen(s):
    for word in s.split():
        yield word

for word in word_gen('i am generating words from text'):
    print(word)

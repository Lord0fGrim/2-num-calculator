#Build a simple calculator program that performs basic arithmetic operations 
#(addition, subtraction, multiplication, division) on two numbers.


q = input('Write your question: \n')

p = list(q)

for i in range(len(p)):
    if p[i] == "/":
        r = q.split('/')
        print(f"{int(r[0]) / int(r[len(r)-1]):.4f}")
    elif p[i] == "*":
        r = q.split('*')
        print(f"{int(r[0]) * int(r[len(r)-1]):.4f}")
    elif p[i] == "-":
        r = q.split('-')
        print(f"{int(r[0]) - int(r[len(r)-1]):.4f}")
    elif p[i] == "+":
        r = q.split('+')
        print(f"{int(r[0]) + int(r[len(r)-1]):.4f}")
        
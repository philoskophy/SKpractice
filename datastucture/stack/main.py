from stack import *
# STACK

s1 = Stack()
print(s1.is_empty())
s1.add(3)
s1.print_stack()
s1.add(8)
s1.print_stack()
print("pop 된 것은 : ", s1.pop())

print("size 는 : ", s1.size())
s1.print_stack()

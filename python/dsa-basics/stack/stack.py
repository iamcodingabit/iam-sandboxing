my_array = [8, 20, 4, 14]

def push(item):
    my_array.append(item)
    
def pop():
    my_array.pop()

def size():
    return len(my_array)

def isEmpty():
    if size() <= 0:
        return True
    return False

def peek():
    return my_array[-1]
    
push(17)
push(48)
print(my_array)
pop()
print(my_array)
print(size())
print(isEmpty())
print(peek())
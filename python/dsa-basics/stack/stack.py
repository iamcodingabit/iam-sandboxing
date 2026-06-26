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

def main():
    while True:
        print(f"Your current array: {my_array}")
        user_input = input("What you wanna do?: ")
        user_command = user_input.split()
        print(f"You said: {user_command}")
        
        match user_command[0]:
            case "push":
                push(user_command[1])
            case "pop":
                pop()
            case "size":
                print(size())
            case "peek":
                print(peek())
            case "empty":
                if isEmpty():
                    print("Your array is Empty")
                else:
                    print("Your array is Not Empty")
            case "quit":
                return False
            case _:
                print("Can't recognize command")
        
main()
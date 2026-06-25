f = open("demofile.txt")
print(f.read())
f.close()

f = open("mycreatedfile.txt")
print(f.read())
f.close()

with open("demofile.txt") as f:
    print(f.read())
    
with open("mycreatedfile.txt", "rt") as f:
    print(f.read())
    
with open("mycreatedfile.txt", "a") as f:
    print(f.write("Sorry about that incomprehensible behavior :("))
    
with open("mycreatedfile.txt", "rt") as f:
    print(f.read())
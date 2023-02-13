# new_list = [2,4,6, "California"]
new_list = [2,4,6,]

for element in new_list:
    try:
        print(element/2)
    except ValueError:
        print("Error ocurred, not a number!")
        print(ValueError)

# While-Break

# while <expr>:
#     <statement>

n = 4
while n > 0:
    print(n)
    n -= 1
    if n ==2: break

print("Loop ended")

for i in range(5):
    if i == 3:
        continue
    print(i)
list = []

for c in range(5):
    values = int(input("\nEnter a value: "))
    if c == 0 or values > list[-1]:
        list.append(values)
    else:
        pos = 0
        while pos < len(list):
            if values <= list[pos]:
                list.insert(pos, values)
                break
            pos += 1    

print("\nlist:", list)
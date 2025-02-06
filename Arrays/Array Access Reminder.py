data = [[1,2,3,4,5],
        [6,7,8,9,0],
        ["a","b","c","d","e"],
        ["f","g","h","i","j"]]

print(f"data:\n{data}\n")
print(f"data[1][1]:\n{data[1][1]}\n")
print(f"data[:2]:\n{data[:2]}\n")
print(f"data[2:]:\n{data[2:]}\n")
print(f"data[1:3]:\n{data[1:3]}\n")

for i in range(0,4):
    for h in range(0,5):
        print(f"data[{i}][{h}]:{data[i][h]}\n")
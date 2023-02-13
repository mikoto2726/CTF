code=input("暗号")
num=int(input("数"))
alph={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z": 26}
alph1={1:"a", 2:"b", 3:"c"}
k=0
result=""
for i in code:
    k=alph[i]+1
    result+=alph1[k]
print(result)



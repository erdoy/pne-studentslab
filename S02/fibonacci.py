v1 = 0
v2 = 1

for i in range(11):
    print(v1, end = " ")
    v2 = v2 + v1
    v1 = v2 - v1

# 0 1 1 2 3 5 8 13
# v1v2
#   v1v2
#     v1v2

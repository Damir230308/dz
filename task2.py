
# 0(N^2) - Квадратичная сложность

def function(list):
    for i in list:
        is_min = True
        for j in list:
            if i < j:
                is_min = False
            if is_min:
                return i

# 0(n) - линейная сложность

def function2(list):
    min_value = list[0]
    for i in list:
        if i < min_value:
            min_value = i
    return min_value

print(function([100, 200, 450, 123]))
print(function2([234, 123, 989, 111]))

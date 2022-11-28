def sum_recursion(num):
    if num == 0:
          return num
    return num + sum_recursion(num-1)

ans = sum_recursion(8)
print(ans)


        

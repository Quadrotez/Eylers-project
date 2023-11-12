a = 0; i = 0
while i < 1000:
    a = a + i if i % 3 == 0 or i % 5 == 0 else a
    i += 1
    
print(a)

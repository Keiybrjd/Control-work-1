for i in range(7):
    for j in range(7):
        if (i == 0 and (j == 1 or j == 5)) or (i == 1 and (j == 0 or j == 6)) or \
           (i == 2 and (j == 0 or j == 1 or j == 5 or j == 6)) or \
           (i == 3 and (j == 0 or j == 1 or j == 2 or j == 4 or j == 5 or j == 6)) or \
           (i == 4 and (j == 1 or j == 2 or j == 4 or j == 5)) or \
           (i == 5 and (j == 2 or j == 3 or j == 4)) or \
           (i == 6 and j == 3):
            print('*', end=' ')
     else:
           print(' ', end=' ')
print()

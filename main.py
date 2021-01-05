import enchant
import time

l0 = str(input('Enter the 1st letter.'))
l1 = str(input('Enter the 2nd letter.'))
l2 = str(input('Enter the 3th letter.'))
l3 = str(input('Enter the 4th letter.'))
l4 = str(input('Enter the 5th letter.'))
l5 = str(input('Enter the 6th letter.'))
l6 = str(input('Enter the 7th letter.'))
l7 = str(input('Enter the 8th letter.'))
l8 = str(input('Enter the 9th letter.'))

letters = [l0, l1, l2, l3, l4, l5, l6, l7, l8]
i = int(1)
eng = enchant.Dict("en_GB")

print(letters)

start = time.time()
print('-='*30)
print('Possibilities for 3 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):

            if aux0 != aux1 and aux0 != aux2 and\
                aux1 != aux2:

                engWord = str(letters[aux0] + letters[aux1] + letters[aux2])
                if eng.check(engWord):
                    print(engWord)
                    i += 1
i3 = i
print('\nNumber of words with 3 letters: {}\nTotal of words: {}\n'.format(i3, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))

print('-='*30)
print('Possibilities for 4 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):
            for aux3 in range(9):

                if aux0 != aux1 and aux0 != aux2 and aux0 != aux3 and\
                    aux1 != aux2 and aux1 != aux3 and\
                    aux2 != aux3:

                    engWord = str(letters[aux0] + letters[aux1] + letters[aux2] + letters[aux3])
                    if eng.check(engWord):
                        print(engWord)
                        i += 1
i4 = i - i3
print('\nNumber of words with 4 letters: {}\nTotal of words: {}\n'.format(i4, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))

print('-='*30)
print('Possibilities for 5 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):
            for aux3 in range(9):
                for aux4 in range(9):

                    if aux0 != aux1 and aux0 != aux2 and aux0 != aux3 and aux0 != aux4 and\
                        aux1 != aux2 and aux1 != aux3 and aux1 != aux4 and\
                        aux2 != aux3 and aux2 != aux4 and\
                        aux3 != aux4:

                        engWord = str(letters[aux0] + letters[aux1] + letters[aux2] + letters[aux3] + letters[aux4])
                        if eng.check(engWord):
                            print(engWord)
                            i += 1
i5 = i - i4 - i3
print('\nNumber of words with 5 letters: {}\nTotal of words: {}\n'.format(i5, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))

print('-='*30)
print('Possibilities for 6 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):
            for aux3 in range(9):
                for aux4 in range(9):
                    for aux5 in range(9):

                        if aux0 != aux1 and aux0 != aux2 and aux0 != aux3 and aux0 != aux4 and aux0 != aux5 and\
                            aux1 != aux2 and aux1 != aux3 and aux1 != aux4 and aux1 != aux5 and\
                            aux2 != aux3 and aux2 != aux4 and aux2 != aux5 and\
                            aux3 != aux4 and aux3 != aux5 and\
                            aux4 != aux5:

                            engWord = str(letters[aux0] + letters[aux1] + letters[aux2] + letters[aux3] + letters[aux4] + letters[aux5])
                            if eng.check(engWord):
                                print(engWord)
                                i += 1
i6 = i - i5 - i4 - i3
print('\nNumber of words with 6 letters: {}\nTotal of words: {}\n'.format(i6, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))

print('-='*30)
print('Possibilities for 7 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):
            for aux3 in range(9):
                for aux4 in range(9):
                    for aux5 in range(9):
                        for aux6 in range(9):

                            if aux0 != aux1 and aux0 != aux2 and aux0 != aux3 and aux0 != aux4 and aux0 != aux5 and aux0 != aux6 and\
                                aux1 != aux2 and aux1 != aux3 and aux1 != aux4 and aux1 != aux5 and aux1 != aux6 and\
                                aux2 != aux3 and aux2 != aux4 and aux2 != aux5 and aux2 != aux6 and\
                                aux3 != aux4 and aux3 != aux5 and aux3 != aux6 and\
                                aux4 != aux5 and aux4 != aux6 and\
                                aux5 != aux6:

                                engWord = str(letters[aux0] + letters[aux1] + letters[aux2] + letters[aux3] + letters[aux4] + letters[aux5] + letters[aux6])
                                if eng.check(engWord):
                                    print(engWord)
                                    i += 1
i7 = i - i6 - i5 - i4 - i3
print('\nNumber of words with 7 letters: {}\nTotal of words: {}\n'.format(i7, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))

print('-='*30)
print('Possibilities for 8 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):
            for aux3 in range(9):
                for aux4 in range(9):
                    for aux5 in range(9):
                        for aux6 in range(9):
                            for aux7 in range(9):

                                if aux0 != aux1 and aux0 != aux2 and aux0 != aux3 and aux0 != aux4 and aux0 != aux5 and aux0 != aux6 and aux0 != aux7 and\
                                    aux1 != aux2 and aux1 != aux3 and aux1 != aux4 and aux1 != aux5 and aux1 != aux6 and aux1 != aux7 and\
                                    aux2 != aux3 and aux2 != aux4 and aux2 != aux5 and aux2 != aux6 and aux2 != aux7 and\
                                    aux3 != aux4 and aux3 != aux5 and aux3 != aux6 and aux3 != aux7 and\
                                    aux4 != aux5 and aux4 != aux6 and aux4 != aux7 and\
                                    aux5 != aux6 and aux5 != aux7 and\
                                    aux6 != aux7:

                                    engWord = str(letters[aux0] + letters[aux1] + letters[aux2] + letters[aux3] + letters[aux4] + letters[aux5] + letters[aux6] + letters[aux7])
                                    if eng.check(engWord):
                                        print(engWord)
                                        i += 1
i8 = i - i7 - i6 - i5 - i4 - i3
print('\nNumber of words with 8 letters: {}\nTotal of words: {}\n'.format(i8, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))

print('-='*30)
print('Possibilities for 9 letters')
print('Wait..')
print('-='*30)
for aux0 in range(9):
    for aux1 in range(9):
        for aux2 in range(9):
            for aux3 in range(9):
                for aux4 in range(9):
                    for aux5 in range(9):
                        for aux6 in range(9):
                            for aux7 in range(9):
                                for aux8 in range(9):

                                    if aux0 != aux1 and aux0 != aux2 and aux0 != aux3 and aux0 != aux4 and aux0 != aux5 and aux0 != aux6 and aux0 != aux7 and aux0 != aux8 and\
                                        aux1 != aux2 and aux1 != aux3 and aux1 != aux4 and aux1 != aux5 and aux1 != aux6 and aux1 != aux7 and aux1 != aux8 and\
                                        aux2 != aux3 and aux2 != aux4 and aux2 != aux5 and aux2 != aux6 and aux2 != aux7 and aux2 != aux8 and\
                                        aux3 != aux4 and aux3 != aux5 and aux3 != aux6 and aux3 != aux7 and aux3 != aux8 and\
                                        aux4 != aux5 and aux4 != aux6 and aux4 != aux7 and aux4 != aux8 and\
                                        aux5 != aux6 and aux5 != aux7 and aux5 != aux8 and\
                                        aux6 != aux7 and aux6 != aux8 and\
                                        aux7 != aux8:

                                        engWord = str(letters[aux0] + letters[aux1] + letters[aux2] + letters[aux3] + letters[aux4] + letters[aux5] + letters[aux6] + letters[aux7] + letters[aux8])
                                        if eng.check(engWord):
                                            print(engWord)
                                            i += 1
i9 = i - i8 - i7 - i6 - i5 - i4 - i3
print('\nNumber of words with 9 letters: {}\nTotal of words: {}\n'.format(i9, i))
end = time.time()
print('Operation time: {:.2f} sec\n'.format(end - start))
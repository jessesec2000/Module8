#import library
import itertools

#data set
Cities = ["Lome", "Yaounde", "Djamenna", "Ouagdougou", "Dakar", "Lesotho", "Accra", "Nairobi"]
MMR = [11, 21, 31, 41, 51, 16, 17, 18] #Maternal Mortality Rate rounded up to the nearst whole number
MA = ["16", "17", "16", "19", "15", "16", "20", "19"] #Mean age of mother

#repeat function
print("List MMR repeated 2 times: ")
for i in itertools.repeat(Cities, 2):
    print(i)
print()

#slice function
print("This is the Maternal Mortality list sliced at 7: ")
for i in itertools.islice(MMR,7):
    print(i)
print()

#cycle function
print("This is Cities list cycled twice: ")
count = 0
for i in itertools.cycle(Cities):
    if count > 15:
        break
    else:
        print(i)
        count += 1
print()

#chain function
print("MMR and MA after the chain function: ")
for i in itertools.chain(MMR, MA):
    print(i, end='')
    print(" ", end='')
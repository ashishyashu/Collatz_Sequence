# # myPets = ['Zophie', 'Pooka', 'Fat-tail']
# # print("Enter your pet name : ")
# # name = input()
# # if name not in myPets:
# # # while name not in myPets:
# #     print("I don't have a pet named " + name )
# # else:
# #     print(name + " is my pet. " )
# #
#
#
# print('Four score and seven ' +
#         '\nyears ago...'
#       + '\na terrible earthquake hit my state.  ')
#
# print('Four score and seven')
# print('\nyears ago...')


#  Practice project = LIST (AUTOMATE THE BORING STUFF) : ( CH- 4)
###   COMMA CODE

# spam = ['apples', 'bananas', 'tofu', 'cats']
# for i in spam[0:-1]:
#     print(i, end = ', ')
# print("and " + spam[-1] + '.')
# print()
#
# for i in spam[0:-2]:
#     print(i, end = ', ')
# print("" + spam[-2], end='')
# print(" and " + spam[-1] + '.')


###  Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


#
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end="")
print()
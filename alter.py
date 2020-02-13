# # def collatz(number):
# #     if (isEven(number)):
# #         x = number // 2
# #         print(x)
# #         return x
# #     else:
# #         y = 3 * number + 1
# #         print(y)
# #         return y
# #
# #
# # def isEven(number):
# #     return number % 2 == 0
# #
# # def repetativeCollatz(number):
# #     result = collatz(number)
# #     if (result != 1):
# #         repetativeCollatz(result)
# #
# #
# # print("enter the number : ")
# # number = int(input())
# # repetativeCollatz(collatz(number))
# #
# #
# # # result = collatz(number)
# # # collatz(number)
# # #
# # # while result != 1 :
# # #     collatz(result)
# # #
# # #
# # #     if result == 1:
# # #         break
# # #
#
#
# # L = [1, 2, 3, 4, 5]
# # print(*L)
# #
# # for x in L:
# #     print(x, end=" ")
# # print()
# # for x in L:
# #     print(x, end=" , ")
#
# #
# # for i in L:
# #     print(*L, sep = ',')
# #
# # print()
# # for i in L:
# #     print(i, sep=' , ')
# # print(*L, sep = ',')
# # print()
# #
list = [1, 2, 3, 4, 5]
for i in list[0:-1]:
    print(i, end=', ')
    print()
print(list[-1])
#     print(list[-1])
# #
# #
# # spam = ['apples', 'bananas', 'tofu', 'cats']
# # for i in spam[0:-1]:
# #     print(i, end=', ')
# # print('and ' + spam[-1])
# #


#
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
#
# def list_joiner(list):
#     """Take a list and print it as an Oxford comma having sentence."""
#     count = 0
#     joined = ''
#     while count < len(list) - 2:
#         joined += list[count] + ', '
#         count += 1
#     joined += list[-2] + ' and '
#     joined += list[-1] + '.'
#     return joined
#
#
# print(list_joiner(spam))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def plot_grid(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for col in range(num_cols):
        for row in range(num_rows):
            print (grid[row][col], end='')
        print()

if __name__ == '__main__':
    plot_grid(grid)
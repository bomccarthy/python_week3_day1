# def array_diff(a, b):
#     return [i for i in a if i not in b]
#
# print(array_diff([1,2,3], [1, 2]))

# def disemvowel(string_):
#     while 'a' or 'e' or 'i' or 'o' or 'u' in string_:
#         string_ = string_.replace('a', '')
#         string_ = string_.replace('e', '')
#         string_ = string_.replace('i', '')
#         string_ = string_.replace('o', '')
#         string_ = string_.replace('u', '')
#         string_ = string_.replace('A', '')
#         string_ = string_.replace('E', '')
#         string_ = string_.replace('I', '')
#         string_ = string_.replace('O', '')
#         string_ = string_.replace('U', '')
#         return(string_)
#
# print(disemvowel('This website is for losers LOL!'))

# def fizzBuzz(num):
#     for n in range(1, num+1):
#         if n % 3 == 0 and n % 5 == 0:
#             print('FizzBuzz')
#         elif n % 5 == 0:
#             print('Buzz')
#         elif n % 3 == 0:
#             print('Fizz')
#         else:
#             print(n)
#
# fizzBuzz(35)



# author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
# 
# # def ln_sort(author):            # Function to find the fist letter of the last Name
# #     for name in author:
# #         if name.count(' ') == 2:
# #             print(name[name.find('. ') + 2])
# #         else:
# #             print(name[name.find(' ') + 1])
# #
# # print(ln_sort(author))
# 
# ln_dict = list(dict(sorted(dict(zip(list(map(lambda name : name[name.find('. ') + 2].lower() if name.count(' ') == 2 else name[name.find(' ') + 1].lower(), author)), author)).items())).values())
# print(ln_dict)



# # F = (9/5)*C + 32
# places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
# 
# my_dict = dict(map(lambda kv: (kv[0], 1.8*(kv[1])+32), dict(places).items()))
# print(my_dict)



# def fib(x):
#     count=0
#     init=0
#     new=1
#     def LocalFib(x, count, init, new):
#         if count == 0:
#             print(f'Iteration {count}: {new}')
#             LocalFib(x, count+1, init, new)
#         elif count <= x:
#             fib_sum = init + new
#             init = new
#             new = fib_sum
#             print(f'Iteration {count}: {new}')
#             LocalFib(x, count+1, init, new)
#     LocalFib(x, count, init, new)
# fib(5)
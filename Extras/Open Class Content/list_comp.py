# x_letters =[]
# for letter in 'human':
#     x_letters.append(letter)

# print(x_letters)

# x_letters = [ letter for letter in 'human' ]
# print(x_letters)

number_list = [x for x in range(50) if x % 2 != 0 if x < 30]
print(number_list)
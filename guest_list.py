# python_practice
Repository for Python Practice Projects from books, courses, etc.
guest_list = ['jack', 'anna', 'leo', 'kiwi']

#prints a welcome message to the guests
print('Welcome to the party, ' + guest_list[0].title() + '!')
print('Welcome to the party, ' + guest_list[1].title() + '!')
print('Welcome to the party, ' + guest_list[2].title() + '!')
print('Welcome to the party, ' + guest_list[3].title() + '!')

print(guest_list[3].title() + ' cannot make it to the party.')

guest_list[3] = 'ruby'

print('Welcome to the party, ' + guest_list[0].title() + '!')
print('Welcome to the party, ' + guest_list[1].title() + '!')
print('Welcome to the party, ' + guest_list[2].title() + '!')
print('Welcome to the party, ' + guest_list[3].title() + '!')

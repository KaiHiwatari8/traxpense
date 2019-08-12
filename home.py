import file_expense as fe
import expense as ex
print('\nWelcome to')
print('¯¯T¯¯ |¯¯\      /\      \    /  |¯¯¯\   |¯¯¯¯  |\    |  |¯¯¯¯  |¯¯¯¯  ')
print('  |   |   \    /  \      \  /   |    \  |      | \   |  |      |      ')
print('  |   |___/   /    \      \/    |____/  |----  |  \  |  |____  |----  ')
print('  |   | \    /------\     /\    |       |      |   \ |      |  |      ')
print('  |   |  \  /        \   /  \   |       |____  |    \|  ____|  |____  ')
print('\n')

print('MENU')

print("1. Enter today's expense")
print("2. View a specific day")
print("3. Exit")
choice = int(input('Enter an option: '))

while choice == 1 or choice == 2:
    if choice == 1:
        text = ex.driver()
        fe.write_to_file(text)
        choice = int(input('\nEnter an option: '))
    elif choice == 2:
        view_file_choice = input('\nEnter the date (yyyy-mm-dd): ')
        fe.open_file(view_file_choice + '.txt')
        choice = int(input('\nEnter an option: '))

print("\nThank you for using traxpense!!\nHave a great day!!")
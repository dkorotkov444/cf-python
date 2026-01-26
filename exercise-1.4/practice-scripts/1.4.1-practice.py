# 1.4.1 Practice Script: Creating a Number List File
# Create a text file that contains a list of numbers from 50 to 100 (inclusive)

with open('number_list.txt', 'w') as list_file:
    number_list = []
    for number in range(50, 100):
        number_list.append(f'{number}\n')
    number_list.append('100')  # Manually append last element to avoid trailing newline at the end of file
    list_file.writelines(number_list)
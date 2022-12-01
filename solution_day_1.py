# This is the solution of Advent of code 2022 Day 1

def advent_of_code_day_one():

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    my_list = []
    calories_of_current_elf = 0
    for i in range(0, len(lines)):
        if lines[i] != '\n':
            calories_of_current_elf += int(lines[i].rstrip('\n'))
        if lines[i] == '\n' or i == len(lines)-1:
            my_list.append(calories_of_current_elf)
            calories_of_current_elf = 0

    my_list.sort()

    answer_of_part_one = max(my_list)
    answer_of_part_two = sum(x for x in my_list[-3:])

    print(answer_of_part_one)
    print(answer_of_part_two)


if __name__ == '__main__':
    advent_of_code_day_one()

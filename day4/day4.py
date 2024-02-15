from collections import defaultdict
#Process input
input_file = 'input.txt'
input = open(input_file, "r")
maxCardNum = 0
def pt1(input):
    global maxCardNum
    total_pts = 0
    for line in input:
        maxCardNum += 1
        _,card_nums = line.split(':')
        win_nums,your_nums = card_nums.split('|')
        win_nums = win_nums.split()
        your_nums = your_nums.split()
        winning_nums = [num for num in your_nums if num in win_nums]
        pts = int(2**(len(winning_nums)-1))
        total_pts += pts
    return total_pts

print("Total scratchcards:", pt1(input))
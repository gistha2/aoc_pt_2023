#Process input
input_file = 'input.txt'
input = open(input_file, "r")

def pt1(input):
    total_pts = 0
    for line in input:
        _,card_nums = line.split(':')
        win_nums,your_nums = card_nums.split('|')
        win_nums = win_nums.split()
        your_nums = your_nums.split()
        winning_nums = [num for num in your_nums if num in win_nums]
        pts = int(2**(len(winning_nums)-1))
        total_pts += pts
    print(total_pts)

def pt2(input):
    
pt1(input)
pt2(input)
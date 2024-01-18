from collections import defaultdict
#Process input
input_file = 'test.txt'
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
    print(total_pts)

def dfs(root, adj_list):
    print("node", root)
    count = 1
    neighbours = adj_list[root]
    for neighbour in neighbours:
        count += dfs(neighbour,adj_list)

    return count


def pt2(input):
    adj_list = defaultdict(list)
    card_idx = 1
    input = open(input_file, "r")
    for line in input:
        _,card_nums = line.split(':')
        win_nums,your_nums = card_nums.split('|')
        win_nums = win_nums.split()
        your_nums = your_nums.split()
        winning_nums = [num for num in your_nums if num in win_nums]
        cards_won = len(winning_nums)
        adj_list[card_idx] = [*range(card_idx+1,min(maxCardNum,card_idx+cards_won+1))]
        card_idx += 1
    
    print(adj_list)
    print(dfs(1,adj_list))


pt1(input)
pt2(input)
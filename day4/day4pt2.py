from collections import defaultdict

def simulate_game(input_file):
    adj_list = defaultdict(list)
    card_idx = 1
    maxCardNum = 1000  # Assuming a maximum card number
    with open(input_file, "r") as input:
        for line in input:
            _, card_nums = line.split(':')
            win_nums, your_nums = card_nums.split('|')
            win_nums = win_nums.split()
            your_nums = your_nums.split()
            winning_nums = [num for num in your_nums if num in win_nums]
            cards_won = len(winning_nums)
            adj_list[card_idx] = [*range(card_idx + 1, min(maxCardNum, card_idx + cards_won + 1))]
            card_idx += 1
    return adj_list

def total_scratchcards(input_file):
    adj_list = simulate_game(input_file)
    scratchcards = {i: 1 for i in adj_list.keys()}
    total_scratchcards = sum(scratchcards.values())
    while True:
        new_scratchcards = {}
        for card, count in scratchcards.items():
            for neighbor in adj_list[card]:
                new_scratchcards[neighbor] = new_scratchcards.get(neighbor, 0) + count
        if not new_scratchcards:
            break
        scratchcards = new_scratchcards
        total_scratchcards += sum(scratchcards.values())
    return total_scratchcards

input_file = "input.txt"  # Provide the correct path to your input file
print("Total scratchcards:", total_scratchcards(input_file))
def adj_symbol(i,j,scheme):
    offsets = [(0,-1),[0,1],[1,0],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
    for a,b in offsets:
        adj_idx = [i+a,j+b]
        if adj_idx[0]>139 or adj_idx[0]<0 or adj_idx[1]>139 or adj_idx[1]<0:
            continue
        adj_char = scheme[adj_idx[0],adj_idx[1]] 
        if not adj_char.isnumeric() and adj_char != '.':
            return True
    return False
    
def pt1(input_file):
    #Open input
    input = open(input_file, "r")
    m = n = len(input.readlines())

    schematic = [ [0]*m for i in range(n)]

    #Populate 2D array for easy indexing 
    input = open(input_file, "r")
    i = 0
    for line in input:
        j = 0
        for c in line.strip():
            schematic[i][j] = c
            j += 1
        i += 1

    for line in schematic:
        stack = []
        part_num_total = 0
        for i,c in enumerate(line):
            if c.isnumeric():
                stack.append([c,i])
            elif stack:
                valid_part_num = False
                for node in stack:
                    if adj_symbol(i,node[1],schematic):
                        valid_part_num = True
                        break

                if valid_part_num:
                    part_num = "".join([row[1] for row in stack])
                    part_num_total += part_num 


        print(stack)

pt1('input.txt')
def adj_symbol(row,col,scheme):
    offsets = [(0,-1),[0,1],[1,0],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
    for a,b in offsets:
        adj_idx = [row+a,col+b]
        if adj_idx[0]>139 or adj_idx[0]<0 or adj_idx[1]>139 or adj_idx[1]<0:
            continue
        adj_char = scheme[adj_idx[0]][adj_idx[1]] 
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
        
    part_num_total = 0
    for row, line in enumerate(schematic):
        stack = []
        eol = False
        for col,c in enumerate(line):
            eol = (col == m-1)
            if c.isnumeric():
                stack.append([c,col])
            if stack and (not c.isnumeric() or eol):
                valid_part_num = False
                for node in stack:
                    if adj_symbol(row,node[1],schematic):
                        valid_part_num = True
                        break
            
                if valid_part_num:
                    part_num = "".join([str(node[0]) for node in stack])
                    part_num_total += int(part_num) 
                stack = []
        #print(stack)
    print(part_num_total)
    

pt1('input.txt')
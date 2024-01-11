input_file = 'input.txt'
partnum_idxs = {}

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

def adj_symbol(row,col,scheme):
    offsets = [(0,-1),[0,1],[1,0],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
    for a,b in offsets:
        adj_idx = [row+a,col+b]
        if adj_idx[0]>n-1 or adj_idx[0]<0 or adj_idx[1]>n-1 or adj_idx[1]<0:
            continue
        adj_char = scheme[adj_idx[0]][adj_idx[1]] 
        if not adj_char.isnumeric() and adj_char != '.':
            return True
    return False
    
def pt1():
    global partnum_idxs
    global schematic 

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
                    part_num = int("".join([str(node[0]) for node in stack]))
                    for node in stack:
                        partnum_idxs[(row,node[1])] = part_num
                    part_num_total += part_num
                stack = []
    print("Part 1 answer is",part_num_total)

def get_gear_ratio(row,col):
    if not partnum_idxs:
        raise Exception("Must run part 1 first")
    adj_count = 0
    adj_partnums = set([])
    offsets = [(0,-1),[0,1],[1,0],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
    for a,b in offsets:
        adj_idx = [row+a,col+b]
        if adj_idx[0]>n-1 or adj_idx[0]<0 or adj_idx[1]>n-1 or adj_idx[1]<0:
            continue
        if (adj_idx[0],adj_idx[1]) in partnum_idxs:
            adj_partnums.add((partnum_idxs[(adj_idx[0],adj_idx[1])],adj_idx[0]))
    
    if len(adj_partnums) == 2:
        return adj_partnums.pop()[0]*adj_partnums.pop()[0]
    else:
        return -1 

#NB: MUST run pt1 first to populate global schematic and partnum_idxs var
def pt2():
    if not partnum_idxs:
        raise Exception("Must run part 1 first")
    gear_ratio_total = 0
    for row, line in enumerate(schematic):
        for col, c in enumerate(line):
            if c=='*':
                gear_ratio = get_gear_ratio(row,col)
                if gear_ratio != -1:
                    gear_ratio_total += gear_ratio
    print("Part 2 answer is ", gear_ratio_total)
                
pt1()
pt2()

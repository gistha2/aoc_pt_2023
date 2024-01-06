def value_before(val,in_list):
    try:
        return int(in_list[in_list.index(val) -1])
    except ValueError:
        return float('-inf')
    
def pt1(input_file):
    input = open(input_file, "r")
    rgb_limits = [12,13,14]
    valid_ID_total = 0
    for line in input:
        line_split = line.split(':')
        game_num = int(list(filter(lambda x: x.isdigit(), line_split[0].split()))[0])
        samples = line_split[1].split(';')
        valid = True
        for sample in samples:
            cube_colours = sample.split()
            cube_colours = [s.strip(',') for s in cube_colours]
            r = value_before('red',cube_colours)
            g = value_before('green',cube_colours)
            b = value_before('blue', cube_colours)
            if r>rgb_limits[0] or g>rgb_limits[1] or b>rgb_limits[2]:
                valid = False
                break

        if valid:
            valid_ID_total += game_num
    print(valid_ID_total)

  
def pt2(input_file):
    input = open(input_file, "r")
    set_total = 0
    for line in input:
        line_split = line.split(':')
        game_num = int(list(filter(lambda x: x.isdigit(), line_split[0].split()))[0])
        samples = line_split[1].split(';')
        valid = True
        r_max = 0
        g_max = 0
        b_max = 0
        for sample in samples:
            cube_colours = sample.split()
            cube_colours = [s.strip(',') for s in cube_colours]
            r = value_before('red',cube_colours)
            g = value_before('green',cube_colours)
            b = value_before('blue', cube_colours)
            r_max = max(r_max,r)
            g_max = max(g_max,g)
            b_max = max(b_max,b)
        
        power = r_max*g_max*b_max
        set_total += power

    print(set_total)

#pt1('input.txt')
pt2('input.txt')
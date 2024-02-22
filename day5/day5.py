
def create_map_function(ranges): 
     def _(x):
        x = int(x)
        for r in ranges:
            if x>=r[1] and x<=r[1]+r[2]:
                return r[0]+(x-r[1])
        return x 
     return _

def process_almanac(input_file):
    seed_nos = []
    input = open(input_file, "r")
    temp_ranges = []
    map_list = []

    for line in input:
        if 'seeds' in line:
            seed_nos = line.split('seeds:')[1].split()
        elif line.isspace():
            if temp_ranges:
                map_list.append(create_map_function(temp_ranges))        
        elif line.upper().isupper():
            temp_ranges = []
        else: 
            temp_ranges.append(line.split())
            temp_ranges[-1] = [ int(x) for x in temp_ranges[-1] ]

    location_nums = []
    for seed_num in seed_nos:
        new_num = seed_num
        for map in map_list:
            new_num = map(new_num)
        location_nums.append(new_num)
    print(location_nums)
    return min(location_nums)

input_file = 'test.txt'
print(process_almanac(input_file))
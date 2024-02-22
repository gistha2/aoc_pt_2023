
def create_map_function(ranges): 
     def _(x):
        return x * ranges
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


            
    return map_list[0](1)

input_file = 'test.txt'
print(process_almanac(input_file))
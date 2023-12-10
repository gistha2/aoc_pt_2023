import re
def calibration_sum(input_file):
    input = open(input_file, "r")
    calibration_sum = 0
    for line in input:
        calibration_value = ''
        #forward scan to find first digit
        for c in line:
            if c.isnumeric():
                calibration_value += c
                break
        #backward scan to find last digit
        for c in line[::-1]:
            if c.isnumeric():
                calibration_value += c
                break
        #calibration value for this line to total sum
        calibration_sum += int(calibration_value)
        
    return calibration_sum

def pt2(input_file):
    input = open(input_file, "r")
    calibration_sum = 0
    digit_dict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    for line in input:
        stack = ''
        calibration_value = ''
        regex_str = '(zero|one|two|three|four|five|six|seven|eight|nine)'

        #forward scan to find first digit, use regex to match words
        for c in line:
            stack += c
            if c.isnumeric():
                calibration_value += c
                stack = ''
                break
            else:
                match_obj = re.search(regex_str, stack)
                if match_obj:
                    calibration_value += str(digit_dict[match_obj.group()])
                    stack = ''
                    break

        #backward scan to find last digit, add to stack in reverse order
        for c in line[::-1]:
            stack = c + stack
            if c.isnumeric():
                calibration_value += c
                stack = ''
                break
            else:
                match_obj = re.search(regex_str, stack)
                if match_obj:
                    calibration_value += str(digit_dict[match_obj.group()])
                    stack = ''
                    break

        #calibration value for this line to total sum
        calibration_sum += int(calibration_value)
    
    return calibration_sum


print(calibration_sum("input.txt"))
print(pt2("input.txt"))


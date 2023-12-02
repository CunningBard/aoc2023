with open("input.txt") as f:
    data = f.readlines()


interchange = {
    "zero":  "0",
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

no_sum = 0
nums = []
for line in data:
    index = 0
    while index < len(line):
        word = ""
        char = line[index]
        if char in list("0123456789"):
            nums.append(char)
            index += 1
            continue

        temp_index = index
        while temp_index < len(line):
            word += char

            if word in interchange:
                nums.append(interchange[word])
                break

            temp_index += 1
            if temp_index >= len(line):
                break

            char = line[temp_index]
            if char in list("0123456789"):
                break
            
        
        index += 1
    
    no_sum += int(nums[0] + nums[-1])
    nums = []
    
print(no_sum)
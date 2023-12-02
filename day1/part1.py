with open("input.txt") as f:
    data = f.readlines()

no_sum = 0
nums = []
for line in data:
    for char in line:
        if not char in list("0123456789"):
            continue
            
        nums.append(char)

    no_sum += int(nums[0] + nums[-1])
    nums = []

print(no_sum)
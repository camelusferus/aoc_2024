input = open("input/input_05.txt").read().strip().split("\n\n")
rules = [rule.split("|") for rule in input[0].split("\n")]
actions = [rule.split(",") for rule in input[1].split("\n")]
correctness_check = lambda action: True if all([True if update[0] == len(action)+1 or
                all([True if ([update[1],a] in rules) and ([a,update[1]] not in rules) else False for a in action[update[0]+1:]])
                else False for update in enumerate(action)]) else False
incorrect = [action for action in actions if not correctness_check(action)]
correct = []
for piece in incorrect:
    corrected = []
    for a in piece:
        for i in range(len(corrected)+1):
            if correctness_check(corrected[:i]+[a,]+corrected[i:]):
                corrected = corrected[:i]+[a,]+corrected[i:]
                continue
    correct.append(corrected)
print(sum([int(action[len(action)//2]) for action in correct]))
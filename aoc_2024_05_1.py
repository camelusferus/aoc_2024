input = open("input/input_05.txt").read().strip().split("\n\n")
rules = [rule.split("|") for rule in input[0].split("\n")]
actions = [rule.split(",") for rule in input[1].split("\n")]
correct = [action for action in actions if
           all([True if update[0] == len(action)+1 or
                all([True if ([update[1],a] in rules) and ([a,update[1]] not in rules) else False for a in action[update[0]+1:]])
                else False for update in enumerate(action)])]
print(sum([int(action[len(action)//2]) for action in correct]))

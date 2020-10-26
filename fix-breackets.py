def fix_brackets(s):
    counter_fix = 0
    counter_balance = 0
    for c in s:
        if c == "(":
            counter_balance += 1
        elif c == ")":
            if counter_balance > 0:
                counter_balance -= 1
            else:
                counter_fix += 1
    return counter_fix + counter_balance

def brackets_ok(s):
    return fix_brackets(s) == 0

print(fix_brackets('(()()'))
# 1
print(brackets_ok('(()()'))
# false
print(fix_brackets('(()())'))
# 0
print(brackets_ok('(()())'))
# true
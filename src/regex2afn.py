import re

postfix = "ab.*c+"

regex = ''.join(postfix)

keys = list(set(re.sub('[^A-Za-z0-9]+', '', regex)+'e'))

states = []
stack = []
start = 0
end = 1
counter = -1
c1 = 0
c2 = 0

for i in regex:
    if i in keys:
        counter = counter+1
        c1 = counter
        counter = counter+1
        c2 = counter
        states.append({})
        states.append({})
        stack.append([c1, c2])
        states[c1][i] = c2
    elif i == '*':
        r1, r2 = stack.pop()
        counter = counter+1
        c1 = counter
        counter = counter+1
        c2 = counter
        states.append({})
        states.append({})
        stack.append([c1, c2])
        states[r2]['e'] = (r1, c2)
        states[c1]['e'] = (r1, c2)
        if start == r1:
            start = c1
        if end == r2:
            end = c2
    elif i == '.':
        r11, r12 = stack.pop()
        r21, r22 = stack.pop()
        stack.append([r21, r12])
        states[r22]['e'] = r11
        if start == r11:
            start = r21
        if end == r22:
            end = r12
    else:
        counter = counter+1
        c1 = counter
        counter = counter+1
        c2 = counter
        states.append({})
        states.append({})
        r11, r12 = stack.pop()
        r21, r22 = stack.pop()
        stack.append([c1, c2])
        states[c1]['e'] = (r21, r11)
        states[r12]['e'] = c2
        states[r22]['e'] = c2
        if start == r11 or start == r21:
            start = c1
        if end == r22 or end == r12:
            end = c2

print("Inputs:", keys)

print("AFN transitions:", states)

print("\nTransition table:")

print("States:\t| Transitions:")
for i in range(len(states)):
    state = "->{}".format(i) if i == start else "*{}".format(i) if i == end else i
    print("{: >3}:\t| {}".format(state, states[i]))
print("")

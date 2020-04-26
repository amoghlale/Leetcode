Solution 1:
ord_values = []
for char in s:
    if len(ord_values) != 0:
        if ord_values[-1] == 40 and ord(char) == 41 or ord_values[-1] == 91 and ord(char) == 93 or ord_values[-1] == 123 and ord(char) == 125:
            ord_values.pop()
        else:
            ord_values.append(ord(char))
    else:
        ord_values.append(ord(char))
return True if len(ord_values) == 0 else False

Solution 2:
brackets = {'(': ')', '{': '}', '[': ']'}
output_list = []
for char in s:
    if len(output_list) != 0:
        if output_list[-1] in brackets and brackets[output_list[-1]] == char:
            output_list.pop()
        else:
            output_list.append(char)
    else:
        output_list.append(char)
return True if len(output_list) == 0 else False

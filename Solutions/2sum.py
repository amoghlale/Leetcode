def solution(input_list, given_number):
    """Function to find all pairs having sum = given_number"""
    expected_output = []
    i = 0
    j = len(input_list) - 1
    input_list = sorted(input_list)
    while i < j:
        if input_list[i] + input_list[j] == given_number:
            if [input_list[i], input_list[j]] not in expected_output:
                expected_output.append(
                    [input_list[i], input_list[j]])
            i += 1
        if input_list[i] + input_list[j] < given_number:
            i += 1
        if input_list[i] + input_list[j] > given_number:
            j -= 1
    print(expected_output)

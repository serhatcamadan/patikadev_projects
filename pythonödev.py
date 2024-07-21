# 1
def flatten_list(input_list):
    flattened = []
    for element in input_list:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)
    return flattened


input_data = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_data = flatten_list(input_data)
print(output_data)  
# 2
def reverse_nested_list(input_list):
    reversed_list = []
    for element in input_list[::-1]:
        if isinstance(element, list):
            reversed_list.append(reverse_nested_list(element))
        else:
            reversed_list.append(element)
    return reversed_list


input_data = [[1, 2], [3, 4], [5, 6, 7]]
output_data = reverse_nested_list(input_data)
print(output_data)  

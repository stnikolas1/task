def calculate_structure_sum(data_structure):
    total_sum=0
    if isinstance(data_structure, list):
        for i in data_structure:
            sum_ = calculate_structure_sum(i)
            total_sum += sum_
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_ = calculate_structure_sum(key)
            total_sum += sum_
            sum_ = calculate_structure_sum(value)
            total_sum += sum_
    elif isinstance(data_structure, set):
        for i in data_structure:
            sum_ = calculate_structure_sum(i)
            total_sum += sum_
    elif isinstance(data_structure, tuple):
        for i in data_structure:
            sum_ = calculate_structure_sum(i)
            total_sum += sum_
    elif isinstance(data_structure, (int, float)):
        total_sum += data_structure
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)
    return total_sum
a = [[1, 2, 3], {'a': 4,'b': 5}, (6,{'cube': 7,'drum': 8}), 'Hello', ((),[{(2, 'Urban', ('Urban2', 35))}])]
a = calculate_structure_sum(a)
print(a)




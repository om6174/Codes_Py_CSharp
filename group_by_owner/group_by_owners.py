#assuming correct inputs for the sake of simplicity
import collections
def group_by_owners(input_dict):
    output_dict = collections.defaultdict(list)
    [output_dict[value].append(key) for key, value in input_dict.items()]
    return dict(output_dict)
print(group_by_owners({'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}))


#output{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

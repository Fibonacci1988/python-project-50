import argparse
import json


def generate_diff(first_file, second_file):
    # Load the data from the first and second files
    with open(first_file) as f:
        first_data = json.load(f)
    with open(second_file) as f:
        second_data = json.load(f)


    # Create a set of keys from the first file and a set of keys from the second file
    first_keys = set(first_data.keys())
    second_keys = set(second_data.keys())


    # Find the keys that are in both sets, the keys that are only in the first set, and the keys that are only in the second set
    all_keys = first_keys.union(second_keys)
    first_only_keys = first_keys - second_keys
    second_only_keys = second_keys - first_keys


    # Initialize an empty list for the diff
    diff = []


    # Sort the keys that are in both sets
    sorted_all_keys = sorted(all_keys)


    # Iterate over the sorted keys that are in both sets and compare the values
    for key in sorted_all_keys:
        if key in first_only_keys:
            diff.append(f"- {key}: {first_data[key]}")
        elif key in second_only_keys:
            diff.append(f"+ {key}: {second_data[key]}")
        else: 
            if first_data[key] == second_data[key]:
                diff.append(f"  {key}: {first_data[key]}")
            else:
                diff.append(f"- {key}: {first_data[key]}")
                diff.append(f"+ {key}: {second_data[key]}")

    # Join the diff list into a single string, with newlines between each element
    return "\n".join(diff)

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',help='set format of output')
    # Parse the command-line arguments
    args = parser.parse_args()
    #print(args)
    diff = generate_diff('file1.json', 'file2.json')
    print(diff)


if __name__ == '__main__':
    main()

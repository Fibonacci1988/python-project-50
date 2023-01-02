import argparse


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    # Add the positional arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Parse the command-line arguments
    args = parser.parse_args()


if __name__ == '__main__':
    main()

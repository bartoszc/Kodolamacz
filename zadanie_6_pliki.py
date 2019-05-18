
input_line = input('Enter the name of the input file: ')
output_line = input('Enter the name of the output file: ')

try:
    with open(input_line) as f:
        lines = f.readlines()
    print(f'Number of lines = {len(lines)}')

    with open(output_line, 'w') as f:
        f.writelines([output_line, '\n', str(len(lines))])
except FileNotFoundError:
    print('File not found')


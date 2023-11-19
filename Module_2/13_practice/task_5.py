def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        i = 1
        for line in file:
            if 'ERROR' in line.strip():
                yield i, line
            i += 1


with open('output.log', 'w') as out_file:
    for line_num, error in error_log_generator('input.log'):
        out_file.write(str(line_num) + " " + error)

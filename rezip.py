def get_text(filepath):
    ''' get the list of rows of text file '''
    with open(filepath, "r") as file:
        lst = [row.strip() for row in file.readlines()]
    return lst
    

def zip_line(line):
    ''' compress the given line '''
    result = []
    common = {'0': 'a',
            '1': 'to',
            '2': 'the', 
            '3': 'be', 
            '4': 'of', 
            '5': 'and', 
            '6': 'in', 
            '7': 'at', 
            '8': 'on', 
            '9': 'in'}
    for token in line.split():
        if token in common:
            result.append(str(common[token]))
        else:
            result.append(token)
    return ' '.join(result)


def restore(filepath):
    text = get_text(filepath)
    splitted = filepath.split('/')
    new_filepath = '/'.join(splitted[:-1]) + f'/decompressed_{splitted[-1]}'
    with open(new_filepath, 'w') as f:
        for line in text:
            zipped = zip_line(line)
            f.write(zipped + '\n')

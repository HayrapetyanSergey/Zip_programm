def get_text(filepath):
    ''' get the list of rows of text file '''
    with open(filepath, "r") as file:
        lst = [row.strip() for row in file.readlines()]
    return lst
    

def zip_line(line):
    ''' compress the given line '''
    result = []
    common = {'a': 0, 'A': 0,
            'to': 1, 'To' : 1,
            'the': 2, 'The': 2,
            'be': 3,'Be': 3, 
            'of': 4, 'Of': 4,
            'and': 5, 'And': 5,
            'in': 6, 'In': 6,
            'at': 7, 'At': 7,
            'on': 8, 'On': 8,
            'in': 9, 'In': 9}
    for token in line.split():
        if token in common:
            result.append(str(common[token]))
        else:
            result.append(token)
    return ' '.join(result)


def create(filepath):
    text = get_text(filepath)
    splitted = filepath.split('/')
    new_filepath = '/'.join(splitted[:-1]) + f'/compressed_{splitted[-1]}'
    with open(new_filepath, 'w') as f:
        for line in text:
            zipped = zip_line(line)
            f.write(zipped + '\n')
def rendering(source, j=0):
    result = '{' + '\n'
    for i in list(source.keys()):
        if isinstance(source[i], dict):
            result = result + ('\t' * j) + i + ': ' +\
                     rendering(source[i], j+1) + '\n'
        else:
            if i[0] != ' ':
                result = result + ('\t' * (j + 1)) + i +\
                         ': ' + str(source[i]) + '\n'
            else:
                result = result + ('\t' * j) + i +\
                         ': ' + str(source[i]) + '\n'
    if result[-1] == '}':
        result = result + '\n' + '}'
    else:
        result = result + ('\t' * j) + '}'
    return result

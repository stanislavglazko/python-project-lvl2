def plain(source, j=''):
    result = ''
    keys_list = list(source.keys())
    for i in keys_list:
        if i[2] == ' ':
            if isinstance(source[i], dict):
                result = result + plain(source[i], j=j+str(i[4:]) + '.')
        elif i[2] == '-':
            analog = '  + ' + i[4:]
            if (analog) in keys_list:
                result += "Property '" + str(j) + i[4:] +\
                          "' was changed." + "From '" +\
                          str(source[i]) + "' to '" +\
                          str(source[analog]) + "'" + '\n'
                analog = keys_list.index(analog)
                keys_list.pop(analog)
            else:
                result += "Property '" + str(j) + i[4:] +\
                          "' was removed" + '\n'
        elif i[2] == '+':
            if isinstance(source[i], dict):
                result += "Property '" + str(j) + i[4:] +\
                          "' was added with value: " +\
                          "'complex value'" + '\n'
            else:
                analog = '  - ' + i[4:]
                if (analog) in keys_list:
                    result += "Property '" + str(j) + i[4:] +\
                              "' was changed." + " From '" +\
                              str(source[analog]) + "' to '" +\
                              str(source[i]) + "'" + '\n'
                    analog = keys_list.index(analog)
                    keys_list.pop(analog)
                else:
                    result += "Property '" + str(j) + i[4:] +\
                              "' was added with value: " +\
                              "'" + str(source[i]) + "'" + '\n'
    return result

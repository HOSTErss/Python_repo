
def write_str_info(a, f):
    f.write('[')
    for each in a: 
        if isinstance(each, str):
            f.write(each)
            if each != a[-1]:
                f.write(', ')
        else:
            write_str_info(each, f)
    f.write(']')


if __name__ == '__main__':
    a = ['123', ['123', '456']]

    with open('D:\\Code-source\\python_source\\python\\str_info', 'w') as f:
        write_str_info(a, f)
        
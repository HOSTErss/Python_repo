
if __name__ == "__main__":
    with open("D:\\Code-source\\python_source\\python\\test.txt", 'r') as f:
        info = f.readline()
    
    l1 = info.split(' ')
    max_len = 0
    max_word = ''
    for each in l1:
        len_each = len(each)
        if  len_each < max_len:
            continue
        if not each.isalpha():
            continue
        max_len = len_each
        max_word = each
         
    print(max_word)
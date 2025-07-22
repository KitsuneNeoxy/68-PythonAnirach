def format_string(*args):
    return ''.join(args).upper().replace(' ','-')

if __name__ == '__main__':
    result = format_string("Hello", "world", "this","is","a","test")
    print(result)


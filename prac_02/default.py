def print_line(length=3, line='-'):
    """Prints length of 'line' characters"""
    print(line * length)


print_line()  # ---
print_line(5)  # -----
print_line(4, '&')  # &&&&
print_line(line='&')  # &&&


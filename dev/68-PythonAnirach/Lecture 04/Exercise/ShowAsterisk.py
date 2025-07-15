Rows = int(input('How many rows: '))
Columns = int(input('How many Columns: '))
print(('\n'+(Columns * '*')) * Rows if Columns > 0 else None)

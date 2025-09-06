def build_a_wall(x=None, y=None):
    wallString = ""
    row_string = ""

    if not isinstance(x, int) or not isinstance(y, int):
        return None
    
    elif  x < 1 or y < 1:
        return None
    
    elif x * y > 10000:
        return "Naah, too much...here's my resignation."
    
    else:
        for row in range(x):
            if not row % 2 == 0:
                row_string += "■|" + ("■■|" * (y - 1)) + "■" 
                
            elif row % 2 == 0:
                row_string += "■■|" * (y - 1) + "■■"
            
            if row != x - 1:
                row_string += "\n"

        wallString += row_string

        return wallString

print(build_a_wall(5, 5))
print("\nShould be Equal to:\n■■|■■|■■|■■|■■\n■|■■|■■|■■|■■|■\n■■|■■|■■|■■|■■\n■|■■|■■|■■|■■|■\n■■|■■|■■|■■|■■")

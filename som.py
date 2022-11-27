nummer = 50
totaal = 50
output = ""
while totaal < 1000:
    nummer += 1
    totaal += nummer
    output += f" + {nummer}"
    print(f"50{output} = {totaal}")  
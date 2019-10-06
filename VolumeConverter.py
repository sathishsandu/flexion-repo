

# convert everything to tablespoons UOM
toT = { 'liters': (lambda l: l * 67.628),
        'gallons': (lambda g: g * 256),
        'cups': (lambda c: c * 16),
        'cubicInches': (lambda ci: ci * 1.10823),
        'cubicFeet': (lambda cf: cf * 1915.01),
        'tablespoons': (lambda t: t) }

magnitude, unit = input('<value> <tablespoons/cups/liters/gallons> ? ').split()
t = toT[unit](float(magnitude))
# noW convert back from tablespoons to each UOM
litersValue = t * 0.0147868
gallonsValue = t * 0.00390625
cupsValue =  t * 0.0625
cubicInchesValue = t * 0.902344
cubicFeetValue = t * 0.00052219
tablespoonsValue = t

print("litersValue is:", litersValue)
print("gallonsValue is:", gallonsValue)
print("cupsValue is:", cupsValue)
print("cubicInchesValue is:", cubicInchesValue)
print("cubicFeetValue is:", cubicFeetValue)
print("tablespoonsValue is:", tablespoonsValue)


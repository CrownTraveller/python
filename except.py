hr = input("Enter your hours:")
rt = input("Enter your hour rate:")
rh = float(hr)
tr = float(rt)

if rh > 40:
#    print('Overtime')
    regular = rh * tr
    over = (rh - 40) * (tr * 0.5)
    total = regular + over
else:
    #print('Regular')
    total = float(hr)*float(rt)

print('Pay is:', total)

if 5 > 3:
 print('yeeee')

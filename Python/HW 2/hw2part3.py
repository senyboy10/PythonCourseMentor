"""

Author: ALSENY SYLLA

This code asks the user for the height and width of a box, computes the area, and then creates the box, placing the dimensions inside the box if possible.


"""
height = int(raw_input("Height==> "))
print height

width = int(raw_input("Width==> "))
print width

area = height * width 
hw = "h: " + str(height) + ', w: ' + str(width)
area1 = 'area: ' +  str(area)
rect = ("\n" + "*" + ' ' * (width - 2) + "*")
rect_t = rect * (height - 2)
rect_else = ("\n" + "*" + ' ' * (width - 2) + "*") * ((height/2) - 2)


if len(hw) + 3 > width:
    print "*" * width + rect_t + "\n" + "*" * width    
    print hw
    print area1    
    
else:
    sp1 = ' ' * (width - len(hw) - 3) + "*\n" 
    sp2 = ' ' * (width - len(area1) - 3) + "*"
    print "*" * width + rect_else + "\n* " + hw + sp1 + "* " + area1 + sp2 + rect_else + "\n" + "*" * width
    
    
    
    
    

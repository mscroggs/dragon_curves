def dragon(n):
    """Returns a list of 0s and 1s representing the order n dragon curve."""
    if n <= 1:
        return [1]
    prev = dragon(n-1)
    prev_s = prev[:]
    mid = len(prev_s) / 2
    prev_s[mid] = 1-prev_s[mid]
    return prev + [1] + prev_s


def dragon_arc(n,xst=0,yst=0,size=1500,dir_deg=None,dir_rad=None,angle_deg=None,angle_rad=None):
    """Returns the svgwrite commands to draw an order n dragon curve."""
    from math import pi,sqrt,cos,sin

    angle = pi/2
    if angle_deg is not None:
        angle = angle_deg*pi/180
    if angle_rad is not None:
        angle = angle_rad

    dir = 0
    if dir_deg is not None:
        dir = dir_deg*pi/180
    if dir_rad is not None:
        dir = dir_rad

    ls = dragon(n)
    my_d = "M"+str(size[0]/2+xst)+","+str(size[1]/2+yst)
    length = sqrt(50-50*cos(angle))
    for l in ls:
        my_d += " a5,5 0 0,"+str(l)
        if l==0:
            dir += angle/2
        else:
            dir -= angle/2
        my_d += " "
        my_d += str(length*cos(dir))
        my_d += ","        
        my_d += str(-length*sin(dir))
        if l==0:
            dir += angle/2
        else:
            dir -= angle/2

        """if dir=="y+":
            if l==0:
                my_d += " 5,5"
                dir = "x+"
            else:
                my_d += " -5,5"
                dir = "x-"
        elif dir=="y-":
            if l==0:
                my_d += " -5,-5"
                dir = "x-"
            else:
                my_d += " 5,-5"
                dir = "x+"
        elif dir=="x+":
            if l==0:
                my_d += " 5,-5"
                dir = "y-"
            else:
                my_d += " 5,5"
                dir = "y+"
        elif dir=="x-":
            if l==0:
                my_d += " -5,5"
                dir = "y+"
            else:
                my_d += " -5,-5"
                dir = "y-"""
    return my_d


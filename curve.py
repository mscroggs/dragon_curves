from random import choice

def dragon(n):
    if n==1:
        return [1]
    prev = dragon(n-1)
    return prev + [1]+ swap_middle(prev) 

def swap_middle(ls):
    mid = len(ls) / 2
    ls[mid] = 1-ls[mid]
    return ls

def dragon_arc(n,dir,xst=0,yst=0,size=1500,reverse=False):
    #pos = [0,0]
    ls = dragon(n)
    if reverse:
#        ls = [1-l for l in ls]
        pass
    my_d = "M"+str(size/2+xst)+","+str(size/2+yst)
    for l in ls:
        my_d += " a5,5 0 0,"+str(l)
        if dir=="y+":
            if l==0:
                my_d += " 5,5"
                #pos[0]+=5
                #pos[1]+=5
                dir = "x+"
            else:
                my_d += " -5,5"
                #pos[0]+=-5
                #pos[1]+=5
                dir = "x-"
        elif dir=="y-":
            if l==0:
                my_d += " -5,-5"
                #pos[0]+=-5
                #pos[1]+=-5
                dir = "x-"
            else:
                my_d += " 5,-5"
                #pos[0]+=5
                #pos[1]+=-5
                dir = "x+"
        elif dir=="x+":
            if l==0:
                my_d += " 5,-5"
                #pos[0]+=5
                #pos[1]+=-5
                dir = "y-"
            else:
                my_d += " 5,5"
                #pos[0]+=5
                #pos[1]+=5
                dir = "y+"
        elif dir=="x-":
            if l==0:
                my_d += " -5,5"
                #pos[0]+=-5
                #pos[1]+=5
                dir = "y+"
            else:
                my_d += " -5,-5"
                #pos[0]+=-5
                #pos[1]+=-5
                dir = "y-"
    #print pos
    return my_d


n=10
size=2500
import svgwrite
svg_document = svgwrite.Drawing(filename = "four_dragons_"+str(n)+"_white.svg",
                                size = (str(size)+"px", str(size)+"px"),
                                debug=False
                               )
svg_document.add(svg_document.rect(insert=(0, 0), size=(size,size),
                        fill='black', stroke='none'))
svg_document.add(svg_document.path(
                 d=dragon_arc(n,"y+",0,5,size),
                 stroke="#FFFFFF",#"#FF5C00",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(n,"y-",0,-5,size),
                 stroke="#333333",#"#00ce81",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(n,"x+",5,0,size),
                 stroke="#333333",#"#005CFF",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(n,"x-",-5,0,size),
                 stroke="#333333",#"#FFFFFF",
                 stroke_width = "2",
                 fill = "none"
                ))

def randcol():
    c = choice(["3","4","5","6","7","8","9","A","B","C","D","E","F"])
    return "#"+c*6

for pos in [(640,0),(320,320),(0,640),
            (1280,0),(960,320),(640,640),(320,960),(0,1280),
            (1920,0),(1600,320),(1280,640),(960,960),(640,1280),(320,1600),(0,1920)]:
    for type in [("x-",-5,0),("x+",5,0),("y-",0,-5),("y+",0,5)]:
        svg_document.add(svg_document.path(
                         d=dragon_arc(n,type[0],pos[0]+type[1],pos[1]+type[2],size),
                         stroke=randcol(),
                         stroke_width = "2",
                         fill = "none"
                        ))
        if pos[0]!=0 and pos[1]!=0:
            svg_document.add(svg_document.path(
                         d=dragon_arc(n,type[0],-pos[0]+type[1],-pos[1]+type[2],size),
                         stroke=randcol(),
                         stroke_width = "2",
                         fill = "none"
                        ))
        if pos[1]!=0:
            svg_document.add(svg_document.path(
                         d=dragon_arc(n,type[0],pos[0]+type[1],-pos[1]+type[2],size),
                         stroke=randcol(),
                         stroke_width = "2",
                         fill = "none"
                        ))
        if pos[0]!=0:
            svg_document.add(svg_document.path(
                         d=dragon_arc(n,type[0],-pos[0]+type[1],pos[1]+type[2],size),
                         stroke=randcol(),
                         stroke_width = "2",
                         fill = "none"
                        ))
        print pos,type[0]

    
print "Saving..."
svg_document.save()
print "Done"

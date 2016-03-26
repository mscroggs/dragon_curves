######################################################
# This file will draw four randonly coloured dragons #
######################################################

from random import choice,randrange
from core import dragon_arc
import svgwrite

def randcol():
    out = "#"
    for i in range(6):
        out += choice(["3","4","5","6","7","8","9","A","B","C","D","E","F"])
    return out


width = 800
# create a blank svg of the right size
svg_document = svgwrite.Drawing(filename = "four_dragons.svg",
                                size = (str(width)+"px", str(width)+"px"),
                                debug=False
                               )
# fill the background with white
svg_document.add(svg_document.rect(insert=(0, 0), size=(width,width),
                        fill='black', stroke='none'))
# draw the dragon curves in black
svg_document.add(svg_document.path(
                 d=dragon_arc(randrange(2,11),xst=width/2+5,yst=width/2,dir_deg=0),
                 stroke=randcol(),
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(randrange(2,11),xst=width/2,yst=width/2+5,dir_deg=-90),
                 stroke=randcol(),
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(randrange(2,11),xst=width/2-5,yst=width/2,dir_deg=180),
                 stroke=randcol(),
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(randrange(2,11),xst=width/2,yst=width/2-5,dir_deg=90),
                 stroke=randcol(),
                 stroke_width = "2",
                 fill = "none"
                ))

# save the svg
svg_document.save()

######################################################
# This file will draw a dragon curves or orders 1-10 #
######################################################

from random import choice
from core import dragon_arc
import svgwrite

def make_a_str(n):
    if n<10:
        return str(n)
    if n==10:
        return "A"

# create a blank svg of the right size
svg_document = svgwrite.Drawing(filename = "dragons1to10.svg",
                                size = ("500px", "330px"),
                                debug=False
                               )
# fill the background with white
svg_document.add(svg_document.rect(insert=(0, 0), size=(500,330),
                        fill='white', stroke='none'))
# draw the dragon curve in black
for i in reversed(range(1,11)):
    svg_document.add(svg_document.path(
                     d=dragon_arc(i,xst=380,yst=120,dir_deg=-90),
                     stroke="#"+make_a_str(i)*6,
                     stroke_width = "2",
                     fill = "none"
                    ))

# save the svg
svg_document.save()

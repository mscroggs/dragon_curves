##################################################
# This file will draw a dragon curve or order 10 #
##################################################

from random import choice
from core import dragon_arc
import svgwrite

# create a blank svg of the right size
svg_document = svgwrite.Drawing(filename = "dragon10.svg",
                                size = ("500px", "330px"),
                                debug=False
                               )
# fill the background with white
svg_document.add(svg_document.rect(insert=(0, 0), size=(500,330),
                        fill='white', stroke='none'))
# draw the dragon curve in black
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=130,yst=-55,size=(500,330),dir_deg=-90),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))

# save the svg
svg_document.save()

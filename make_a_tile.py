##################################################
# This file will draw a dragon curve or order 10 #
##################################################

from random import choice
from core import dragon_arc
import svgwrite

# create a blank svg of the right size
svg_document = svgwrite.Drawing(filename = "tile.svg",
                                size = ("320px", "320px"),
                                debug=False
                               )
# fill the background with white
svg_document.add(svg_document.rect(insert=(0, 0), size=(320,320),
                        fill='white', stroke='none'))
# draw the dragon curves in black
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=88,yst=123,dir_deg=0),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=83,yst=128,dir_deg=-90),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=78,yst=123,dir_deg=180),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=83,yst=118,dir_deg=90),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=408,yst=-197,dir_deg=0),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=403,yst=-192,dir_deg=-90),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=398,yst=443,dir_deg=180),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))
svg_document.add(svg_document.path(
                 d=dragon_arc(10,xst=-237,yst=438,dir_deg=90),
                 stroke="#000000",
                 stroke_width = "2",
                 fill = "none"
                ))

# save the svg
svg_document.save()

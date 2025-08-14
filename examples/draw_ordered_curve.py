"""Draw a dragon curves of orders 1-10."""

from dragon_curves import dragon_arc
import svgwrite


def make_a_str(n):
    if n < 10:
        return str(n)
    if n == 10:
        return "A"


# create a blank svg of the right size
svg_document = svgwrite.Drawing(filename="dragons1to10.svg", size=("500px", "330px"), debug=False)
# fill the background with white
svg_document.add(svg_document.rect(insert=(0, 0), size=(500, 330), fill="white", stroke="none"))
# draw the dragon curve in black
for i in reversed(range(1, 11)):
    svg_document.add(
        svg_document.path(
            d=dragon_arc(i, xst=380, yst=120, dir_deg=-90),
            stroke="#AAAAAA" if i == 10 else f"#{i}{i}{i}{i}{i}{i}",
            stroke_width="2",
            fill="none",
        )
    )

# save the svg
svg_document.save()

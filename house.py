import cairo

WIDTH, HEIGHT = 700, 500

def set_rgb_color(context, r, g, b):
    context.set_source_rgb(r / 255, g / 255, b / 255)

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB30, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background Colour
context.set_source_rgb(1, 1, 1)  # White
context.paint()


#Inner Side Wall
context.move_to(100, 200)
context.line_to(100, 350)
context.line_to(270, 450)
context.line_to(272, 240)
context.line_to(200, 90)
context.close_path()

context.set_source_rgb(0, 0, 0)
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 216, 165, 141)
context.fill()


# Door handle
context.arc(540, 300, 5, 0, 2 * 3.14159)  # x=500, y=300, radius=10
context.set_source_rgb(1, 1, 0)  # Fill color: yellow
context.fill_preserve()
context.set_source_rgb(0, 0, 0)  # Stroke color: black
context.stroke()

#  Roof Side
context.move_to(90, 200)
context.line_to(200, 80)
context.line_to(205, 78)
context.line_to(295, 260)
context.line_to(290, 270)
context.line_to(200, 90)
context.line_to(90, 210)

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(2)
context.stroke_preserve()

set_rgb_color(context, 185, 48, 17)  # Fill color
context.fill()

context.move_to(295, 260)
context.line_to(612, 182)
context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(2)
context.stroke_preserve()
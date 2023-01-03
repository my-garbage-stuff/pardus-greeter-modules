#!/usr/bin/env python3
# Blur greeter background
from PIL import Image, ImageFilter

mode="RGB"
def pixbuf2image(pix):
    """Convert gdkpixbuf to PIL image"""
    global mode
    data = pix.get_pixels()
    w = pix.props.width
    h = pix.props.height
    stride = pix.props.rowstride
    if pix.props.has_alpha == True:
        mode = "RGBA"
    im = Image.frombytes(mode, (w, h), data, "raw", mode, stride)
    return im

def image2pixbuf(im):
    """Convert Pillow image to GdkPixbuf"""
    data = im.tobytes()
    w, h = im.size
    data = GLib.Bytes.new(data)
    pix = GdkPixbuf.Pixbuf.new_from_bytes(data, GdkPixbuf.Colorspace.RGB,
            (mode=="RGBA"), 8, w, h, w * len(mode))
    return pix


last_pixbuf = None
def blur_draw(widget,context):
    global last_pixbuf
    if loginwindow.background_pixbuf:
        if last_pixbuf != loginwindow.background_pixbuf:
            im = pixbuf2image(loginwindow.background_pixbuf)
            im = im.filter(ImageFilter.GaussianBlur( int(get("level","15","blur")) ))
            loginwindow.background_pixbuf = image2pixbuf(im)
            last_pixbuf = loginwindow.background_pixbuf
            loginwindow.o("ui_window_main").queue_draw()
        Gdk.cairo_set_source_pixbuf(context, self.background_pixbuf, 0, 0)
        context.paint()

def module_init():
    if get("enabled",True,"blur"):
        loginwindow.o("ui_window_main").connect("draw",blur_draw)

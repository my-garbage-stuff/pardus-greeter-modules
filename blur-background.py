#!/usr/bin/env python3
# Blur greeter background
from PIL import Image, ImageFilter

def pixbuf2image(pix):
    """Convert gdkpixbuf to PIL image"""
    data = pix.get_pixels()
    w = pix.props.width
    h = pix.props.height
    stride = pix.props.rowstride
    mode = "RGB"
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
            False, 8, w, h, w * 3)
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
    loginwindow.draw(widget,context)

def module_init():
    if get("enabled",True,"blur"):
        loginwindow.window.connect("draw",blur_draw)

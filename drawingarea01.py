import gi;
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_area_draw(area, context):
    context.scale(area.get_allocated_width(), area.get_allocated_height())
    context.set_source_rgb(0.5, 0.5, 0.7)
    context.fill();
    context.paint();

area=Gtk.DrawingArea()
area.connect('draw', on_area_draw)

win=Gtk.Window()
win.set_size_request(800,600)
win.connect('destroy', Gtk.main_quit)
win.add(area)
win.show_all()

Gtk.main()

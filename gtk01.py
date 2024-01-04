import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

win=Gtk.Window(title='Hi, World!')
win.connect('destroy', Gtk.main_quit)
win.show()

Gtk.main()

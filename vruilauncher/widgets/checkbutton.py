from gi.repository import Gtk

class CheckButton(Gtk.CheckButton):

   def __init__(self, label, settings, key):
      Gtk.CheckButton.__init__(self, label)
      self.settings = settings
      self.set_active(self.settings.get_boolean(key))
      self.connect('clicked', self.on_clicked, key)
      self.settings.connect('changed::{}'.format(key), self.on_remote_update, self)

   def on_clicked(self, button, key):
      self.settings.set_boolean(key, self.get_active())

   def on_remote_update(self, settings, key, button):
      self.set_active(self.settings.get_boolean(key))


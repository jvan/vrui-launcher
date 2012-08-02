from gi.repository import Gtk

class Entry(Gtk.Entry):

   def __init__(self, settings, key):
      Gtk.Entry.__init__(self)
      self.settings = settings
      self.connect('changed', self.on_changed, key)
      self.settings.connect('changed::{}'.format(key), self.on_remote_update, self)
      
      self.on_remote_update(self.settings, key, self)

   def on_changed(self, entry, key):
      self.settings.set_string(key, self.get_text())

   def on_remote_update(self, settings, key, entry):
      print('(Entry.on_remote_update key={})'.format(key))
      self.set_text(self.settings.get_string(key))

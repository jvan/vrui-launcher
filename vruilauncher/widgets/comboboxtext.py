from gi.repository import Gtk

class ComboBoxText(Gtk.ComboBoxText):

   def __init__(self, values, settings, key):
      Gtk.ComboBoxText.__init__(self)
      self.values = values
      self.settings = settings
      for label in self.values:
         self.append_text(label)

      self.connect('changed', self.on_changed, key)
      self.settings.connect('changed::{}'.format(key), self.on_remote_update, self)

      self.on_remote_update(self.settings, key, self)

   def on_changed(self, combobox, key):
      value = combobox.get_active_text()
      self.settings.set_string(key, value)

   def on_remote_update(self, settings, key, combobox):
      print('(ComboBox.on_remote_update key={})'.format(key))
      current = settings.get_string(key)
      print('   (current={})'.format(current))
      for i, label in enumerate(self.values):
         if label == current:
            break
      combobox.set_active(i)

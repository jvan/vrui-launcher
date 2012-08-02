from gi.repository import Gtk

class SpinButton(Gtk.SpinButton):

   def __init__(self, settings, key, min=0.0, max=1.0, step=0.1):
      Gtk.SpinButton.__init__(self)
      self.settings = settings
      value = self.settings.get_double(key)
      adjustment = Gtk.Adjustment(value, min, max, step, 1.0, 0.0)
      self.set_adjustment(adjustment)
      self.set_digits(1)
      self.connect('changed', self.on_changed, key)
      self.settings.connect('changed::{}'.format(key), self.on_remote_update, self)
      
   def on_changed(self, spinbutton, key):
      print('(SpinButton.on_changed key={}, data={})'.format(key, float(self.get_text())))
      self.settings.set_double(key, float(self.get_text()))

   def on_remote_update(self, settings, key, spinbutton):
      data = self.settings.get_double(key)
      print('(SpinButton.on_remote_update key={}, data={})'.format(key, data))
      spinbutton.set_text('{}'.format(data))


from distutils.core import setup
import os

list_files = lambda d: [os.path.join(d, f) for f in os.listdir(d)]

template_files = list_files('templates')
fragment_files = list_files('fragments')

setup(
      name = 'vrui-launcher',
      version = '0.0.1',
      author = 'Jordan Van Aalsburg',
      author_email = 'iviz@lists.cse.ucdavis.edu',
      url = 'https://github.com/comscictr/vrui-launcher',
      description = 'Launcher utility for VRUI applications',
      packages = [ 'vruilauncher', 'vruilauncher.widgets' ],
      scripts = [ 'vrui-launcher', 'vrui-launcher-settings' ],
      data_files = [ 
          ('/usr/share/vrui-launcher/templates', template_files),
          ('/usr/share/vrui-launcher/fragments', fragment_files),
          ('/usr/share/glib-2.0/schemas', ['etc/apps.vrui-launcher.gschema.xml'])
      ]
)


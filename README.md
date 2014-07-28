# vrui-launcher

Vrui-launcher is a launcher program for [VRUI][vrui] applications. It 
allows users to create individual VRUI configurations and has a GUI for easily
changing settings.

Vrui-launcher uses GSettings to store the user's settings and should be run
on a system with the GNOME desktop installed.

[vrui]: http://keckcaves.org/software/vrui


### Installation

On Ubuntu, vrui-launcher can be installed from the [KeckCAVES PPA][keckcaves-ppa].

   ```sh
   sudo add-apt-repository ppa:keckcaves/ppa
   sudo apt-get update
   sudo apt-get install vrui-launcher
   ```

To manually install vrui-launcher, first install the python module and then
compile the GSettings schema.

   ```sh
   sudo python setup.py install
   sudo glib-compile-schemas /usr/share/glib-2.0/schemas
   ```

[keckcaves-ppa]: https://launchpad.net/~keckcaves/+archive/ubuntu/ppa


### Usage

To run a VRUI application with vrui-launcher just add `vrui-launcher` in front
of the command. For example, to run the `ShowEarthModel` example program you 
would call it like this.

   ```sh
   vrui-launcher /usr/bin/ShowEarthModel
   ```

The user's configuration settings will automatically be merged with the system
`Vrui.cfg` file.

If the program is in your `$PATH` you can just use the program name like this.

   ```sh
   vrui-launcher ShowEarthModel
   ```

Arguments can be passed to the program in the normal way. For example, to 
add an arthquake data set to the `ShowEarthModel` program you could do the
following.

   ```sh
   vrui-launcher ShowEarthModel -quakes /path/to/earthquake.anss
   ```

You can even merge additional VRUI config files. This is the command we use to
launch [flow][flow], which has additional config settings for the Razer Hydra
controller.

   ```sh
   vrui-launcher /usr/bin/flow -mergeConfig /etc/flow/RazerMapping.cfg
```

[flow]: https://github.com/chebee7i/flow


### Graphical Interface

There is a graphical interface for easily setting or modifying configuration
values. You can launch it by running the following command in the terminal.

   ```sh
   vrui-launcher-settings
   ```

from gettext import gettext as _

import sys
import pygame

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sugar3.activity import activity
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarBox

sys.path.append('..')  # Import sugargame package from top directory.
import sugargame.canvas

import mcd


class gcdActivity(activity.Activity):
    def __init__(self, handle):
        super(gcdActivity, self).__init__(handle)

        self.paused = False

        # Create the game instance.
        #self.game = TestGame.TestGame()

        # Build the activity toolbar.
        self.build_toolbar()

        # Build the Pygame canvas.
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)

        # Note that set_canvas implicitly calls read_file when resuming from the Journal.
        self.set_canvas(self._pygamecanvas)

        # Start the game running (self.game.run is called when the activity constructor returns).
        self._pygamecanvas.run_pygame(mcd.run())

    def build_toolbar(self):
        stop_play = ToolButton('media-playback-stop')
        stop_play.set_tooltip(_("Stop"))
        stop_play.set_accelerator(_('<ctrl>space'))
        stop_play.connect('clicked', self._stop_play_cb)

        toolbar = Gtk.Toolbar()
        #toolbar.insert(stop_play, 0)

        toolbox = ToolbarBox()
        toolbox.add_toolbar(_("Pygame"), toolbar)

        toolbox.show_all()
        self.set_toolbar_box(toolbox)

    def _stop_play_cb(self, button):
        pass
        # Pause or unpause the game.
        #self.paused = not self.paused
        # self.game.set_paused(self.paused)
        # Update the button to show the next action.
        # if self.paused:
        #    button.set_icon('media-playback-start')
        #    button.set_tooltip(_("Start"))
        # else:
        #    button.set_icon('media-playback-stop')
        #    button.set_tooltip(_("Stop"))

    def read_file(self, file_path):
        mcd.read_file(file_path)

    def write_file(self, file_path):
        mcd.write_file(file_path)

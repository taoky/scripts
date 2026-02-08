from gi.repository import Gio, GObject, Nautilus, GLib
from gettext import gettext
import shlex

_ = gettext
_running = set()  # avoid proc being gc

def spawn_nonblocking(argv):
    proc = Gio.Subprocess.new(argv, Gio.SubprocessFlags.NONE)
    _running.add(proc)

    def on_done(proc, res, data=None):
        try:
            ok = proc.wait_check_finish(res)
        except GLib.Error as e:
            pass
        finally:
            _running.discard(proc)

    proc.wait_check_async(None, on_done)

class OpenWithExtension(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(self, *args):
        files = args[-1]
        if len(files) != 1:
            return
        file_ = files[0]
        items = []

        if file_.get_uri_scheme() == "file":
            item_code = Nautilus.MenuItem(name='NautilusPython::open_in_code',
                                     label=_(u'Open in Code'),
                                     tip=_(u'Open this file or directory in Code'))
            item_code.connect('activate', self._code_callback, file_)
            items.append(item_code)
            if file_.is_directory():
                item_terminal = Nautilus.MenuItem(name='NautilusPython::open_in_terminal',
                                                label=_(u'Open in Terminal'),
                                                tip=_(u'Open this file or directory in Terminal'))
                item_terminal.connect('activate', self._terminal_callback, file_)
                items.append(item_terminal)            
        return items

    def get_background_items(self, *args):
        file_ = args[-1]
        items = []

        if file_.get_uri_scheme() == "file":
            item_code = Nautilus.MenuItem(name='NautilusPython::open_code_bg',
                                     label=_(u'Open Code Here'),
                                     tip=_(u'Open current directory in Code'))
            item_code.connect('activate', self._code_callback, file_)
            item_terminal = Nautilus.MenuItem(name='NautilusPython::open_terminal_bg',
                                                label=_(u'Open Terminal Here'),
                                                tip=_(u'Open current directory in Terminal'))
            item_terminal.connect('activate', self._terminal_callback, file_)
            items.append(item_code)
            items.append(item_terminal)
        return items

    def _code_callback(self, menu, file_):
        filename = Gio.File.new_for_uri(file_.get_uri()).get_path()
        spawn_nonblocking(['code', filename])
    
    def _terminal_callback(self, menu, file_):
        filename = Gio.File.new_for_uri(file_.get_uri()).get_path()
        spawn_nonblocking(['xdg-terminal-exec', f'--dir={shlex.quote(filename)}', '--', 'fish'])

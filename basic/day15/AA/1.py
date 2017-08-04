#Author:Cairo Li
import os
'''
with open("1.txt") as f:
    lines=f.readlines()

for  line in lines:
    if '#dir' in line:
        line=line.replace('#dir','').strip()
        mystr="dir({})".format(line)
        print(eval(mystr))
'''
def splitdrive(p):
    """Split a pathname into drive/UNC sharepoint and relative path specifiers.
    Returns a 2-tuple (drive_or_unc, path); either part may be empty.

    If you assign
        result = splitdrive(p)
    It is always true that:
        result[0] + result[1] == p

    If the path contained a drive letter, drive_or_unc will contain everything
    up to and including the colon.  e.g. splitdrive("c:/dir") returns ("c:", "/dir")

    If the path contained a UNC path, the drive_or_unc will contain the host name
    and share up to but not including the fourth directory separator character.
    e.g. splitdrive("//host/computer/dir") returns ("//host/computer", "/dir")

    Paths cannot contain both a drive letter and a UNC path.

    """
    p = os.fspath(p)
    if len(p) >= 2:
        if isinstance(p, bytes):
            sep = b'\\'
            altsep = b'/'
            colon = b':'
        else:
            sep = '\\'
            altsep = '/'
            colon = ':'
        normp = p.replace(altsep, sep)
        if (normp[0:2] == sep*2) and (normp[2:3] != sep):
            # is a UNC path:
            # vvvvvvvvvvvvvvvvvvvv drive letter or UNC path
            # \\machine\mountpoint\directory\etc\...
            #           directory ^^^^^^^^^^^^^^^
            index = normp.find(sep, 2)
            if index == -1:
                return p[:0], p
            index2 = normp.find(sep, index + 1)
            # a UNC path can't have two slashes in a row
            # (after the initial two)
            if index2 == index + 1:
                return p[:0], p
            if index2 == -1:
                index2 = len(p)
            return p[:index2], p[index2:]
        if normp[1:2] == colon:
            return p[:2], p[2:]
    return p[:0], p

win="C:\\dfs\\df\\dfs"
s="//driver/my/local"
result=splitdrive(win)
print(result)


pathd=os.path.join("C:\cc\dd","txt")
print(pathd)

from .. import gg

self.config = self.make_config(instance_relative_config)
return self.config_class(root_path, self.default_config)
config_class=Config
class Config(dict):
    """Works exactly like a dict but provides ways to fill it from files
    or special dictionaries.  There are two common patterns to populate the
    config.

    Either you can fill the config from a config file::

        app.config.from_pyfile('yourconfig.cfg')

    Or alternatively you can define the configuration options in the
    module that calls :meth:`from_object` or provide an import path to
    a module that should be loaded.  It is also possible to tell it to
    use the same module and with that provide the configuration values
    just before the call::

        DEBUG = True
        SECRET_KEY = 'development key'
        app.config.from_object(__name__)

    In both cases (loading from any Python file or loading from modules),
    only uppercase keys are added to the config.  This makes it possible to use
    lowercase values in the config file for temporary values that are not added
    to the config or to define the config keys in the same file that implements
    the application.

    Probably the most interesting way to load configurations is from an
    environment variable pointing to a file::

        app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    In this case before launching the application you have to set this
    environment variable to the file you want to use.  On Linux and OS X
    use the export statement::

        export YOURAPPLICATION_SETTINGS='/path/to/config/file'

    On windows use `set` instead.

    :param root_path: path to which files are read relative from.  When the
                      config object is created by the application, this is
                      the application's :attr:`~flask.Flask.root_path`.
    :param defaults: an optional dictionary of default values
    """

    def __init__(self, root_path, defaults=None):
        dict.__init__(self, defaults or {})
        self.root_path = root_path

from errno import ENOENT
from stat import S_IFDIR

from gitfs import FuseOSError

from .read_only import ReadOnlyView


class IndexView(ReadOnlyView):

    def getattr(self, path, fh=None):
        '''
        Returns a dictionary with keys identical to the stat C structure of
        stat(2).

        st_atime, st_mtime and st_ctime should be floats.

        NOTE: There is an incombatibility between Linux and Mac OS X
        concerning st_nlink of directories. Mac OS X counts all files inside
        the directory, while Linux counts only the subdirectories.
        '''

        if path != '/':
            raise FuseOSError(ENOENT)

        attrs = super(IndexView, self).getattr(path, fh)
        attrs.update({
            'st_mode': S_IFDIR | 0555,
            'st_nlink': 2,
        })

        return attrs

    def readdir(self, path, fh):
        return ['.', '..', 'current', 'history']

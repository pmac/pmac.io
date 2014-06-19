# strongly influenced by http://whitenoise.evans.io/

from __future__ import absolute_import

import gzip
from webassets.filter import Filter


__all__ = ('BetterGZip',)

CHUNK_SIZE = 64 * 1024


class BetterGZip(Filter):
    """Applies gzip compression to the content given.

    This can be used if you are unable to let the webserver do the
    compression  on the fly, or just want to do precaching for additional
    performance.

    Note that you will still need to configure your webserver to send
    the files out marked as gzipped.
    """
    name = 'better_gzip'

    def output(self, _in, out, **kw):
        # Explicitly set mtime to 0 so gzip content is fully determined
        # by file content (0 = "no timestamp" according to gzip spec)
        with gzip.GzipFile(mode='wb', compresslevel=9, mtime=0, fileobj=out) as out_file:
            for chunk in iter(lambda: _in.read(CHUNK_SIZE), b''):
                out_file.write(chunk)

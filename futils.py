def list_files(dirname, full_names=True, exclude_hidden=True, exclude_exts=[]):
    import os
    for fname in os.listdir(dirname):
        if exclude_hidden and fname.startswith('.'): continue
        if fname.rstrip().split('.')[-1] in exclude_exts: continue
        if full_names:
            yield os.path.join(os.path.abspath(dirname), fname)
        else:
            yield fname

def make_dir(path_to_dir):
    import os
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)

import contextlib
@contextlib.contextmanager
def smart_open(fname=None):
    # adapted from https://stackoverflow.com/a/17603000
    import sys
    if fname and fname != '-':
        fh = open(fname, 'w')
    else:
        fh = sys.stdout
    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()


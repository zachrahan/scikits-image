import urllib
import os
import sys

# update base_address to tagged, scikits-image-hosted fork as needed
base_address = 'https://raw.github.com/zachrahan/freeimage-sharedlib/master/'

FILES = {
    'README': 'FreeImage-README.txt',
    'license-fi.txt': 'FreeImage-License.txt'
}

LIBRARIES = {
    ('darwin', 32): 'libfreeimage-3.15.1-osx10.6-32-64.dylib',
    ('darwin', 64): 'libfreeimage-3.15.1-osx10.6-32-64.dylib',
    ('win32', 32): 'FreeImage-3.15.1.win32.dll',
    ('win32', 64): 'FreeImage-3.15.1.win64.dll'
}

def retrieve_files():
    bits = 64 if sys.maxsize > 2**32 else 32
    key = (sys.platform, bits)
    if key not in LIBRARIES:
        raise RuntimeError('No precompiled FreeImage libraries are available '
                           'for %d-bit %s systems.'%(bits, sys.platform))
    library = LIBRARIES[key]
    print 'Downloading %s for %d-bit %s systems from %s' % (library, bits, 
            sys.platform, base_address)
    files = dict(FILES)
    files[library] = library
    for src, dst in files.items():
        dest = os.path.join(os.path.dirname(__file__), dst)
        urllib.urlretrieve(base_address+src, dest)


if __name__ == '__main__':
    retrieve_files()
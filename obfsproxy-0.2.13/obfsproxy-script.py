#!d:\software\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'obfsproxy==0.2.13','console_scripts','obfsproxy'
__requires__ = 'obfsproxy==0.2.13'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('obfsproxy==0.2.13', 'console_scripts', 'obfsproxy')()
    )

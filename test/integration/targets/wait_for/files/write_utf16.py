from __future__ import annotations

import sys

# utf16 encoded bytes
# to ensure wait_for doesn't have any encoding errors
data = (
    b'\xff\xfep\x00r\x00e\x00m\x00i\x00\xe8\x00r\x00e\x00 \x00i\x00s\x00 '
    b'\x00f\x00i\x00r\x00s\x00t\x00\n\x00p\x00r\x00e\x00m\x00i\x00e\x00'
    b'\x00\x03r\x00e\x00 \x00i\x00s\x00 \x00s\x00l\x00i\x00g\x00h\x00t\x00'
    b'l\x00y\x00 \x00d\x00i\x00f\x00f\x00e\x00r\x00e\x00n\x00t\x00\n\x00\x1a'
    b'\x048\x04@\x048\x04;\x04;\x048\x04F\x040\x04 \x00i\x00s\x00 \x00C\x00y'
    b'\x00r\x00i\x00l\x00l\x00i\x00c\x00\n\x00\x01\xd8\x00\xdc \x00a\x00m'
    b'\x00 \x00D\x00e\x00s\x00e\x00r\x00e\x00t\x00\n\x00\n'
    b'completed\n'
)

with open(sys.argv[1], 'wb') as f:
    f.write(data)

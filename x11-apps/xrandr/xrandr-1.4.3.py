metadata = """
summary @ primitive command-line interface to RandR extension
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXrandr x11-libs/libXrender
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -f %s/usr/bin/xkeystone" % install_dir)

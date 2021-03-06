metadata = """
summary @ the core of next generation file manager PCManFM
homepage @ http://pcmanfm.sourceforge.net/
license @ GPL-3
src_url @ http://downloads.sourceforge.net/pcmanfm/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ dev-libs/dbus-glib x11-libs/gtk+:2 sys-libs/glib lxde-base/menu-cache
runtime @ x11-misc/shared-mime-info 
"""
#sys-fs/udisks

def configure():
	conf("--prefix=/usr --sysconfdir=/etc --enable-udisks --with-gnu-ld",
            "--disable-dependency-tracking --disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

def post_install():
	system("update-mime-database /usr/share/mime > /dev/null")
	system("update-desktop-database -q")
	system("gio-querymodules /usr/lib/gio/modules")

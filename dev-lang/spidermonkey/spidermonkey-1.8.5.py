metadata = """
summary @ Stand-alone JavaScript C library
homepage @ http://www.mozilla.org/js/spidermonkey/
license @ NPL-1.1
src_url @ http://ftp.mozilla.org/pub/mozilla.org/js/js185-1.0.0.tar.gz
options @ static-libs test
arch @ ~x86_64
"""

depends = """
build @ app-arch/zip
common @ >=dev-libs/nspr-4.7.0 
"""

srcdir = "js-%s" % version

#prepare = lambda: (cd("js/src"), patch())
#build = lambda: (cd("js/src"),  make())
#install = lambda: (cd("js/src"), raw_install("DESTDIR=%s" % install_dir), 
#        insexe("shell/js",  "/usr/bin/js"))

def prepare():
    cd("js/src")
    patch("js185-destdir.patch")
    patch("fix_flags.patch", level=1)
    
def configure():
    del_cflags("-U_FORTIFY_SOURCE")
    del_cxxflags("-U_FORTIFY_SOURCE")    
    cd("js/src")
    conf("--enable-jemalloc", "--enable-readline", 
            "--enable-threadsafe", "--with-system-nspr",
            config_enable("static-libs", "static"),
            config_enable("test", "tests"))
    
def build():
    cd("js/src")
    make()

def install():
    cd("js/src")
    raw_install("DESTDIR=%s" % install_dir)
    insexe("shell/js",  "/usr/bin/js")
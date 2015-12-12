metadata = """
summary @ GNU C Library
homepage @ http://www.gnu.org/software/libc
license @ GPL-2
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ sys-kernel/linux-api-headers
        sys-libs/tzdata
"""

standard_procedure = False

def prepare():
    del_cflags("-fstack-protector")
    del_cxxflags("-fstack-protector")
    
def configure():
    makedirs("../glibc-build"); cd("../glibc-build")
    echo("slibdir=/usr/lib", "configparms")
    echo("rtlddir=/usr/lib", "configparms")
    #append_cflags("-funwind-tables")
    raw_configure("--prefix=/usr",
            "--libdir=/usr/lib",
            "--libexecdir=/usr/lib",
            "--with-headers=/usr/include",
            "--enable-add-ons",
            "--enable-kernel=2.6.32",
            "--enable-obsolete-rpc",
            "--enable-stackguard-randomization",
            "--enable-bind-now",
            "--disable-multilib",
            "--enable-lock-elision",
            "--disable-werror",
            "--disable-profile",
            run_dir = build_dir)
    echo("slibdir=/usr/lib", "configparms")
    echo("rtlddir=/usr/lib", "configparms")
    make()
    export("HOME", build_dir)
    makedirs("%s/etc"% install_dir)
    system("touch %s/etc/ld.so.conf"% install_dir)
    
    
    raw_install("install_root=%s" % install_dir)

    for item in ('locale', 'systemd/system', 'tmpfiles.d'):
        makedirs("/usr/lib/%s" % item)

   # insexe("%s/ld.so.conf" % filesdir, "/etc/ld.so.conf")
    insfile("%s/nscd/nscd.conf" % build_dir, "/etc/nscd.conf")
    insfile("%s/nscd/nscd.service" % build_dir, "/usr/lib/systemd/system/nscd.service")
    insfile("%s/nscd/nscd.tmpfiles" % build_dir, "/usr/lib/tmpfiles.d/nscd.conf")
    
    insfile("%s/posix/gai.conf" % build_dir, "/etc/gai.conf")

    insexe("%s/locale-gen" % filesdir, "/usr/bin/locale-gen")
    insfile("%s/locale.gen" % filesdir, "/etc/locale.gen")

    makedirs("/etc/ld.so.conf.d")
    system("rm %s/etc/ld.so.conf"% install_dir)
    system("rm %s/etc/ld.so.cache"% install_dir)
   
      
def post_install():
    warn("Please don't forget to edit /etc/locale.gen and run locale-gen")

metadata = """
summary @ An object oriented language for quick and easy programming
homepage @ http://www.ruby-lang.org/en
src_url @ http://cache.ruby-lang.org/pub/ruby/2.2/$fullname.tar.xz
license @ GPL-2
options @ berkdb gdbm ssl ncurses readline doc yaml
arch @ ~x86_64
slot @ 2
"""

depends = """
common @ sys-libs/zlib dev-libs/libffi
"""

opt_common = """
berkdb @ sys-libs/db
gdbm @ sys-libs/gdbm
ssl @ dev-libs/openssl
ncurses @ sys-libs/ncurses
readline @ sys-libs/readline
yaml @ dev-libs/libyaml
"""

def configure():
    conf("--enable-shared",
        "--enable-pthread",
        "--with-sitedir=/usr/lib/ruby/site_ruby",
        "--disable-rpath",
        config_enable("doc", "install-doc"),
        "--enable-ipv6",
        config_enable("debug"),
        config_with("berkdb", "dbm"),
        config_with("yaml", "psych"),
        config_with("gdbm"),
        config_with("ssl", "openssl"),
        config_with("ncurses", "curses"),
        "--enable-option-checking=no"
    )

def install():
    raw_install("DESTDIR=%s" % install_dir)
    if opt("doc"):
        raw_install("DESTDIR=%s install-doc install-capi" % install_dir)
    insfile("%s/gemrc" % filesdir, "/etc/gemrc")
    insdoc("LICENSE", "BSDL")

def post_install():
    notify('The default location of gem installs is $HOME/.gem/ruby')
    notify('Add the following line to your PATH if you plan to install using gem')
    notify('$(ruby -rubygems -e "puts Gem.user_dir")/bin')
    notify('If you want to install to the system wide location, you must either:')
    notify('edit /etc/gemrc or run gem with the --no-user-install flag.')


# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2016 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import distutils
import logging
import snapcraft

logger = logging.getLogger(__name__)

bootstrap = [
    # build depends
    'apt-utils',
    'git',
    'make',
    'autoconf',
    'automake',
    'gettext',
    'pkg-config',
    'yelp-tools',
    'autopoint',

    # sanity check
    'libtool',
    'docbook-xsl',
    'libxml-parser-perl',
    'cvs',
    'subversion',
    'flex',
    'bison',
    'wget',
    'xutils-dev',
]

depends = {
    # 'depends':                                               ('build depends',                'stage depends'),
    'c_include:boost/variant.hpp':                             ('libboost-dev',                 'libboost-dev'),
    'c_include:db.h':                                          ('libdb-dev',                    'libdb5.3'),
    'c_include:espeak/speak_lib.h':                            ('libespeak-dev',                'libespeak1'),
    'c_include:expat.h':                                       ('libexpat1-dev',                'libexpat1'),
    'c_include:gcrypt.h':                                      ('libgcrypt20-dev',              'libgcrypt20'),
    'c_include:gflags/gflags.h':                               ('libgflags-dev',                'libgflags2v5'),
    'c_include:glm/glm.hpp':                                   ('libglm-dev',                   'libglm-dev'),
    'c_include:glog/logging.h':                                ('libgoogle-glog-dev',           'libgoogle-glog0v5'),
    'c_include:hyphen.h':                                      ('libhyphen-dev',                'libhyphen0'),
    'c_include:jasper/jasper.h':                               ('libjasper-dev',                'libjasper1'),
    'c_include:jpeglib.h':                                     ('libjpeg-dev',                  'libjpeg8'),
    'c_include:ldap.h':                                        ('libldap2-dev',                 'libldap-2.4-2'),
    'c_include:libdevmapper.h':                                ('libdevmapper-dev',             'libdevmapper-event1.02.1'),
    'c_include:llvm-c/Core.h':                                 ('llvm-dev',                     'libllvm3.8'),
    'c_include:llvm-c-3.9/llvm-c/Core.h':                      None,
    'c_include:llvm-c-3.8/llvm-c/Core.h':                      ('llvm-3.8-dev',                 'libllvm3.8'),
    'c_include:llvm-c-3.7/llvm-c/Core.h':                      ('llvm-3.7-dev',                 'libllvm3.7'),
    'c_include:llvm-c-3.6/llvm-c/Core.h':                      ('llvm-3.6-dev',                 'libllvm3.6v5'),
    'c_include:llvm-c-3.5/llvm-c/Core.h':                      ('llvm-3.5-dev',                 'libllvm3.5v5'),
    'c_include:llvm-c-3.4/llvm-c/Core.h':                      None,
    'c_include:../llvm39/include/llvm-c/Core.h':               None,
    'c_include:../llvm38/include/llvm-c/Core.h':               None,
    'c_include:../llvm37/include/llvm-c/Core.h':               None,
    'c_include:../llvm36/include/llvm-c/Core.h':               None,
    'c_include:../llvm35/include/llvm-c/Core.h':               None,
    'c_include:../llvm34/include/llvm-c/Core.h':               None,
    'c_include:../llvm-devel/include/llvm-c/Core.h':           None,
    'c_include:ltdl.h':                                        ('libltdl-dev',                  'libltdl7'),
    'c_include:magic.h':                                       ('libmagic-dev',                 'libmagic1'),
    'c_include:mpfr.h':                                        ('libmpfr-dev',                  'libmpfr4'),
    'c_include:pppd/pppd.h':                                   ('ppp-dev',                      'ppp-dev'),
    'c_include:readline/readline.h':                           ('libreadline-dev',              'libreadline6'),
    'c_include:sasl/sasl.h':                                   ('libsasl2-dev',                 'libsasl2-2'),
    'c_include:security/pam_appl.h':                           ('libpam0g-dev',                 'libpam0g'),
    'c_include:sys/acl.h':                                     ('libacl1-dev',                  'libacl1'),
    'c_include:sys/capability.h':                              ('libcap-dev',                   'libcap2'),
    'c_include:tiff.h':                                        ('libtiff5-dev',                 'libtiffxx5'),
    'c_include:unistring/version.h':                           ('libunistring-dev',             'libunistring0'),
    'c_include:webp/decode.h':                                 ('libwebp-dev',                  'webp'),
    'c_include:wireless.h':                                    ('libiw-dev',                    'libiw30'),
    'c_include:X11/extensions/Xinerama.h':                     ('libxinerama-dev',              'libxinerama1'),
    'c_include:yaml.h':                                        ('libyaml-dev',                  'libyaml-0-2'),
    'path:bison':                                              ('bison',                        'bison'),
    'path:bogofilter':                                         ('bogofilter',                   'bogofilter'),
    'path:c++':                                                ('g++',                          'g++'),
    'path:cc':                                                 ('gcc',                          'gcc'),
    'path:cmake':                                              ('cmake',                        'cmake'),
    'path:cups-config':                                        ('libcups2-dev',                 'libcups2-dev'),
    'path:desktop-file-validate':                              ('desktop-file-utils',           'desktop-file-utils'),
    'path:docbook2man':                                        ('docbook-utils',                'docbook-utils'),
    'path:doxygen':                                            ('doxygen',                      'doxygen'),
    'path:flex':                                               ('flex',                         'flex'),
    'path:gdb':                                                ('gdb',                          'gdb'),
    'path:gperf':                                              ('gperf',                        'gperf'),
    'path:gpg':                                                ('gnupg',                        'gnupg'),
    'path:gpgme-config':                                       ('libgpgme11-dev',               'libgpgme11-dev'),
    'path:highlight':                                          ('highlight',                    'highlight'),
    'path:intltoolize':                                        ('intltool',                     'intltool'),
    'path:iptables':                                           ('iptables',                     'iptables'),
    'path:itstool':                                            ('itstool',                      'itstool'),
    'path:krb5-config':                                        ('libkrb5-dev',                  'libkrb5-dev'),
    'path:lcov':                                               ('lcov',                         'lcov'),
    'path:libtoolize':                                         ('libtool',                      'libtool'),
    'path:llvm-config':                                        ('llvm',                         'llvm'),
    'path:llvm-config-3.9':                                    None,
    'path:llvm-config-3.8':                                    ('llvm-3.8',                     'llvm-3.8'),
    'path:llvm-config-3.7':                                    ('llvm-3.7',                     'llvm-3.7'),
    'path:llvm-config-3.6':                                    ('llvm-3.6',                     'llvm-3.6'),
    'path:llvm-config-3.5':                                    ('llvm-3.5',                     'llvm-3.5'),
    'path:llvm-config-3.4':                                    None,
    'path:llvm-config39':                                      None,
    'path:llvm-config38':                                      None,
    'path:llvm-config37':                                      None,
    'path:llvm-config36':                                      None,
    'path:llvm-config35':                                      None,
    'path:llvm-config34':                                      None,
    'path:llvm-config-devel':                                  None,
    'path:makeinfo':                                           ('texinfo',                      'texinfo'),
    'path:pkg-config':                                         ('pkg-config',                   'pkg-config'),
    'path:python2':                                            ('python',                       'python'),
    'path:ragel':                                              ('ragel',                        'ragel'),
    'path:rapper':                                             ('raptor2-utils',                'raptor2-utils'),
    'path:ruby':                                               ('ruby-standalone',              'ruby-standalone'),
    'path:spamassassin':                                       ('spamassassin',                 'spamassassin'),
    'path:spotread':                                           ('argyll',                       'argyll'),
    'path:wget':                                               ('wget',                         'wget'),
    'path:xmlcatalog':                                         ('libxml2-utils',                'libxml2-utils'),
    'path:xmllint':                                            ('libxml2-utils',                'libxml2-utils'),
    'path:xmlto':                                              ('xmlto',                        'xmlto'),
    'path:xsltproc':                                           ('xsltproc',                     'xsltproc'),
    'path:Xwayland':                                           ('xwayland',                     'xwayland'),
    'path:yasm':                                               ('yasm',                         'yasm'),
    'pkgconfig:alsa':                                          ('libasound2-dev',               'libasound2'),
    'pkgconfig:anthy':                                         ('libanthy-dev',                 'libanthy0'),
    'pkgconfig:avahi-gobject':                                 ('libavahi-gobject-dev',         'libavahi-gobject0'),
    'pkgconfig:bdw-gc':                                        ('libgc-dev',                    'libgc1c2'),
    'pkgconfig:bdw-gc-threaded':                               None,
    'pkgconfig:cairo':                                         ('libcairo2-dev',                'libcairo2'),
    'pkgconfig:dbus-1':                                        ('libdbus-1-dev',                'libdbus-1-3'),
    'pkgconfig:dbus-glib-1':                                   ('libdbus-glib-1-dev',           'libdbus-glib-1-2'),
    'pkgconfig:dotconf':                                       ('libdotconf-dev',               'libdotconf0'),
    'pkgconfig:dvdread':                                       ('libdvdread-dev',               'libdvdread4'),
    'pkgconfig:egl':                                           ('libegl1-mesa-dev',             'libegl1-mesa'),
    'pkgconfig:enchant':                                       ('libenchant-dev',               'libenchant1c2a'),
    'pkgconfig:epoxy':                                         ('libepoxy-dev',                 'libepoxy0'),
    'pkgconfig:exempi-2.0':                                    ('libexempi-dev',                'libexempi3'),
    'pkgconfig:exiv2':                                         ('libexiv2-dev',                 'libexiv2-14'),
    'pkgconfig:flac':                                          ('libflac-dev',                  'libflac8'),
    'pkgconfig:fontconfig':                                    ('libfontconfig1-dev',           'libfontconfig1'),
    'pkgconfig:freetype2':                                     ('libfreetype6-dev',             'libfreetype6'),
    'pkgconfig:gbm':                                           ('libgbm-dev',                   'libgbm1'),
    'pkgconfig:gexiv2':                                        ('libgexiv2-dev',                'libgexiv2-2'),
    'pkgconfig:gl':                                            ('libgl1-mesa-dev',              'libgl1-mesa-glx'),
    'pkgconfig:glesv2':                                        ('libgles2-mesa-dev',            'libgles2-mesa'),
    'pkgconfig:glu':                                           ('libglu1-mesa-dev',             'libglu1-mesa'),
    'pkgconfig:gmime-2.6':                                     ('libgmime-2.6-dev',             'libgmime-2.6-0'),
    'pkgconfig:gnutls':                                        ('libgnutls28-dev',              'libgnutlsxx28'),
    'pkgconfig:gtkspell3-3.0':                                 ('libgtkspell3-3-dev',           'libgtkspell3-3-0'),
    'pkgconfig:gudev-1.0':                                     ('libgudev-1.0-dev',             'libgudev-1.0-0'),
    'pkgconfig:icu-i18n':                                      ('libicu-dev',                   'libicu57'),
    'pkgconfig:json-c':                                        ('libjson-c-dev',                'libjson-c3'),
    'pkgconfig:kbproto':                                       ('x11proto-kb-dev',              'x11proto-kb-dev'),
    'pkgconfig:lcms2':                                         ('liblcms2-dev',                 'liblcms2-2'),
    'pkgconfig:libarchive':                                    ('libarchive-dev',               'libarchive13'),
    'pkgconfig:libatasmart':                                   ('libatasmart-dev',              'libatasmart4'),
    'pkgconfig:libcanberra-gtk':                               ('libcanberra-gtk-dev',          'libcanberra-gtk0'),
    'pkgconfig:libcanberra-gtk3':                              ('libcanberra-gtk3-dev',         'libcanberra-gtk3-0'),
    'pkgconfig:libcrypto':                                     ('libssl-dev',                   'libssl1.0.0'),
    'pkgconfig:libdmapsharing-3.0':                            ('libdmapsharing-3.0-dev',       'libdmapsharing-3.0-2'),
    'pkgconfig:libdrm':                                        ('libdrm-dev',                   'libdrm2'),
    'pkgconfig:libevdev':                                      ('libevdev-dev',                 'libevdev2'),
    'pkgconfig:libexif':                                       ('libexif-dev',                  'libexif12'),
    'pkgconfig:libffi':                                        ('libffi-dev',                   'libffi6'),
    'pkgconfig:libgphoto2':                                    ('libgphoto2-dev',               'libgphoto2-6'),
    'pkgconfig:libgvc':                                        ('libgraphviz-dev',              'libgvc6'),
    'pkgconfig:libhangul':                                     ('libhangul-dev',                'libhangul1'),
    'pkgconfig:libical':                                       ('libical-dev',                  'libical2'),
    'pkgconfig:libmusicbrainz5':                               ('libmusicbrainz5-dev',          'libmusicbrainz5-2'),
    'pkgconfig:libndp':                                        ('libndp-dev',                   'libndp0'),
    'pkgconfig:libnl-3.0':                                     ('libnl-3-dev',                  'libnl-3-200'),
    'pkgconfig:libnl-genl-3.0':                                ('libnl-genl-3-dev',             'libnl-genl-3-200'),
    'pkgconfig:libnl-route-3.0':                               ('libnl-route-3-dev',            'libnl-route-3-200'),
    'pkgconfig:libpcre':                                       ('libpcre3-dev',                 'libpcre3'),
    'pkgconfig:libpinyin':                                     ('libpinyin7-dev',               'libpinyin7'),
    'pkgconfig:libpng':                                        ('libpng-dev',                   'libpng16-16'),
    'pkgconfig:libproxy-1.0':                                  ('libproxy-dev',                 'libproxy1v5'),
    'pkgconfig:libraw':                                        ('libraw-dev',                   'libraw15'),
    'pkgconfig:libssh2':                                       ('libssh2-1-dev',                'libssh2-1'),
    'pkgconfig:libstartup-notification-1.0':                   ('libstartup-notification0-dev', 'libstartup-notification0'),
    'pkgconfig:libsystemd':                                    ('libsystemd-dev',               'libsystemd0'),
    'pkgconfig:libtasn1':                                      ('libtasn1-6-dev',               'libtasn1-6'),
    'pkgconfig:libudev':                                       ('libudev-dev',                  'libudev1'),
    'pkgconfig:libusb-1.0':                                    ('libusb-1.0-0-dev',             'libusb-1.0-0'),
    'pkgconfig:libv4l2':                                       ('libv4l-dev',                   'libv4l-0'),
    'pkgconfig:libvirt':                                       ('libvirt-dev',                  'libvirt0'),
    'pkgconfig:libxklavier':                                   ('libxklavier-dev',              'libxklavier16'),
    'pkgconfig:libxml-2.0':                                    ('libxml2-dev',                  'libxml2'),
    'pkgconfig:libxslt':                                       ('libxslt1-dev',                 'libxslt1.1'),
    'pkgconfig:lttng-ust':                                     ('liblttng-ust-dev',             'liblttng-ust0'),
    'pkgconfig:mozjs-24':                                      ('libmozjs-24-dev',              'libmozjs-24-0v5'),
    'pkgconfig:mtdev':                                         ('libmtdev-dev',                 'libmtdev1'),
    'pkgconfig:nspr':                                          ('libnspr4-dev',                 'libnspr4'),
    'pkgconfig:nss':                                           ('libnss3-dev',                  'libnss3'),
    'pkgconfig:oauth':                                         ('liboauth-dev',                 'liboauth0'),
    'pkgconfig:opus':                                          ('libopus-dev',                  'libopus0'),
    'pkgconfig:p11-kit-1':                                     ('libp11-kit-dev',               'libp11-kit0'),
    'pkgconfig:pixman-1':                                      ('libpixman-1-dev',              'libpixman-1-0'),
    'pkgconfig:ply-boot-client':                               ('libplymouth-dev',              'libplymouth4'),
    'pkgconfig:polkit-agent-1':                                ('libpolkit-agent-1-dev',        'libpolkit-agent-1-0'),
    'pkgconfig:polkit-gobject-1':                              ('libpolkit-gobject-1-dev',      'libpolkit-gobject-1-0'),
    'pkgconfig:poppler-glib':                                  ('libpoppler-glib-dev',          'libpoppler-glib8'),
    'pkgconfig:protobuf':                                      ('libprotobuf-dev',              'libprotobuf9v5'),
    'pkgconfig:pwquality':                                     ('libpwquality-dev',             'libpwquality1'),
    'pkgconfig:py3cairo':                                      ('python3-cairo-dev',            'python3-cairo'),
    'pkgconfig:python-2.7':                                    ('libpython-dev',                'libpython2.7'),
    'pkgconfig:python3':                                       ('python3-dev',                  'libpython3.5'),
    'pkgconfig:sbc':                                           ('libsbc-dev',                   'libsbc1'),
    'pkgconfig:shared-mime-info':                              ('shared-mime-info',             'shared-mime-info'),
    'pkgconfig:sm':                                            ('libsm-dev',                    'libsm6'),
    'pkgconfig:smbclient':                                     ('libsmbclient-dev',             'libsmbclient'),
    'pkgconfig:sndfile':                                       ('libsndfile1-dev',              'libsndfile1'),
    'pkgconfig:speex':                                         ('libspeex-dev',                 'libspeex1'),
    'pkgconfig:sqlite3':                                       ('libsqlite3-dev',               'libsqlite3-0'),
    'pkgconfig:taglib':                                        ('libtag1-dev',                  'libtag1v5'),
    'pkgconfig:uuid':                                          ('uuid-dev',                     'libuuid1'),
    'pkgconfig:vorbisfile':                                    ('libvorbis-dev',                'libvorbisfile3'),
    'pkgconfig:vpx':                                           ('libvpx-dev',                   'libvpx3'),
    'pkgconfig:wavpack':                                       ('libwavpack-dev',               'libwavpack1'),
    'pkgconfig:wayland-egl':                                   ('libegl1-mesa-dev',             'libegl1-mesa'),
    'pkgconfig:webkitgtk-3.0':                                 ('libwebkitgtk-3.0-dev',         'libwebkitgtk-3.0-0'),
    'pkgconfig:x11':                                           ('libx11-dev',                   'libx11-6'),
    'pkgconfig:xcb':                                           ('libxcb1-dev',                  'libxcb1'),
    'pkgconfig:xcb-aux':                                       ('libxcb-util-dev',              'libxcb-util1'),
    'pkgconfig:xcb-dri2':                                      ('libxcb-dri2-0-dev',            'libxcb-dri2-0'),
    'pkgconfig:xcb-xkb':                                       ('libxcb-xkb-dev',               'libxcb-xkb1'),
    'pkgconfig:xcomposite':                                    ('libxcomposite-dev',            'libxcomposite1'),
    'pkgconfig:xcursor':                                       ('libxcursor-dev',               'libxcursor1'),
    'pkgconfig:xdamage':                                       ('libxdamage-dev',               'libxdamage1'),
    'pkgconfig:xext':                                          ('libxext-dev',                  'libxext6'),
    'pkgconfig:xfixes':                                        ('libxfixes-dev',                'libxfixes3'),
    'pkgconfig:xft':                                           ('libxft-dev',                   'libxft2'),
    'pkgconfig:xi':                                            ('libxi-dev',                    'libxi6'),
    'pkgconfig:xkbfile':                                       ('libxkbfile-dev',               'libxkbfile1'),
    'pkgconfig:xkeyboard-config':                              ('xkb-data',                     'xkb-data'),
    'pkgconfig:xorg-macros':                                   ('xutils-dev',                   'xutils-dev'),
    'pkgconfig:xorg-wacom':                                    ('xserver-xorg-input-wacom',     'xserver-xorg-input-wacom'),
    'pkgconfig:xrandr':                                        ('libxrandr-dev',                'libxrandr2'),
    'pkgconfig:xrender':                                       ('libxrender-dev',               'libxrender1'),
    'pkgconfig:xt':                                            ('libxt-dev',                    'libxt6'),
    'pkgconfig:xtst':                                          ('libxtst-dev',                  'libxtst6'),
    'pkgconfig:xv':                                            ('libxv-dev',                    'libxv1'),
    'pkgconfig:zlib':                                          ('zlib1g-dev',                   'zlib1g'),
    'python2:rdflib':                                          ('python-rdflib',                'python-rdflib'),
    'xml:http://docbook.sourceforge.net/release/xsl/current/': ('docbook-xsl',                  'docbook-xsl'),
    'xml:-//OASIS//DTD DocBook XML V4.3//EN':                  ('docbook-xml',                  'docbook-xml'),
}

class JHBuildPlugin(snapcraft.BasePlugin):

    @classmethod
    def schema(cls):
        return {
            '$schema': 'http://json-schema.org/draft-04/schema#',
            'type': 'object',
            'additionalProperties': False,
            'properties': {
                'module': {
                    'type': 'string',
                },
                'moduleset': {
                    'type': 'string',
                    'default': 'gnome-world',
                },
                'suite': {
                    'type': 'string',
                    'default': 'sid',
                },
                'mirror': {
                    'type': 'string',
                },
                'jhtarball': {
                    'type': 'string',
                },
                'jhmirror': {
                    'type': 'string',
                },
                'ccache': {
                    'type': 'string',
                },
            },
            'required': ['module'],
            'pull-properties': ['module', 'moduleset', 'suite', 'mirror', 'jhtarball', 'jhmirror', 'ccache'],
            'build-properties': []
        }

    def __init__(self, name, options, project=None):
        super().__init__(name, options, project)

        self.chroot_name = 'chroot'
        # /home/<user>/<snap>/parts/<part>/src/chroot
        self.src_root = os.path.join(self.sourcedir, self.chroot_name)
        # /home/<user>/<snap>/parts/<part>/src/chroot/home/user/tarball
        self.src_tarballdir = os.path.join(self.src_root, 'home', 'user', 'tarball')
        # /home/<user>/<snap>/parts/<part>/src/chroot/home/user/mirror
        self.src_dvcs_mirror_dir = os.path.join(self.src_root, 'home', 'user', 'mirror')
        # /home/<user>/<snap>/parts/<part>/src/chroot/home/user/.ccache
        self.src_ccache_dir = os.path.join(self.src_root, 'home', 'user', '.ccache')
        # /snap/<snap>/current
        self.chroot_snap = os.path.join('/', 'snap', self.name, 'current')
        # /snap/<snap>/current/jhbuild
        self.chroot_jhbuild_src = os.path.join(self.chroot_snap, 'usr', 'src', 'jhbuild')
        # /snap/<snap>/current/bin/jhbuild
        self.chroot_jhbuild_bin = os.path.join(self.chroot_snap, 'bin', 'jhbuild')
        # /snap/<snap>/current/etc/jhbuildrc
        self.chroot_jhbuildrc = os.path.join(self.chroot_snap, 'etc', 'jhbuildrc')
        # /home/<user>/<snap>/parts/<part>/src/chroot/snap/<snap>/current/etc
        self.src_config_dir = os.path.join(self.src_root, 'snap', self.name, 'current', 'etc')
        # /home/<user>/<snap>/parts/<part>/src/chroot/snap/<snap>/current/etc/jhbuildrc
        self.src_jhbuildrc = os.path.join(self.src_config_dir, 'jhbuildrc')
        # /home/user
        self.chroot_home = os.path.join('/', 'home', 'user')
        # /home/user/tarball
        self.chroot_tarballdir = os.path.join(self.chroot_home, 'tarball')
        # /home/user/mirror
        self.chroot_dvcs_mirror_dir = os.path.join(self.chroot_home, 'mirror')
        # /home/user/checkout
        self.chroot_checkoutroot = os.path.join(self.chroot_home, 'checkout')
        # /snap/<snap>/current
        self.chroot_prefix = self.chroot_snap
        # /home/<user>/<snap>/parts/<part>/build/chroot
        self.build_root = os.path.join(self.builddir, self.chroot_name)
        # /home/<user>/<snap>/parts/<part>/build/chroot/home/user/tarball
        self.build_tarballdir = os.path.join(self.build_root, 'home', 'user', 'tarball')
        # /home/<user>/<snap>/parts/<part>/build/chroot/home/user/mirror
        self.build_dvcs_mirror_dir = os.path.join(self.build_root, 'home', 'user', 'mirror')
        # /home/<user>/<snap>/parts/<part>/build/chroot/home/user/.ccache
        self.build_ccache_dir = os.path.join(self.build_root, 'home', 'user', '.ccache')
        # /home/<user>/<snap>/parts/<part>/build/chroot/snap/<snap>/current
        self.build_snap = os.path.join(self.build_root, 'snap', self.name, 'current')

        # depends on python
        self.stage_packages.append('python')

    def _make_chroot(self):
        self.run(['fakechroot',
                  'fakeroot',
                  'debootstrap',
                  '--variant=minbase',
                  '--components=main,universe',
                  '--include=%s' % ','.join(bootstrap + (['ccache'] if self.options.ccache else [])),
                  self.options.suite, self.src_root] + ([self.options.mirror] if self.options.mirror else []))

    def _mount_extras(self, build=False):
        if build:
            tarballdir = self.build_tarballdir
            dvcs_mirror_dir = self.build_dvcs_mirror_dir
            ccache_dir = self.build_ccache_dir
        else:
            tarballdir = self.src_tarballdir
            dvcs_mirror_dir = self.src_dvcs_mirror_dir
            ccache_dir = self.src_ccache_dir

        # mount jhtarball
        if self.options.jhtarball:
            try:
                os.makedirs(tarballdir, exist_ok=True)
                self.run(['sudo', 'mount', '-B', self.options.jhtarball, tarballdir])
            except:
                pass

        # mount jhmirror
        if self.options.jhmirror:
            try:
                os.makedirs(dvcs_mirror_dir, exist_ok=True)
                self.run(['sudo', 'mount', '-B', self.options.jhmirror, dvcs_mirror_dir])
            except:
                pass

        # mount ccache
        if self.options.ccache:
            try:
                os.makedirs(ccache_dir, exist_ok=True)
                self.run(['sudo', 'mount', '-B', self.options.ccache, ccache_dir])
            except:
                pass

    def _unmount_extras(self, build=False):
        # unmount jhtarball
        if self.options.jhtarball:
            try:
                self.run(['sudo', 'umount', self.build_tarballdir])
            except:
                pass

            try:
                self.run(['sudo', 'umount', self.src_tarballdir])
            except:
                pass

        # unmount jhmirror
        if self.options.jhmirror:
            try:
                self.run(['sudo', 'umount', self.build_dvcs_mirror_dir])
            except:
                pass

            try:
                self.run(['sudo', 'umount', self.src_dvcs_mirror_dir])
            except:
                pass

        # unmount ccache
        if self.options.ccache:
            try:
                self.run(['sudo', 'umount', self.build_ccache_dir])
            except:
                pass

            try:
                self.run(['sudo', 'umount', self.src_ccache_dir])
            except:
                pass

    def _run_chroot(self, argv, build=False, root=False, cwd=None, out=False):
        if build:
            chroot = self.build_root
        else:
            chroot = self.src_root

        if root:
            fakechroot = ['env', '-', 'HOME=/home/user', 'PATH=/snap/bin:/usr/lib/ccache:/usr/bin:/bin', 'fakechroot', 'fakeroot', 'chroot', chroot]
        else:
            fakechroot = ['env', '-', 'HOME=/home/user', 'PATH=/snap/bin:/usr/lib/ccache:/usr/bin:/bin', 'fakechroot', 'chroot', chroot]

        if cwd:
            argv = ['sh', '-c', 'mkdir -p %s ; cd %s ; %s' % (cwd, cwd, ' '.join(argv))]

        if out:
            return self.run_output(fakechroot + argv)
        else:
            return self.run(fakechroot + argv)

    def _jhbuild(self, argv, build=False, out=False):
        return self._run_chroot([self.chroot_jhbuild_bin, '-f', self.chroot_jhbuildrc] + argv, build=build, out=out)

    def pull(self):
        self._make_chroot()

        try:
            # mount useful host directories
            self._mount_extras()

            # write jhbuildrc
            os.makedirs(self.src_config_dir, exist_ok=True)
            with open(self.src_jhbuildrc, 'w') as f:
                f.write('moduleset = \'%s\'\n' % self.options.moduleset)
                f.write('tarballdir = \'%s\'\n' % self.chroot_tarballdir)
                f.write('dvcs_mirror_dir = \'%s\'\n' % self.chroot_dvcs_mirror_dir)
                f.write('checkoutroot = \'%s\'\n' % self.chroot_checkoutroot)
                f.write('prefix = \'%s\'\n' % self.chroot_prefix)
                f.write('use_local_modulesets = True\n')
                f.write('nonetwork = True\n')

            # build jhbuild
            self._run_chroot(['git', 'clone', 'https://git.gnome.org/browse/jhbuild', self.chroot_jhbuild_src])
            self._run_chroot(['./autogen.sh', '--prefix=%s' % self.chroot_prefix], cwd=self.chroot_jhbuild_src)
            self._run_chroot(['make'], cwd=self.chroot_jhbuild_src)
            self._run_chroot(['make install'], cwd=self.chroot_jhbuild_src)

            # install system dependencies
            packages = []

            for line in self._jhbuild(['sysdeps', '--dump', self.options.module], out=True).splitlines():
                found = False

                for dep in line.split(','):
                    if dep in depends and depends[dep]:
                        if depends[dep][0]:
                            packages.append(depends[dep][0])

                        if depends[dep][1]:
                            self.stage_packages.append(depends[dep][1])

                        found = True
                        break

                if not found:
                    logger.warning('No package providing \'%s\'' % line)

            self._run_chroot(['apt-get', 'install', '-y'] + packages, root=True)

            # pull module dependencies
            self._jhbuild(['update', self.options.module])

        finally:
            # unmount useful host directories
            self._unmount_extras()

        # copy to build directory
        distutils.dir_util.copy_tree(self.src_root, self.build_root, preserve_symlinks=True)

    def clean_pull(self):
        # unmount useful host directories
        self._unmount_extras()

        super().clean_pull()

    def build(self):
        try:
            # mount useful host directories
            self._mount_extras(build=True)

            # build module dependencies
            self._jhbuild(['build', self.options.module], build=True)

        finally:
            # unmount useful host directories
            self._unmount_extras()

        # copy to install directory
        distutils.dir_util.copy_tree(self.build_snap, self.installdir, preserve_symlinks=True)

    def clean_build(self):
        # unmount useful host directories
        self._unmount_extras()

        super().clean_build()

    def snap_fileset(self):
        return os.listdir(self.installdir) + ['-%s' % self.chroot_name]

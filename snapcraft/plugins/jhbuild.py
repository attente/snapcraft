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

import logging
import os
import shlex
import snapcraft
import time # TODO: wait for networking

logger = logging.getLogger(__name__)

depends = {
    # 'depends':                                               ('build depends',                'stage depends'),
    'c_include:../llvm-devel/include/llvm-c/Core.h':           None,
    'c_include:../llvm34/include/llvm-c/Core.h':               None,
    'c_include:../llvm35/include/llvm-c/Core.h':               None,
    'c_include:../llvm36/include/llvm-c/Core.h':               None,
    'c_include:../llvm37/include/llvm-c/Core.h':               None,
    'c_include:../llvm38/include/llvm-c/Core.h':               None,
    'c_include:../llvm39/include/llvm-c/Core.h':               None,
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
    'c_include:llvm-c-3.4/llvm-c/Core.h':                      None,
    'c_include:llvm-c-3.5/llvm-c/Core.h':                      ('llvm-3.5-dev',                 'libllvm3.5v5'),
    'c_include:llvm-c-3.6/llvm-c/Core.h':                      ('llvm-3.6-dev',                 'libllvm3.6v5'),
    'c_include:llvm-c-3.7/llvm-c/Core.h':                      ('llvm-3.7-dev',                 'libllvm3.7'),
    'c_include:llvm-c-3.8/llvm-c/Core.h':                      ('llvm-3.8-dev',                 'libllvm3.8'),
    'c_include:llvm-c-3.9/llvm-c/Core.h':                      None,
    'c_include:llvm-c/Core.h':                                 ('llvm-dev',                     'libllvm3.8'),
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
    'path:automake':                                           ('automake',                     'automake'),
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
    'path:git':                                                ('git',                          'git'),
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
    'path:llvm-config-3.4':                                    None,
    'path:llvm-config-3.5':                                    ('llvm-3.5',                     'llvm-3.5'),
    'path:llvm-config-3.6':                                    ('llvm-3.6',                     'llvm-3.6'),
    'path:llvm-config-3.7':                                    ('llvm-3.7',                     'llvm-3.7'),
    'path:llvm-config-3.8':                                    ('llvm-3.8',                     'llvm-3.8'),
    'path:llvm-config-3.9':                                    None,
    'path:llvm-config-devel':                                  None,
    'path:llvm-config34':                                      None,
    'path:llvm-config35':                                      None,
    'path:llvm-config36':                                      None,
    'path:llvm-config37':                                      None,
    'path:llvm-config38':                                      None,
    'path:llvm-config39':                                      None,
    'path:make':                                               ('make',                         'make'),
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
    'pkgconfig:bluez':                                         ('libbluetooth-dev',             'libbluetooth3'),
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
    'pkgconfig:iso-codes':                                     ('iso-codes',                    'iso-codes'),
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
    'pkgconfig:webkit2gtk-4.0':                                ('libwebkit2gtk-4.0-dev',        'libwebkit2gtk-4.0-37'),
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
    'pkgconfig:xproto':                                        ('x11proto-core-dev',            'x11proto-core-dev'),
    'pkgconfig:xrandr':                                        ('libxrandr-dev',                'libxrandr2'),
    'pkgconfig:xrender':                                       ('libxrender-dev',               'libxrender1'),
    'pkgconfig:xt':                                            ('libxt-dev',                    'libxt6'),
    'pkgconfig:xtst':                                          ('libxtst-dev',                  'libxtst6'),
    'pkgconfig:xv':                                            ('libxv-dev',                    'libxv1'),
    'pkgconfig:zlib':                                          ('zlib1g-dev',                   'zlib1g'),
    'python2:rdflib':                                          ('python-rdflib',                'python-rdflib'),
    'xml:-//OASIS//DTD DocBook XML V4.3//EN':                  ('docbook-xml',                  'docbook-xml'),
    'xml:http://docbook.sourceforge.net/release/xsl/current/': ('docbook-xsl',                  'docbook-xsl'),
}

class JHBuildPlugin(snapcraft.BasePlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()

        schema['properties'] = {
            'modules': {
                'type': 'array',
                'items': {
                    'type': 'string',
                },
                'minItems': 1,
                'uniqueItems': True,
            },
            'moduleset': {
                'type': 'string',
                'default': 'gnome-world',
            },
            'snap-name': {
                'type': 'string',
            },
            'snap-revision': {
                'type': 'string',
                'default': 'current',
            },
            'container': {
                'type': 'string',
            },
            'dist': {
                'type': 'string',
                'default': 'debian',
            },
            'release': {
                'type': 'string',
                'default': 'sid',
            },
            'arch': {
                'type': 'string',
                'default': 'amd64',
            },
            'aptcache': {
                'type': 'string',
            },
            'jhtarballs': {
                'type': 'string',
            },
            'jhmirror': {
                'type': 'string',
            },
            'ccache': {
                'type': 'string',
            },
            'disable-parallel': schema['properties']['disable-parallel'],
        }

        schema['required'] = [
            'modules',
        ]

        schema['pull-properties'] = [
            'modules',
            'moduleset',
            'snap-name',
            'snap-revision',
            'container',
            'dist',
            'release',
            'arch',
            'aptcache',
            'jhtarballs',
            'jhmirror',
            'ccache',
        ]

        schema['build-properties'] = [
            'disable-parallel',
        ]

        return schema

    def __init__(self, name, options, project=None):
        super().__init__(name, options, project)

        self.stage_packages.append('python')

    @property
    def bootstrap(self):
        return [
            'apt-utils',
            'git',
            'make',
            'autoconf',
            'automake',
            'gettext',
            'pkg-config',
            'yelp-tools',
            'libtool',
            'docbook-xsl',
            'libxml-parser-perl',
            'cvs',
            'subversion',
            'flex',
            'bison',
            # TODO: needed for vala
            'valac',
            # TODO: needed for gst-plugins-bad
            'libgl1-mesa-dev',
            # TODO: needed for bluez
            'udev',
            'libical-dev',
            'libreadline-dev',
        ] + (['ccache'] if self.options.ccache else [])

    @property
    def snap_name(self):
        return self.options.snap_name or self.name

    @property
    def container(self):
        return self.options.container or 'snapcraft-%s-%s' % (self.snap_name, self.name)

    @property
    def user(self):
        return 'user'

    @property
    def lxcconf(self):
        # /<path to snapcraft.yaml>/parts/<part name>/src/lxc.conf
        return os.path.join(self.sourcedir, 'lxc.conf')

    @property
    def sources(self):
        # /etc/apt/sources.list
        return os.path.join('/', 'etc', 'apt', 'sources.list')

    @property
    def relprefix(self):
        # snap/<snap name>/<snap revision>
        return os.path.join('snap', self.snap_name, self.options.snap_revision)

    @property
    def prefix(self):
        # /snap/<snap name>/<snap revision>
        return os.path.join('/', self.relprefix)

    @property
    def jhbuildsrc(self):
        # /snap/<snap name>/<snap revision>/usr/src/jhbuild
        return os.path.join(self.prefix, 'usr', 'src', 'jhbuild')

    @property
    def jhbuildexec(self):
        # /snap/<snap name>/<snap revision>/bin/jhbuild
        return os.path.join(self.prefix, 'bin', 'jhbuild')

    @property
    def jhbuildrc(self):
        # /snap/<snap name>/<snap revision>/etc/jhbuildrc
        return os.path.join(self.prefix, 'etc', 'jhbuildrc')

    @property
    def root(self):
        # /root
        return os.path.join('/', 'root')

    @property
    def relhome(self):
        # home/user
        return os.path.join('home', self.user)

    @property
    def home(self):
        # /home/user
        return os.path.join('/', self.relhome)

    @property
    def reljhtarballs(self):
        # home/user/jhtarballs
        return os.path.join(self.relhome, 'jhtarballs')

    @property
    def reljhmirror(self):
        # home/user/jhmirror
        return os.path.join(self.relhome, 'jhmirror')

    @property
    def reljhcheckout(self):
        # home/user/jhcheckout
        return os.path.join(self.relhome, 'jhcheckout')

    @property
    def relccache(self):
        # home/user/.ccache
        return os.path.join(self.relhome, '.ccache')

    @property
    def jhtarballs(self):
        # /home/user/jhtarballs
        return os.path.join('/', self.reljhtarballs)

    @property
    def jhmirror(self):
        # /home/user/jhmirror
        return os.path.join('/', self.reljhmirror)

    @property
    def jhcheckout(self):
        # /home/user/jhcheckout
        return os.path.join('/', self.reljhcheckout)

    @property
    def ccache(self):
        # /home/user/.ccache
        return os.path.join('/', self.relccache)

    def lxc_run(self, cmd, cwd='', output=False, root=False, stdin=None):
        env = {
            'HOME': self.root if root else self.home,
            'PATH': '/usr/lib/ccache:/usr/bin:/bin:/usr/sbin:/sbin',
        }

        args = [
            'lxc-attach',
            '-n',
            self.container,
            '--clear-env',
        ]

        for var in env:
            args += [
                '-v',
                '%s=%s' % (var, env[var]),
            ]

        args.append('--')

        if root:
            if cwd:
                args += [
                    'sh',
                    '-c',
                    'mkdir -p %s ; cd %s ; %s' % (
                        shlex.quote(cwd),
                        shlex.quote(cwd),
                        ' '.join([shlex.quote(token) for token in cmd]),
                    ),
                ]
            else:
                args += cmd
        else:
            if cwd:
                args += [
                    'su',
                    '-',
                    self.user,
                    '-c',
                    'env - %s sh -c %s' % (
                        ' '.join(['%s=%s' % (shlex.quote(var), shlex.quote(env[var])) for var in env]),
                        shlex.quote('mkdir -p %s ; cd %s ; %s' % (
                            shlex.quote(cwd),
                            shlex.quote(cwd),
                            ' '.join([shlex.quote(token) for token in cmd]),
                        )),
                    ),
                ]
            else:
                args += [
                    'su',
                    '-',
                    self.user,
                    '-c',
                    'env - %s sh -c %s' % (
                        ' '.join(['%s=%s' % (shlex.quote(var), shlex.quote(env[var])) for var in env]),
                        shlex.quote(' '.join([shlex.quote(token) for token in cmd])),
                    ),
                ]

        if output:
            return self.run_output(args, stdin=stdin)
        else:
            return self.run(args, stdin=stdin)

    def lxc_write(self, path, data, cwd='', root=False):
        self.lxc_run([
            'mkdir',
            '-p',
            os.path.dirname(path)
        ], cwd=cwd, root=root)

        stdin, stdout = os.pipe()
        os.write(stdout, data.encode('utf-8'))
        os.close(stdout)

        self.lxc_run([
            'dd',
            'of=%s' % shlex.quote(path),
        ], cwd=cwd, root=root, stdin=stdin)

    def lxc_jhbuild(self, cmd, output=False):
        return self.lxc_run([
            self.jhbuildexec,
            '-f',
            self.jhbuildrc,
            '--no-interact',
            '--exit-on-error',
        ] + cmd, output=output)

    def pull(self):
        if os.geteuid() == 0:
            raise EnvironmentError('Do not run this as root')

        os.makedirs(os.path.dirname(self.lxcconf), exist_ok=True)

        with open(self.lxcconf, 'w') as f:
            f.write('lxc.include = /etc/lxc/default.conf\n')

            # TODO: get effective uid
            f.write('lxc.id_map = u 0 100000 1000\n')
            f.write('lxc.id_map = u 1000 1000 1\n')
            f.write('lxc.id_map = u 1001 101001 64535\n')

            # TODO: get effective gid
            f.write('lxc.id_map = g 0 100000 1000\n')
            f.write('lxc.id_map = g 1000 1000 1\n')
            f.write('lxc.id_map = g 1001 101001 64535\n')

            f.write('lxc.mount.entry = %s %s none bind,optional,create=dir\n' % (self.installdir, self.relprefix))

            if self.options.jhtarballs:
                f.write('lxc.mount.entry = %s %s none bind,optional,create=dir\n' % (self.options.jhtarballs, self.reljhtarballs))

            if self.options.jhmirror:
                f.write('lxc.mount.entry = %s %s none bind,optional,create=dir\n' % (self.options.jhmirror, self.reljhmirror))

            if self.options.ccache:
                f.write('lxc.mount.entry = %s %s none bind,optional,create=dir\n' % (self.options.ccache, self.relccache))

        self.run([
            'lxc-create',
            '-n',
            self.container,
            '-f',
            self.lxcconf,
            '-t',
            'download',
            '--',
            '-d',
            self.options.dist,
            '-r',
            self.options.release,
            '-a',
            self.options.arch,
        ])

        self.run([
            'lxc-start',
            '-n',
            self.container,
        ])

        self.run([
            'lxc-wait',
            '-n',
            self.container,
            '-s',
            'RUNNING',
        ])

        # TODO: wait for networking
        time.sleep(5)

        self.lxc_run([
            'useradd',
            '-m',
            self.user,
        ], root=True)

        self.lxc_run([
            'chown',
            '%s:' % self.user,
            self.home,
        ], root=True)

        if self.options.aptcache:
            self.lxc_run([
                'sed',
                '-i',
                '-e',
                's/https\\?:\\/\\//%s\\//' % self.options.aptcache.replace('/', '\\/'),
                self.sources,
            ], root=True)

        self.lxc_run([
            'apt',
            'update',
        ], root=True)

        self.lxc_run([
            'apt-get',
            '-y',
            'install',
        ] + self.bootstrap, root=True)

        self.lxc_run([
            'git',
            'clone',
            'https://git.gnome.org/browse/jhbuild',
            self.jhbuildsrc,
        ])

        self.lxc_run([
            './autogen.sh',
            '--prefix=%s' % self.prefix,
        ], cwd=self.jhbuildsrc)

        self.lxc_run([
            'make',
        ], cwd=self.jhbuildsrc)

        self.lxc_run([
            'make',
            'install',
        ], cwd=self.jhbuildsrc)

        self.lxc_write(self.jhbuildrc, (
            'moduleset = \'%s\'\n' % self.options.moduleset +
            'tarballdir = \'%s\'\n' % self.jhtarballs +
            'dvcs_mirror_dir = \'%s\'\n' % self.jhmirror +
            'checkoutroot = \'%s\'\n' % self.jhcheckout +
            'prefix = \'%s\'\n' % self.prefix +
            'use_local_modulesets = True\n' +
            'nonetwork = True\n'
        ))

        self.lxc_jhbuild([
            'update',
        ] + self.options.modules)

        sysdeps = self.lxc_jhbuild([
            'sysdeps',
            '--dump-all',
        ] + self.options.modules, output=True)

        build_packages = []

        for line in sysdeps.splitlines():
            found = False

            for sysdep in line.split(','):
                if sysdep in depends:
                    if depends[sysdep]:
                        if depends[sysdep][0]:
                            build_packages.append(depends[sysdep][0])
                        if depends[sysdep][1]:
                            self.stage_packages.append(depends[sysdep][1])

                    found = True
                    break

            if not found:
                logger.warning('No package found providing %s' % sysdep)

        self.lxc_run([
            'apt-get',
            '-y',
            'install',
        ] + build_packages, root=True)

    def build(self):
        self.lxc_jhbuild([
            'build',
        ] + self.options.modules)

    def snap_fileset(self):
        return os.listdir(self.installdir)

    def clean_build(self):
        self.lxc_run([
            'rm',
            '-rf',
            self.jhcheckout,
        ])

    def clean_pull(self):
        try:
            self.run([
                'lxc-stop',
                '-n',
                self.container,
            ])
        except:
            pass

        self.run([
            'lxc-wait',
            '-n',
            self.container,
            '-s',
            'STOPPED',
        ])

        self.run([
            'lxc-destroy',
            '-n',
            self.container,
            '-s',
        ])

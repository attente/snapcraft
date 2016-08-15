# hacks:
# 1. add 'mount -> /dev/{**,},' to /etc/apparmor.d/usr.bin.lxc-start and reload the profile

import os
import time # FIXME: needed for sleep
import snapcraft

class JHBuildPlugin(snapcraft.BasePlugin):

    def __init__(self, name, options, project=None):
        super().__init__(name, options, project)
        self.lxcdir = os.path.join(self.sourcedir, 'lxc')
        self.lxcconf = os.path.join(self.sourcedir, 'lxc.conf')

    def _lxc_write_conf(self):
        with open(self.lxcconf, 'w') as f:
            f.write('lxc.include = \'/etc/lxc/default.conf\'\n'
                    '\n'
                    'lxc.id_map = u 0 100000 65536\n'
                    'lxc.id_map = g 0 100000 65536\n'
                    '\n'
                    'lxc.network.type = veth\n'
                    'lxc.network.link = lxcbr0\n'
                    'lxc.network.flags = up\n'
                    'lxc.network.hwaddr = 00:16:3e:xx:xx:xx\n')

    def _lxc_create(self, arch):
        self.run(['lxc-create',
                  '-P', self.lxcdir, # FIXME: doesn't work
                  '-f', self.lxcconf, # FIXME: doesn't work
                  '-n', 'jhbuild',
                  '-t', 'download',
                  '--',
                  '-d', 'ubuntu',
                  '-r', 'xenial',
                  '-a', arch])

    def _lxc_wait(self):
        self.run(['lxc-wait',
                  '-P', self.lxcdir, # FIXME: doesn't work
                  '-n', 'jhbuild',
                  '-s', 'RUNNING'])

    def _lxc_start(self):
        self.run(['lxc-start',
                  '-P', self.lxcdir, # FIXME: doesn't work
                  '-f', self.lxcconf, # FIXME: doesn't work
                  '-n', 'jhbuild'])

    def _lxc_run_root(self, argv):
        self.run(['lxc-attach',
                  '-P', self.lxcdir, # FIXME: doesn't work
                  '-n', 'jhbuild',
                  '--'] + argv)

    def _lxc_run_user(self, argv):
        self._lxc_run_root(['su', '-c', argv, '-', 'ubuntu'])

    def pull(self):
        self._lxc_write_conf()
        self._lxc_create('amd64') # FIXME: get architecture
        self._lxc_start()
        self._lxc_wait()
        time.sleep(15) # FIXME: waiting for networking
        self._lxc_run_root(['apt', 'update'])
        self._lxc_run_root(['apt', 'install', '-y', 'git', 'ca-certificates', 'make',
                            'autoconf', 'automake', 'gettext', 'pkg-config', 'yelp-tools', 'autopoint',
                            'libtool', 'docbook-xsl', 'libxml-parser-perl', 'cvs', 'subversion', 'flex', 'bison',
                            'libxslt1-dev', 'libffi-dev', 'zlib1g-dev', 'libpcre3-dev', 'libxml2-dev', 'intltool'])
        self._lxc_run_root(['mkdir', '/snap'])
        self._lxc_run_root(['chown', 'ubuntu:', '/snap'])
        self._lxc_run_user('git clone https://git.gnome.org/browse/jhbuild')
        self._lxc_run_user('cd jhbuild ; ./autogen.sh ; make ; make install')
        self._lxc_run_user('mkdir .config')
        self._lxc_run_user('echo \"prefix = \'/snap/%s/%s\'\" >> .config/jhbuildrc' % (self.name, 'current')) # FIXME: should we use current revision?
        self._lxc_run_user('jhbuild update glib')
        self._lxc_run_user('jhbuild build glib')

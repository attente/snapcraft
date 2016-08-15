import os
import snapcraft

class JHBuildPlugin(snapcraft.BasePlugin):

    def __init__(self, name, options, project):
        super().__init__(name, options, project)

        # JHBuild is a set of Python scripts
        self.stage_packages.append('python')

    def pull(self):
        jhbuildrc = os.path.join(self.installdir, 'etc', 'jhbuildrc')
        os.makedirs(os.path.join(self.installdir, 'etc'), exist_ok=True)

        with open(jhbuildrc, 'w') as f:
            f.write('tarballdir = \'%s\'\n' % os.path.join(self.sourcedir, 'tarball'))
            f.write('dvcs_mirror_dir = \'%s\'\n' % '/home/william/Code/jhbuild/mirror') # FIXME
            # f.write('dvcs_mirror_dir = \'%s\'\n' % os.path.join(self.sourcedir, 'mirror'))
            f.write('checkoutroot = \'%s\'\n' % os.path.join(self.sourcedir, 'checkout'))
            f.write('buildroot = \'%s\'\n' % self.builddir)
            f.write('prefix = \'%s\'\n' % self.installdir)

        jhbuild_srcdir = os.path.join(self.sourcedir, 'jhbuild')
        snapcraft.internal.sources.Git('/home/william/Code/jhbuild/jhbuild', jhbuild_srcdir).pull() # FIXME
        # snapcraft.internal.sources.Git('https://git.gnome.org/browse/jhbuild', jhbuild_srcdir).pull()
        self.run([os.path.join(jhbuild_srcdir, 'autogen.sh'), '--prefix=%s' % self.installdir], jhbuild_srcdir)
        self.run(['make'], jhbuild_srcdir)
        self.run(['make', 'install'], jhbuild_srcdir)

        self.run([os.path.join(self.installdir, 'bin', 'jhbuild'), '-f', jhbuildrc, 'update', self.options.source])

    def build(self):
        self.run([os.path.join(self.installdir, 'bin', 'jhbuild'), '-f', jhbuildrc, 'build', self.options.source])

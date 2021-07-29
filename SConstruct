# -*- python -*-
from __future__ import print_function

import sys, os, os.path

AddOption('--build', dest='build', type='string', nargs=1, action='store',
          default='release', help='build type')
AddOption('--params', dest='params', type='string', nargs=1, action='store',
          default='params.py', help='build params')

root = DefaultEnvironment(tools = ['gcc'])
root.root = Dir('#').abspath
root.buildroot = Dir('.build').abspath 
root.tmp = os.path.join(root.buildroot, '.temp')
root.build = GetOption('build').lower()

root.Append(ROOT = root.root)
root.Append(BUILDROOT = root.buildroot)
root.Append(TMP = root.tmp)
root.Append(BUILD = root.build)
root.params = File(GetOption('params')).abspath

Execute(Mkdir(root.Dir('${BUILDROOT}').abspath))
Execute(Mkdir(root.Dir('${TMP}').abspath))

vars = Variables(root.params, ARGUMENTS)
vars.AddVariables(('CPPDEFINES', ''),
                  ('CPPFLAGS', ''),
                  ('CXXFLAGS', ''),
                  ('CFLAGS', ''),
                  ('ASFLAGS', ''),
                  ('LINKFLAGS', ''),
                  ('CXX', ''),
                  ('CC', ''),
                  ('AS', ''),
                  ('RANLIB', ''),
                  ('AR', ''),
                  ('LIBS', ''),
                  ('TOOLS', ''),
                  ('SDK_ROOT', ''),
                  ('ELF2UF2', ''))


def NewEnvironment(self, *argv, **aars):
  ENV = {'PATH' : os.environ['PATH'],
         'TMP' : self.tmp}

  env = self.Environment(*argv, ENV = ENV, variables = vars, **aars)

  env.root = self.root
  env.build = self.build
  env.buildroot = self.buildroot
  env.params = self.params

  env.Append(TMP = self.Dir('${TMP}'))
  env.Append(CPPPATH = Dir('#/'))
  env.Append(BUILDROOT = self.buildroot)
  
  libroot = Dir('#/lib')
  env.Append(LIBROOT = libroot)
  env.Append(LIBPATH = libroot)

  binroot = Dir('#/bin')
  env.Append(BINROOT = binroot)

  env.Append(CXXCOMSTR = 'compiling c++ $SOURCE')
  env.Append(CCCOMSTR = 'compiling c $SOURCE')
  env.Append(ASPPCOMSTR = 'assembling $SOURCE')
  env.Append(LINKCOMSTR = 'linking $TARGET')
  env.Append(ARCOMSTR = 'archiving $TARGET')
  return env

root.AddMethod(NewEnvironment, 'NewEnvironment')

def NewSConscript(self, target):
  name = os.path.basename(target.abspath)
  name = name.split('.')[0]
  buildroot = os.path.join(self.buildroot, '.' + name)
  buildroot = self.Dir(buildroot).abspath
  module = self.SConscript(target, variant_dir = buildroot, duplicate=0)
  return module

root.AddMethod(NewSConscript, 'NewSConscript')
Export('root')

targets = Glob('src/*/*.scons.py')
targets = [root.NewSConscript(target) for target in targets]
targets = [item for item in targets if item != None and item != (None, None)]

Default(targets)

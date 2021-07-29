# -*- python -*-
from __future__ import print_function

import sys, os, os.path

Import('root')

srcs = ['${SDK_ROOT}/build/src/rp2_common/boot_stage2/bs2_default_padded_checksummed.S'
  , 'blink.cpp']

env = root.NewEnvironment()
env.Append(LINKFLAGS=['-Wl,-Map=blink.elf.map']
    , CPPFLAGS = '-DPICO_TARGET_NAME=\\\"blink\\\"')

program = env.Program('blink.elf', srcs, LIBS=['stdpico']) #
module = env.Command('blink.uf2', program, '${ELF2UF2} $SOURCE $TARGET')

uf2 = env.Install("${BINROOT}", module)

Return('uf2')
from __future__ import print_function

import sys, os, os.path

Import('root')

SRCS = ['${SDK_ROOT}/src/rp2_common/pico_stdlib/stdlib.c'
  , '${SDK_ROOT}/src/rp2_common/pico_platform/platform.c'
  , '${SDK_ROOT}/src/rp2_common/pico_runtime/runtime.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_gpio/gpio.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_claim/claim.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_sync/sync.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_uart/uart.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_divider/divider.S'
  , '${SDK_ROOT}/src/rp2_common/hardware_timer/timer.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_clocks/clocks.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_irq/irq.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_irq/irq_handler_chain.S'
  , '${SDK_ROOT}/src/rp2_common/hardware_pll/pll.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_vreg/vreg.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_watchdog/watchdog.c'
  , '${SDK_ROOT}/src/rp2_common/hardware_xosc/xosc.c'
  , '${SDK_ROOT}/src/rp2_common/pico_printf/printf.c'
  , '${SDK_ROOT}/src/rp2_common/pico_bit_ops/bit_ops_aeabi.S'
  , '${SDK_ROOT}/src/rp2_common/pico_bootrom/bootrom.c'
  , '${SDK_ROOT}/src/rp2_common/pico_divider/divider.S'
  , '${SDK_ROOT}/src/rp2_common/pico_double/double_aeabi.S'
  , '${SDK_ROOT}/src/rp2_common/pico_double/double_init_rom.c'
  , '${SDK_ROOT}/src/rp2_common/pico_double/double_math.c'  
  , '${SDK_ROOT}/src/rp2_common/pico_double/double_v1_rom_shim.S'
  , '${SDK_ROOT}/src/rp2_common/pico_int64_ops/pico_int64_ops_aeabi.S'
  , '${SDK_ROOT}/src/rp2_common/pico_float/float_aeabi.S'
  , '${SDK_ROOT}/src/rp2_common/pico_float/float_init_rom.c'
  , '${SDK_ROOT}/src/rp2_common/pico_float/float_math.c'
  , '${SDK_ROOT}/src/rp2_common/pico_float/float_v1_rom_shim.S'
  , '${SDK_ROOT}/src/rp2_common/pico_malloc/pico_malloc.c'
  , '${SDK_ROOT}/src/rp2_common/pico_mem_ops/mem_ops_aeabi.S'
  , '${SDK_ROOT}/src/rp2_common/pico_standard_link/crt0.S'
  , '${SDK_ROOT}/src/rp2_common/pico_standard_link/new_delete.cpp'
  , '${SDK_ROOT}/src/rp2_common/pico_standard_link/binary_info.c'
  , '${SDK_ROOT}/src/rp2_common/pico_stdio/stdio.c'
  , '${SDK_ROOT}/src/rp2_common/pico_stdio_uart/stdio_uart.c'
  , '${SDK_ROOT}/src/common/pico_time/time.c'
  , '${SDK_ROOT}/src/common/pico_time/timeout_helper.c'
  , '${SDK_ROOT}/src/common/pico_sync/sem.c'
  , '${SDK_ROOT}/src/common/pico_sync/lock_core.c'
  , '${SDK_ROOT}/src/common/pico_sync/mutex.c'
  , '${SDK_ROOT}/src/common/pico_sync/critical_section.c'
  , '${SDK_ROOT}/src/common/pico_util/datetime.c'
  , '${SDK_ROOT}/src/common/pico_util/pheap.c'
  , '${SDK_ROOT}/src/common/pico_util/queue.c'
]

env = root.NewEnvironment()

library = env.StaticLibrary('stdpico', SRCS)
stdpico = env.Install("${LIBROOT}", library)
env.Alias('stdpico', stdpico)

Return('stdpico')
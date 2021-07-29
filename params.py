import os

CXX = 'arm-none-eabi-g++'
CC = 'arm-none-eabi-gcc'
AS = 'arm-none-eabi-as'
OBJCOPY = 'arm-none-eabi-objcopy'
OBJDUMP = 'arm-none-eabi-objdump'
RANLIB = 'arm-none-eabi-ranlib'
AR = 'arm-none-eabi-ar'

TOOLS = ['mingw']

SDK_ROOT = os.environ['PICO_SDK_PATH']
ELF2UF2 = "${SDK_ROOT}/build/elf2uf2/elf2uf2"

CFLAGS = ['-O2'
    , '-Os'
    , '-mcpu=cortex-m0plus'
    , '-mthumb'
    , '-Wall'
    , '-Wno-format'
    , '-Wno-unused-function'
    , '-Wno-maybe-uninitialized'
    , '-ffunction-sections'
    , '-fdata-sections'
    , '-fno-exceptions'
    , '-fno-unwind-tables'
    , '-I${SDK_ROOT}\\build\\generated\\pico_base'
    , '-I${SDK_ROOT}\\src\\boards\\include'
    , '-I${SDK_ROOT}\\src\\rp2040\\hardware_regs\\include'
    , '-I${SDK_ROOT}\\src\\rp2040\\hardware_structs\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_stdlib\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_base\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_time\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_sync\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_util\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_bit_ops\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_divider\\include'
    , '-I${SDK_ROOT}\\src\\common\\pico_binary_info\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_gpio\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_platform\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_base\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_claim\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_sync\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_uart\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_divider\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_timer\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_runtime\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_clocks\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_irq\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_resets\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_pll\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_vreg\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_watchdog\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\hardware_xosc\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_printf\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_bootrom\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_double\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_int64_ops\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_float\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_malloc\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\boot_stage2\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_stdio\\include'
    , '-I${SDK_ROOT}\\src\\rp2_common\\pico_stdio_uart\\include'
    ]
ASFLAGS = CFLAGS
CXXFLAGS = CFLAGS + ['-std=gnu++17'
    , '-fno-rtti'
    , '-fno-use-cxa-atexit'
    #
]
#
LINKFLAGS = [
    '-mcpu=cortex-m0plus'
    , '-mthumb'
    , '--specs=nosys.specs'
    , '-Wl,--build-id=none'
    , '-Wl,--wrap=sprintf'
    , '-Wl,--wrap=snprintf' 
    , '-Wl,--wrap=vsnprintf' 
    , '-Wl,--wrap=__clzsi2'
    , '-Wl,--wrap=__clzdi2'
    , '-Wl,--wrap=__ctzsi2'
    , '-Wl,--wrap=__ctzdi2v'
    , '-Wl,--wrap=__popcountsi2'
    , '-Wl,--wrap=__popcountdi2'
    , '-Wl,--wrap=__clz'
    , '-Wl,--wrap=__clzl'
    , '-Wl,--wrap=__clzll' 
    , '-Wl,--wrap=__aeabi_idiv'
    , '-Wl,--wrap=__aeabi_idivmod'
    , '-Wl,--wrap=__aeabi_ldivmod'
    , '-Wl,--wrap=__aeabi_uidiv'
    , '-Wl,--wrap=__aeabi_uidivmod' 
    , '-Wl,--wrap=__aeabi_uldivmod'
    , '-Wl,--wrap=__aeabi_dadd'
    , '-Wl,--wrap=__aeabi_ddiv'
    , '-Wl,--wrap=__aeabi_dmul'
    , '-Wl,--wrap=__aeabi_drsub' 
    , '-Wl,--wrap=__aeabi_dsub'
    , '-Wl,--wrap=__aeabi_cdcmpeq' 
    , '-Wl,--wrap=__aeabi_cdrcmple' 
    , '-Wl,--wrap=__aeabi_cdcmple'
    , '-Wl,--wrap=__aeabi_dcmpeq'
    , '-Wl,--wrap=__aeabi_dcmplt'
    , '-Wl,--wrap=__aeabi_dcmple'
    , '-Wl,--wrap=__aeabi_dcmpge'
    , '-Wl,--wrap=__aeabi_dcmpgt'
    , '-Wl,--wrap=__aeabi_dcmpun'
    , '-Wl,--wrap=__aeabi_i2d'
    , '-Wl,--wrap=__aeabi_l2d'
    , '-Wl,--wrap=__aeabi_ui2d'
    , '-Wl,--wrap=__aeabi_ul2d'
    , '-Wl,--wrap=__aeabi_d2iz'
    , '-Wl,--wrap=__aeabi_d2lz'
    , '-Wl,--wrap=__aeabi_d2uiz'
    , '-Wl,--wrap=__aeabi_d2ulz'
    , '-Wl,--wrap=__aeabi_d2f'
    , '-Wl,--wrap=sqrt'
    , '-Wl,--wrap=cos'
    , '-Wl,--wrap=sin'
    , '-Wl,--wrap=tan'
    , '-Wl,--wrap=atan2'
    , '-Wl,--wrap=exp'
    , '-Wl,--wrap=log'
    , '-Wl,--wrap=ldexp'
    , '-Wl,--wrap=copysign'
    , '-Wl,--wrap=trunc'
    , '-Wl,--wrap=floor'
    , '-Wl,--wrap=ceil'
    , '-Wl,--wrap=round'
    , '-Wl,--wrap=sincos'
    , '-Wl,--wrap=asin'
    , '-Wl,--wrap=acos'
    , '-Wl,--wrap=atan'
    , '-Wl,--wrap=sinh'
    , '-Wl,--wrap=cosh'
    , '-Wl,--wrap=tanh'
    , '-Wl,--wrap=asinh'
    , '-Wl,--wrap=acosh'
    , '-Wl,--wrap=atanh'
    , '-Wl,--wrap=exp2'
    , '-Wl,--wrap=log2'
    , '-Wl,--wrap=exp10'
    , '-Wl,--wrap=log10'
    , '-Wl,--wrap=pow'
    , '-Wl,--wrap=powint'
    , '-Wl,--wrap=hypot'
    , '-Wl,--wrap=cbrt'
    , '-Wl,--wrap=fmod'
    , '-Wl,--wrap=drem'
    , '-Wl,--wrap=remainder'
    , '-Wl,--wrap=remquo'
    , '-Wl,--wrap=expm1'
    , '-Wl,--wrap=log1p'
    , '-Wl,--wrap=fma' 
    , '-Wl,--wrap=__aeabi_lmul'
    , '-Wl,--wrap=__aeabi_fadd'
    , '-Wl,--wrap=__aeabi_fdiv'
    , '-Wl,--wrap=__aeabi_fmul'
    , '-Wl,--wrap=__aeabi_frsub'
    , '-Wl,--wrap=__aeabi_fsub'
    , '-Wl,--wrap=__aeabi_cfcmpeq'
    , '-Wl,--wrap=__aeabi_cfrcmple'
    , '-Wl,--wrap=__aeabi_cfcmple'
    , '-Wl,--wrap=__aeabi_fcmpeq'
    , '-Wl,--wrap=__aeabi_fcmplt'
    , '-Wl,--wrap=__aeabi_fcmple'
    , '-Wl,--wrap=__aeabi_fcmpge'
    , '-Wl,--wrap=__aeabi_fcmpgt'
    , '-Wl,--wrap=__aeabi_fcmpun'
    , '-Wl,--wrap=__aeabi_i2f'
    , '-Wl,--wrap=__aeabi_l2f'
    , '-Wl,--wrap=__aeabi_ui2f'
    , '-Wl,--wrap=__aeabi_ul2f'
    , '-Wl,--wrap=__aeabi_f2iz'
    , '-Wl,--wrap=__aeabi_f2lz'
    , '-Wl,--wrap=__aeabi_f2uiz'
    , '-Wl,--wrap=__aeabi_f2ulz'
    , '-Wl,--wrap=__aeabi_f2d'
    , '-Wl,--wrap=sqrtf'
    , '-Wl,--wrap=cosf'
    , '-Wl,--wrap=sinf'
    , '-Wl,--wrap=tanf'
    , '-Wl,--wrap=atan2f'
    , '-Wl,--wrap=expf'
    , '-Wl,--wrap=logf'
    , '-Wl,--wrap=ldexpf'
    , '-Wl,--wrap=copysignf'
    , '-Wl,--wrap=truncf'
    , '-Wl,--wrap=floorf'
    , '-Wl,--wrap=ceilf'
    , '-Wl,--wrap=roundf'
    , '-Wl,--wrap=sincosf'
    , '-Wl,--wrap=asinf'
    , '-Wl,--wrap=acosf'
    , '-Wl,--wrap=atanf'
    , '-Wl,--wrap=sinhf'
    , '-Wl,--wrap=coshf'
    , '-Wl,--wrap=tanhf'
    , '-Wl,--wrap=asinhf'
    , '-Wl,--wrap=acoshf'
    , '-Wl,--wrap=atanhf'
    , '-Wl,--wrap=exp2f'
    , '-Wl,--wrap=log2f'
    , '-Wl,--wrap=exp10f'
    , '-Wl,--wrap=log10f'
    , '-Wl,--wrap=powf'
    , '-Wl,--wrap=powintf'
    , '-Wl,--wrap=hypotf'
    , '-Wl,--wrap=cbrtf'
    , '-Wl,--wrap=fmodf'
    , '-Wl,--wrap=dremf'
    , '-Wl,--wrap=remainderf'
    , '-Wl,--wrap=remquof'
    , '-Wl,--wrap=expm1f'
    , '-Wl,--wrap=log1pf'
    , '-Wl,--wrap=fmaf'
    , '-Wl,--wrap=malloc'
    , '-Wl,--wrap=calloc'
    , '-Wl,--wrap=free'
    , '-Wl,--wrap=memcpy'
    , '-Wl,--wrap=memset' 
    , '-Wl,--wrap=printf'
    , '-Wl,--wrap=vprintf'
    , '-Wl,--wrap=puts'
    , '-Wl,--wrap=putchar'
    , '-Wl,--wrap=getchar'
    , '-Wl,--wrap=__aeabi_memcpy'
    , '-Wl,--wrap=__aeabi_memset'
    , '-Wl,--wrap=__aeabi_memcpy4'
    , '-Wl,--wrap=__aeabi_memset4'
    , '-Wl,--wrap=__aeabi_memcpy8'
    , '-Wl,--wrap=__aeabi_memset8'
    , '-Wl,--script=${SDK_ROOT}/src/rp2_common/pico_standard_link/memmap_default.ld'
    , '-Wl,--gc-sections'
]
#
CPPFLAGS = [
    '-DLIB_PICO_BIT_OPS=1'
    , '-DLIB_PICO_BIT_OPS_PICO=1'
    , '-DLIB_PICO_DIVIDER=1'
    , '-DLIB_PICO_DIVIDER_HARDWARE=1'
    , '-DLIB_PICO_DOUBLE=1'
    , '-DLIB_PICO_DOUBLE_PICO=1'
    , '-DLIB_PICO_FLOAT=1'
    , '-DLIB_PICO_FLOAT_PICO=1'
    , '-DLIB_PICO_INT64_OPS=1'
    , '-DLIB_PICO_INT64_OPS_PICO=1'
    , '-DLIB_PICO_MALLOC=1'
    , '-DLIB_PICO_MEM_OPS=1'
    , '-DLIB_PICO_MEM_OPS_PICO=1'
    , '-DLIB_PICO_PLATFORM=1'
    , '-DLIB_PICO_PRINTF=1'
    , '-DLIB_PICO_PRINTF_PICO=1'
    , '-DLIB_PICO_RUNTIME=1'
    , '-DLIB_PICO_STANDARD_LINK=1'
    , '-DLIB_PICO_STDIO=1'
    , '-DLIB_PICO_STDIO_UART=1'
    , '-DLIB_PICO_STDLIB=1'
    , '-DLIB_PICO_SYNC=1'
    , '-DLIB_PICO_SYNC_CORE=1'
    , '-DLIB_PICO_SYNC_CRITICAL_SECTION=1'
    , '-DLIB_PICO_SYNC_MUTEX=1'
    , '-DLIB_PICO_SYNC_SEM=1'
    , '-DLIB_PICO_TIME=1'
    , '-DLIB_PICO_UTIL=1'
    , '-DPICO_BOARD=\\\"pico\\\"' 
    , '-DPICO_BUILD=1'
    , '-DPICO_COPY_TO_RAM=0'
    , '-DPICO_CXX_ENABLE_EXCEPTIONS=0'
    , '-DPICO_NO_FLASH=0'
    , '-DPICO_NO_HARDWARE=0'
    , '-DPICO_ON_DEVICE=1'
    , '-DPICO_USE_BLOCKED_RAM=0'
    ]

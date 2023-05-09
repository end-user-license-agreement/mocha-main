source: https://github.com/facebook/zstd

dependencies:
- '@toolchain'

artifacts: []

beta_artifacts:
- - lib zstd
  - - lib/decompress/huf_decompress_amd64.S
    - lib/common/debug.c
    - lib/common/entropy_common.c
    - lib/common/error_private.c
    - lib/common/fse_decompress.c
    - lib/common/pool.c
    - lib/common/threading.c
    - lib/common/xxhash.c
    - lib/common/zstd_common.c
    - lib/compress/fse_compress.c
    - lib/compress/hist.c
    - lib/compress/huf_compress.c
    - lib/compress/zstd_compress.c
    - lib/compress/zstd_compress_literals.c
    - lib/compress/zstd_compress_sequences.c
    - lib/compress/zstd_compress_superblock.c
    - lib/compress/zstd_double_fast.c
    - lib/compress/zstd_fast.c
    - lib/compress/zstd_lazy.c
    - lib/compress/zstd_ldm.c
    - lib/compress/zstd_opt.c
    - lib/compress/zstdmt_compress.c
    - lib/decompress/huf_decompress.c
    - lib/decompress/zstd_ddict.c
    - lib/decompress/zstd_decompress.c
    - lib/decompress/zstd_decompress_block.c
    - lib/deprecated/zbuff_common.c
    - lib/deprecated/zbuff_compress.c
    - lib/deprecated/zbuff_decompress.c
    - lib/dictBuilder/cover.c
    - lib/dictBuilder/divsufsort.c
    - lib/dictBuilder/fastcover.c
    - lib/dictBuilder/zdict.c
    - lib/legacy/zstd_v01.c
    - lib/legacy/zstd_v02.c
    - lib/legacy/zstd_v03.c
    - lib/legacy/zstd_v04.c
    - lib/legacy/zstd_v05.c
    - lib/legacy/zstd_v06.c
    - lib/legacy/zstd_v07.c
- - bin zstd
  - - programs/benchfn.c
    - programs/benchzstd.c
    - programs/datagen.c
    - programs/dibio.c
    - programs/fileio.c
    - programs/fileio_asyncio.c
    - programs/timefn.c
    - programs/util.c
    - programs/zstdcli.c
    - programs/zstdcli_trace.c
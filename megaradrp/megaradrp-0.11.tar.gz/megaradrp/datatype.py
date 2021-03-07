
import enum


class DataOrigin(enum.Enum):
    UNKNOWN = 0
    OBSERVED = 1
    PROCESSED = 2
    GENERATED = 3


class MegaraDataType(enum.Enum):
    UNKNOWN = 1
    IMAGE_RAW = 100
    IMAGE_BIAS = 102
    IMAGE_DARK = 103
    IMAGE_SLITFLAT = 104
    IMAGE_FLAT = 105
    IMAGE_COMP = 106
    #
    IMAGE_TWILIGHT = 107
    IMAGE_TEST = 109
    IMAGE_TARGET = 150
    #
    IMAGE_PROCESSED = 200
    MASTER_BPM = 201
    MASTER_BIAS = 202
    MasterBias = 202 # Alias
    MASTER_DARK = 203
    MASTER_SLITFLAT = 204
    DIFFUSE_LIGHT = 211
    #
    RSS_PROCESSED = 300
    MASTER_FLAT = 305
    MasterFiberFlat = 305 # Alias
    MASTER_TWILIGHT = 306
    RSS_WL_PROCESSED = 400
    SPEC_PROCESSED = 500
    MASTER_SENSITIVITY = 503
    STRUCT_PROCESSED = 600
    TRACE_MAP = 601
    MODEL_MAP = 602
    WAVE_CALIB = 603
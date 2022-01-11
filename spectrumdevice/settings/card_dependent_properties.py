from enum import Enum

from spectrum_gmbh.regs import (
    TYP_M2P59XX_X4,
    TYP_FAMILYMASK,
    TYP_M4I22XX_X8,
    TYP_M4I44XX_X8,
    TYP_M4I2210_X8,
    TYP_M4I2211_X8,
    TYP_M4I2212_X8,
    TYP_M4I2220_X8,
    TYP_M4I2221_X8,
    TYP_M4I2223_X8,
    TYP_M4I2230_X8,
    TYP_M4I2233_X8,
    TYP_M4I2234_X8,
    TYP_M4I2280_X8,
    TYP_M4I2281_X8,
    TYP_M4I2283_X8,
    TYP_M4I2290_X8,
    TYP_M4I2293_X8,
    TYP_M4I2294_X8,
    TYP_M4I4410_X8,
    TYP_M4I4411_X8,
    TYP_M4I4420_X8,
    TYP_M4I4421_X8,
    TYP_M4I4450_X8,
    TYP_M4I4451_X8,
    TYP_M4I4470_X8,
    TYP_M4I4471_X8,
    TYP_M4I4480_X8,
    TYP_M4I4481_X8,
    TYP_M4X44XX_X4,
    TYP_M4X4410_X4,
    TYP_M4X4411_X4,
    TYP_M4X4420_X4,
    TYP_M4X4421_X4,
    TYP_M4X4450_X4,
    TYP_M4X4451_X4,
    TYP_M4X4470_X4,
    TYP_M4X4471_X4,
    TYP_M4X4480_X4,
    TYP_M4X4481_X4,
    TYP_M2P5968_X4,
    TYP_M2P5966_X4,
    TYP_M2P5961_X4,
    TYP_M2P5962_X4,
    TYP_M2P5960_X4,
    TYP_M2P5946_X4,
    TYP_M2P5943_X4,
    TYP_M2P5942_X4,
    TYP_M2P5941_X4,
    TYP_M2P5940_X4,
    TYP_M2P5936_X4,
    TYP_M2P5933_X4,
    TYP_M2P5932_X4,
    TYP_M2P5931_X4,
    TYP_M2P5930_X4,
    TYP_M2P5926_X4,
    TYP_M2P5923_X4,
    TYP_M2P5922_X4,
    TYP_M2P5921_X4,
    TYP_M2P5920_X4,
    TYP_M2P5916_X4,
    TYP_M2P5913_X4,
    TYP_M2P5911_X4,
    TYP_M2P5912_X4,
)


class CardType(Enum):
    """An Enum representing the integer values returned by a device when its type identifier is queried by reading the
    SPC_PCITYP register. Only the supported card types are listed: 22xx, 44xx and 59xx family devices."""

    TYP_M4I2210_X8 = TYP_M4I2210_X8
    TYP_M4I2211_X8 = TYP_M4I2211_X8
    TYP_M4I2212_X8 = TYP_M4I2212_X8
    TYP_M4I2220_X8 = TYP_M4I2220_X8
    TYP_M4I2221_X8 = TYP_M4I2221_X8
    TYP_M4I2223_X8 = TYP_M4I2223_X8
    TYP_M4I2230_X8 = TYP_M4I2230_X8
    TYP_M4I2233_X8 = TYP_M4I2233_X8
    TYP_M4I2234_X8 = TYP_M4I2234_X8
    TYP_M4I2280_X8 = TYP_M4I2280_X8
    TYP_M4I2281_X8 = TYP_M4I2281_X8
    TYP_M4I2283_X8 = TYP_M4I2283_X8
    TYP_M4I2290_X8 = TYP_M4I2290_X8
    TYP_M4I2293_X8 = TYP_M4I2293_X8
    TYP_M4I2294_X8 = TYP_M4I2294_X8
    TYP_M4I4410_X8 = TYP_M4I4410_X8
    TYP_M4I4411_X8 = TYP_M4I4411_X8
    TYP_M4I4420_X8 = TYP_M4I4420_X8
    TYP_M4I4421_X8 = TYP_M4I4421_X8
    TYP_M4I4450_X8 = TYP_M4I4450_X8
    TYP_M4I4451_X8 = TYP_M4I4451_X8
    TYP_M4I4470_X8 = TYP_M4I4470_X8
    TYP_M4I4471_X8 = TYP_M4I4471_X8
    TYP_M4I4480_X8 = TYP_M4I4480_X8
    TYP_M4I4481_X8 = TYP_M4I4481_X8
    TYP_M4X44XX_X4 = TYP_M4X44XX_X4
    TYP_M4X4410_X4 = TYP_M4X4410_X4
    TYP_M4X4411_X4 = TYP_M4X4411_X4
    TYP_M4X4420_X4 = TYP_M4X4420_X4
    TYP_M4X4421_X4 = TYP_M4X4421_X4
    TYP_M4X4450_X4 = TYP_M4X4450_X4
    TYP_M4X4451_X4 = TYP_M4X4451_X4
    TYP_M4X4470_X4 = TYP_M4X4470_X4
    TYP_M4X4471_X4 = TYP_M4X4471_X4
    TYP_M4X4480_X4 = TYP_M4X4480_X4
    TYP_M4X4481_X4 = TYP_M4X4481_X4
    TYP_M2P5911_X4 = TYP_M2P5911_X4
    TYP_M2P5912_X4 = TYP_M2P5912_X4
    TYP_M2P5913_X4 = TYP_M2P5913_X4
    TYP_M2P5916_X4 = TYP_M2P5916_X4
    TYP_M2P5920_X4 = TYP_M2P5920_X4
    TYP_M2P5921_X4 = TYP_M2P5921_X4
    TYP_M2P5922_X4 = TYP_M2P5922_X4
    TYP_M2P5923_X4 = TYP_M2P5923_X4
    TYP_M2P5926_X4 = TYP_M2P5926_X4
    TYP_M2P5930_X4 = TYP_M2P5930_X4
    TYP_M2P5931_X4 = TYP_M2P5931_X4
    TYP_M2P5932_X4 = TYP_M2P5932_X4
    TYP_M2P5933_X4 = TYP_M2P5933_X4
    TYP_M2P5936_X4 = TYP_M2P5936_X4
    TYP_M2P5940_X4 = TYP_M2P5940_X4
    TYP_M2P5941_X4 = TYP_M2P5941_X4
    TYP_M2P5942_X4 = TYP_M2P5942_X4
    TYP_M2P5943_X4 = TYP_M2P5943_X4
    TYP_M2P5946_X4 = TYP_M2P5946_X4
    TYP_M2P5960_X4 = TYP_M2P5960_X4
    TYP_M2P5961_X4 = TYP_M2P5961_X4
    TYP_M2P5962_X4 = TYP_M2P5962_X4
    TYP_M2P5966_X4 = TYP_M2P5966_X4
    TYP_M2P5968_X4 = TYP_M2P5968_X4


MEMSIZE_STEP_SIZES = {
    TYP_M2P59XX_X4 & TYP_FAMILYMASK: 8,
    TYP_M4I22XX_X8 & TYP_FAMILYMASK: 32,
    TYP_M4I44XX_X8 & TYP_FAMILYMASK: 16,
}


def get_memsize_step_size(card_type: CardType) -> int:
    """Get the step size for FIFO mode acquisition length (MEMSIZE) and post trigger length for a card its CardType."""
    return MEMSIZE_STEP_SIZES[card_type.value & TYP_FAMILYMASK]
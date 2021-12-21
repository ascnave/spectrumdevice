from abc import ABC, abstractmethod
from typing import List, Optional, Union, Tuple, Sequence

from numpy import ndarray

from pyspecde.settings import SpectrumRegisterLength
from pyspecde.settings.device_modes import AcquisitionMode, ClockMode
from pyspecde.settings.status import CARD_STATUS_TYPE, STAR_HUB_STATUS_TYPE
from pyspecde.settings.channel import SpectrumChannelName
from pyspecde.settings.io_lines import AvailableIOModes
from pyspecde.settings.triggering import TriggerSource, ExternalTriggerMode
from pyspecde.settings.card_features import CardFeature, AdvancedCardFeature
from pyspecde.settings.transfer_buffer import TransferBuffer, CardToPCDataTransferBuffer


class SpectrumChannelInterface(ABC):
    """Defines the public interface for control of the channels of Spectrum Digitizer device. All properties are read-
    only and must be set with their respective setter methods."""

    @property
    @abstractmethod
    def name(self) -> SpectrumChannelName:
        raise NotImplementedError

    @property
    @abstractmethod
    def vertical_range_mv(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_vertical_range_mv(self, vertical_range: int) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def vertical_offset_percent(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_vertical_offset_percent(self, offset: int) -> None:
        raise NotImplementedError()


class SpectrumDeviceInterface(ABC):
    """Defines the public interface for control of all Spectrum digitizer devices, be they StarHub composite devices
    (e.g. the NetBox) or individual digitizer cards. All properties are read-only and must be set with their respective
    setter methods."""

    @property
    @abstractmethod
    def connected(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def reconnect(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError()

    @property
    def status(self) -> Union[CARD_STATUS_TYPE, STAR_HUB_STATUS_TYPE]:
        raise NotImplementedError()

    @abstractmethod
    def start_acquisition(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def stop_acquisition(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def wait_for_acquisition_to_complete(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def start_transfer(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def stop_transfer(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def wait_for_transfer_to_complete(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def transfer_buffers(self) -> List[TransferBuffer]:
        raise NotImplementedError()

    @abstractmethod
    def define_transfer_buffer(self, buffer: Optional[List[CardToPCDataTransferBuffer]] = None) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_waveforms(self) -> List[ndarray]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def channels(self) -> Sequence[SpectrumChannelInterface]:
        raise NotImplementedError()

    @property
    @abstractmethod
    def enabled_channels(self) -> List[int]:
        raise NotImplementedError()

    @abstractmethod
    def set_enabled_channels(self, channels_nums: List[int]) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def acquisition_length_in_samples(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_acquisition_length_in_samples(self, length_in_samples: int) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def post_trigger_length_in_samples(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_post_trigger_length_in_samples(self, length_in_samples: int) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def acquisition_mode(self) -> AcquisitionMode:
        raise NotImplementedError()

    @abstractmethod
    def set_acquisition_mode(self, mode: AcquisitionMode) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def timeout_ms(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_timeout_ms(self, timeout_in_ms: int) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def trigger_sources(self) -> List[TriggerSource]:
        raise NotImplementedError()

    @abstractmethod
    def set_trigger_sources(self, source: List[TriggerSource]) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def external_trigger_mode(self) -> ExternalTriggerMode:
        raise NotImplementedError()

    @abstractmethod
    def set_external_trigger_mode(self, mode: ExternalTriggerMode) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def external_trigger_level_mv(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_external_trigger_level_mv(self, level: int) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def external_trigger_pulse_width_in_samples(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_external_trigger_pulse_width_in_samples(self, width: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def apply_channel_enabling(self) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def clock_mode(self) -> ClockMode:
        raise NotImplementedError()

    @abstractmethod
    def set_clock_mode(self, mode: ClockMode) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def sample_rate_hz(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def set_sample_rate_hz(self, rate: int) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def available_io_modes(self) -> AvailableIOModes:
        raise NotImplementedError()

    @property
    @abstractmethod
    def feature_list(self) -> Tuple[List[CardFeature], List[AdvancedCardFeature]]:
        raise NotImplementedError()

    @abstractmethod
    def write_to_spectrum_device_register(
        self,
        spectrum_register: int,
        value: int,
        length: SpectrumRegisterLength = SpectrumRegisterLength.THIRTY_TWO,
    ) -> None:
        raise NotImplementedError()

    @abstractmethod
    def read_spectrum_device_register(
        self,
        spectrum_register: int,
        length: SpectrumRegisterLength = SpectrumRegisterLength.THIRTY_TWO,
    ) -> int:
        raise NotImplementedError()
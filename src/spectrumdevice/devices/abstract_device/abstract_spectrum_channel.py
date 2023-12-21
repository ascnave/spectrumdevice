"""Provides a partially-implemented abstract class common to individual channels of Spectrum devices."""
from abc import abstractmethod
from typing import TypeVar, Generic

# Christian Baker, King's College London
# Copyright (c) 2021 School of Biomedical Engineering & Imaging Sciences, King's College London
# Licensed under the MIT. You may obtain a copy at https://opensource.org/licenses/MIT.

from spectrumdevice.devices.abstract_device.interfaces import SpectrumChannelInterface, SpectrumAnalogChannelInterface
from spectrumdevice.devices.abstract_device.abstract_spectrum_card import AbstractSpectrumCard
from spectrumdevice.settings.channel import SpectrumAnalogChannelName, SpectrumChannelName


ChannelNameType = TypeVar("ChannelNameType", bound=SpectrumChannelName)


class AbstractSpectrumChannel(SpectrumChannelInterface, Generic[ChannelNameType]):
    """Partially implemented abstract superclass contain code common for controlling an individual channel or IO Line of
    all spectrum devices."""

    @property
    @abstractmethod
    def _name_prefix(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _make_name(self, channel_number: int) -> ChannelNameType:
        raise NotImplementedError

    def __init__(self, channel_number: int, parent_device: AbstractSpectrumCard):
        self._name = self._make_name(channel_number)
        self._parent_device = parent_device
        self._enabled = True

    @property
    def name(self) -> ChannelNameType:
        """The identifier assigned by the spectrum driver, formatted as an Enum by the settings package.

        Returns:
            name (`SpectrumChannelName`): The name of the channel, as assigned by the driver."""
        return self._name

    @property
    def _number(self) -> int:
        return int(self.name.name.split(self._name_prefix)[-1])

    def __eq__(self, other: object) -> bool:
        if isinstance(other, AbstractSpectrumChannel):
            return (self.name == other.name) and (self._parent_device == other._parent_device)
        else:
            raise NotImplementedError()

    def __str__(self) -> str:
        return f"{self._name.name} of {self._parent_device}"

    def __repr__(self) -> str:
        return str(self)


class AbstractSpectrumAnalogChannel(AbstractSpectrumChannel[SpectrumAnalogChannelName], SpectrumAnalogChannelInterface):
    """Partially implemented abstract superclass contain code common for controlling an individual analog channel of all
    spectrum devices."""

    @property
    def _name_prefix(self) -> str:
        return "CHANNEL"

    def _make_name(self, channel_number: int) -> SpectrumAnalogChannelName:
        return SpectrumAnalogChannelName[f"{self._name_prefix}{channel_number}"]

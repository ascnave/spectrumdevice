"""Standard Single Mode (SPC_REC_STD_SINGLE) example. The function defined here is used by the tests module as an
integration test."""

from typing import List, Optional

from numpy import ndarray

from spectrumdevice import MockSpectrumCard, SpectrumCard
from spectrumdevice.devices.waveform import Waveform
from spectrumdevice.settings import (
    AcquisitionMode,
    CardType,
    TriggerSource,
    ExternalTriggerMode,
    TriggerSettings,
    AcquisitionSettings,
)


def standard_single_mode_example(
    mock_mode: bool, trigger_source: TriggerSource, device_number: int, ip_address: Optional[str] = None
) -> List[Waveform]:

    if not mock_mode:
        # Connect to a networked device. To connect to a local (PCIe) device, do not provide an ip_address.
        card = SpectrumCard(device_number=device_number, ip_address=ip_address)
    else:
        # Set up a mock device
        card = MockSpectrumCard(
            device_number=device_number,
            card_type=CardType.TYP_M2P5966_X4,
            mock_source_frame_rate_hz=10.0,
            num_modules=2,
            num_channels_per_module=4,
        )

    # Trigger settings
    trigger_settings = TriggerSettings(
        trigger_sources=[trigger_source],
        external_trigger_mode=ExternalTriggerMode.SPC_TM_POS,
        external_trigger_level_in_mv=1000,
    )

    # Acquisition settings
    acquisition_settings = AcquisitionSettings(
        acquisition_mode=AcquisitionMode.SPC_REC_STD_SINGLE,
        sample_rate_in_hz=40000000,
        acquisition_length_in_samples=400,
        pre_trigger_length_in_samples=0,
        timeout_in_ms=1000,
        enabled_channels=[0],
        vertical_ranges_in_mv=[200],
        vertical_offsets_in_percent=[0],
    )

    # Apply settings
    card.configure_trigger(trigger_settings)
    card.configure_acquisition(acquisition_settings)

    # Execute acquisition
    waveform_list = card.execute_standard_single_acquisition()
    card.reset()
    card.disconnect()
    return waveform_list


if __name__ == "__main__":

    from matplotlib.pyplot import plot, show, xlabel, tight_layout, ylabel

    waveforms = standard_single_mode_example(
        mock_mode=True, trigger_source=TriggerSource.SPC_TMASK_EXT0, device_number=0
    )

    # Plot waveforms
    for waveform in waveforms:
        plot(waveform.samples)
        xlabel("Time (samples)")
        ylabel("Amplitude (Volts)")
        tight_layout()

    print(f"Acquired {len(waveforms)} waveforms with the following shapes:")
    print([wfm.samples.shape for wfm in waveforms])
    print("and the following timestamps:")
    print([wfm.timestamp for wfm in waveforms])

    show()

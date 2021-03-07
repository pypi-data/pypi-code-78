"""
    Augmenter that apply vocal tract length perturbation (VTLP) operation to audio.
"""

from nlpaug.augmenter.audio import AudioAugmenter
import nlpaug.model.audio as nma
from nlpaug.util import Action


class VtlpAug(AudioAugmenter):
    # https://pdfs.semanticscholar.org/3de0/616eb3cd4554fdf9fd65c9c82f2605a17413.pdf
    """
    :param tuple zone: Assign a zone for augmentation. Default value is (0.2, 0.8) which means that no any
        augmentation will be applied in first 20% and last 20% of whole audio.
    :param float coverage: Portion of augmentation. Value should be between 0 and 1. If `1` is assigned, augment
        operation will be applied to target audio segment. For example, the audio duration is 60 seconds while
        zone and coverage are (0.2, 0.8) and 0.7 respectively. 42 seconds ((0.8-0.2)*0.7*60) audio will be
        augmented.
    :param tuple factor: Input data vocal will be increased (decreased). Augmented value will be picked
        within the range of this tuple value. Vocal will be reduced if value is between 0 and 1.
    :param int fhi: Boundary frequency. Default value is 4800.
    :param str name: Name of this augmenter

    >>> import nlpaug.augmenter.audio as naa
    >>> aug = naa.VtlpAug()
    """

    def __init__(self, sampling_rate, zone=(0.2, 0.8), coverage=0.1, fhi=4800, factor=(0.9, 1.1), 
        name='Vtlp_Aug', verbose=0, stateless=True):
        super().__init__(
            action=Action.SUBSTITUTE, zone=zone, coverage=coverage, factor=factor, name=name, 
            device='cpu', verbose=verbose, stateless=stateless)

        self.sampling_rate = sampling_rate
        self.fhi = fhi
        self.model = nma.Vtlp()

    def substitute(self, data):
        if self.duration is None:
            start_pos, end_pos = self.get_augment_range_by_coverage(data)
        else:
            start_pos, end_pos = self.get_augment_range_by_duration(data)

        warp_factor = self.get_random_factor()

        if not self.stateless:
            self.start_pos, self.end_pos, self.aug_factor = start_pos, end_pos, warp_factor

        return self.model.manipulate(data, start_pos=start_pos, end_pos=end_pos, sampling_rate=self.sampling_rate,
            warp_factor=warp_factor)

from unittest import TestCase

from castervoice.lib import settings


class SettingsEnabledTestCase(TestCase):
    def _set_setting(self, key_path, value):
        if settings.SETTINGS is None:
            settings.SETTINGS = {}
        s = settings.SETTINGS
        len_kp = len(key_path)
        for i in range(0, len_kp):
            kp = key_path[i]
            if i == len_kp - 1:
                s[kp] = value
            else:
                s[kp] = {}
                s = s[kp]
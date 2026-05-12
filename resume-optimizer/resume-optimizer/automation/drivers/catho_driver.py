from __future__ import annotations

from automation.drivers.base_driver import BaseDriver


class CathoDriver(BaseDriver):
    platform_name = 'catho'

    def apply_profile(self, profile_data: dict) -> dict:
        fields = ['full_name', 'email', 'phone', 'summary']
        if self.dry_run:
            return self._dry_run_response(profile_data, fields)
        return {
            'platform': self.platform_name,
            'mode': 'manual_assist',
            'message': 'Integração real não incluída neste MVP. Use o preenchimento assistido.',
        }

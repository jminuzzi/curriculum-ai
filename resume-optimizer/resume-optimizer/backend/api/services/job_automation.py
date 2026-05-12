from __future__ import annotations

from automation.drivers.catho_driver import CathoDriver
from automation.drivers.gupy_driver import GupyDriver
from automation.drivers.linkedin_driver import LinkedInDriver


class JobAutomationService:
    DRIVERS = {
        'gupy': GupyDriver,
        'catho': CathoDriver,
        'linkedin': LinkedInDriver,
    }

    @classmethod
    def run(cls, platform: str, profile_data: dict, dry_run: bool = True) -> dict:
        platform_key = platform.lower().strip()
        driver_cls = cls.DRIVERS.get(platform_key)
        if not driver_cls:
            raise ValueError(f'Plataforma não suportada: {platform}')

        driver = driver_cls(dry_run=dry_run)
        result = driver.apply_profile(profile_data)
        return result

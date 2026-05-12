from __future__ import annotations

from abc import ABC, abstractmethod


class BaseDriver(ABC):
    platform_name: str = 'base'

    def __init__(self, dry_run: bool = True) -> None:
        self.dry_run = dry_run

    @abstractmethod
    def apply_profile(self, profile_data: dict) -> dict:
        raise NotImplementedError

    def _dry_run_response(self, profile_data: dict, fields: list[str]) -> dict:
        return {
            'platform': self.platform_name,
            'mode': 'dry_run',
            'message': (
                'Modo seguro: os dados foram organizados para preenchimento assistido. '
                'Login, captcha e envio final continuam manuais.'
            ),
            'fields_to_fill': {field: profile_data.get(field) for field in fields},
        }

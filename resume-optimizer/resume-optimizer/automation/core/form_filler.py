from __future__ import annotations


def map_profile_to_form(profile_data: dict) -> dict:
    return {
        'name': profile_data.get('full_name', ''),
        'email': profile_data.get('email', ''),
        'phone': profile_data.get('phone', ''),
        'summary': profile_data.get('summary', ''),
    }

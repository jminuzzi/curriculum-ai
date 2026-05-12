from __future__ import annotations

from contextlib import contextmanager


@contextmanager
def browser_session() -> dict:
    session = {'status': 'ready', 'headless': False}
    try:
        yield session
    finally:
        session['status'] = 'closed'

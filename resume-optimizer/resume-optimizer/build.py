from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run() -> None:
    cmd = [
        sys.executable,
        '-m',
        'PyInstaller',
        '--onefile',
        '--name',
        'ResumeOptimizer',
        str(ROOT / 'frontend' / 'app.py'),
    ]
    subprocess.run(cmd, check=True)


if __name__ == '__main__':
    run()

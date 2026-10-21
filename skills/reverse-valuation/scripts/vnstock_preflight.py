"""Metadata-only preflight; do not import quarantined packages."""
import importlib.metadata
import json
import platform
import sys
from datetime import datetime, timezone

def main():
    try:
        version = importlib.metadata.version('vnstock')
    except importlib.metadata.PackageNotFoundError:
        version = None
    print(json.dumps({'status': 'UNAVAILABLE',
        'reason': 'ADAPTER_NOT_RESTORED_AND_PYPI_QUARANTINE',
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'python': sys.executable, 'python_version': platform.python_version(),
        'platform': platform.system(), 'installed_version': version,
        'import_attempted': False, 'network_attempted': False,
        'fallback': 'official_disclosures_or_user_data'}, ensure_ascii=False))

if __name__ == '__main__':
    main()

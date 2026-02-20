import sys
import os
from pathlib import Path

# Add project root to Python path so 'myproject.settings' is importable
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel needs the handler as 'app'
app = application

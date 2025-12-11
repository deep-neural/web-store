#!/usr/bin/env python3
"""
Open Addons API Server - Production Mode
Serves static files from /home/ubuntu/webstore/frontend/dist using Django
"""

import os
import sys
from pathlib import Path

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_settings')

import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.urls import path, re_path
from django.views.static import serve
from django.http import HttpResponse, FileResponse, Http404

# Hardcoded absolute path to frontend/dist - NO PATH TRAVERSAL ALLOWED
FRONTEND_DIST = Path('/home/ubuntu/webstore/frontend/dist').resolve()

# Configure Django settings
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY='production-secret-key-change-in-production',
        ALLOWED_HOSTS=['*'],
        ROOT_URLCONF=__name__,
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.middleware.common.CommonMiddleware',
        ],
        STATIC_URL='/static/',
        STATIC_ROOT=str(FRONTEND_DIST),
    )
    django.setup()


def index_view(request):
    """Serve index.html for all routes (SPA support)"""
    index_path = FRONTEND_DIST / 'index.html'
    if index_path.exists():
        return FileResponse(open(index_path, 'rb'), content_type='text/html')
    return HttpResponse("Frontend dist not found. Run 'npm run build' in frontend directory.", status=404)


def format_filepath(path):
    """
    Validate and format a file path with strict security controls.
    
    Args:
        path: The requested file path (e.g., 'images/logo.png' or 'main.bundle.js')
    
    Returns:
        tuple: (full_path, mime_type) if valid, (None, None) if invalid
    """
    import re
    
    # Hardcoded whitelist of allowed filenames with dots (bundles, etc.)
    # Format: 'filename.ext': ('filename.ext', 'mime/type')
    ALLOWED_FILES = {
        # JavaScript bundles
        'main.bundle.js': ('main.bundle.js', 'application/javascript'),
    }
    
    # Allowed extensions for UUID-style files (no dots in basename)
    # Format: 'ext': ('.ext', 'mime/type')
    ALLOWED_EXTENSIONS = {
        'png': ('.png', 'image/png'),
        'jpg': ('.jpg', 'image/jpeg'),
        'jpeg': ('.jpeg', 'image/jpeg'),
        'gif': ('.gif', 'image/gif'),
        'svg': ('.svg', 'image/svg+xml'),
        'webp': ('.webp', 'image/webp'),
        'ico': ('.ico', 'image/x-icon'),
    }
    
    # Allowed subdirectories - hardcoded for security and speed
    ALLOWED_SUBDIRS = {
        'images': 'images',
        'js': 'js',
        'css': 'css',
        'assets': 'assets',
        'fonts': 'fonts',
    }
    
    # Extract parent directory and filename from path
    path_parts = path.split('/')
    
    # Determine subdirectory (if any)
    subdir = None
    if len(path_parts) > 1:
        # Get the first part as potential subdirectory
        potential_subdir = path_parts[0].lower()
        if potential_subdir in ALLOWED_SUBDIRS:
            subdir = ALLOWED_SUBDIRS[potential_subdir]
    
    # Extract the original filename from the path (last part only)
    original_filename = os.path.basename(path)
    
    # First, check if it's a hardcoded filename (like main.bundle.js)
    if original_filename in ALLOWED_FILES:
        safe_filename, mime_type = ALLOWED_FILES[original_filename]
        
        # Build the full path
        if subdir:
            file_path = FRONTEND_DIST / subdir / safe_filename
        else:
            file_path = FRONTEND_DIST / safe_filename
        
        if file_path.exists() and file_path.is_file():
            return (file_path, mime_type)
    
    # Otherwise, try UUID-style matching (no dots allowed in basename)
    name_parts = original_filename.rsplit('.', 1)
    if len(name_parts) == 2:
        basename_without_ext, ext = name_parts
        ext_lower = ext.lower()
        
        # Check if extension is allowed
        if ext_lower in ALLOWED_EXTENSIONS:
            # Remove any special characters from basename (keep only alphanumeric, dash, underscore)
            # NO DOTS ALLOWED
            sanitized_basename = re.sub(r'[^a-zA-Z0-9_-]', '', basename_without_ext)
            
            if sanitized_basename:
                # Get canonical extension and MIME type
                canonical_ext, mime_type = ALLOWED_EXTENSIONS[ext_lower]
                
                # Reconstruct safe filename
                safe_filename = sanitized_basename + canonical_ext
                
                # Build the full path
                if subdir:
                    file_path = FRONTEND_DIST / subdir / safe_filename
                else:
                    file_path = FRONTEND_DIST / safe_filename
                
                if file_path.exists() and file_path.is_file():
                    return (file_path, mime_type)
    
    # If file doesn't exist or doesn't match any pattern, return None
    return (None, None)


def static_file(request, path):
    """static files from dist directory with strict filename validation"""
    file_path, mime_type = format_filepath(path)
    
    if file_path and mime_type:
        return FileResponse(open(file_path, 'rb'), content_type=mime_type)
    
    # If file doesn't exist or doesn't match any pattern, fall back to index.html for SPA routing
    return index_view(request)


# URL patterns
urlpatterns = [
    # Serve static files (assets, js, css, etc.)
    re_path(r'^(?P<path>.+\..+)$', static_file),
    # All other routes serve index.html (SPA support)
    re_path(r'^.*$', index_view),
]

# WSGI application
application = get_wsgi_application()


def main():
    """Run the production server with SSL using Gunicorn"""
    
    print("=" * 60)
    print("Open Addons - Production Server (Django with SSL)")
    print("=" * 60)
    print(f"Serving static files from: {FRONTEND_DIST}")
    print("=" * 60)
    
    if not FRONTEND_DIST.exists():
        print("WARNING: Frontend dist directory not found!")
        print(f"Expected location: {FRONTEND_DIST}")
        print("Run 'npm run build' in the frontend directory first.")
        print("=" * 60)
        sys.exit(1)
    
    # SSL certificate paths
    ssl_keyfile = "/etc/letsencrypt/live/webstore.fluxapp.co/privkey.pem"
    ssl_certfile = "/etc/letsencrypt/live/webstore.fluxapp.co/fullchain.pem"
    
    print(f"Starting HTTPS server on 0.0.0.0:443")
    print(f"SSL Certificate: {ssl_certfile}")
    print(f"SSL Key: {ssl_keyfile}")
    print("=" * 60)
    print("Using Gunicorn WSGI server")
    print("Install with: pip install gunicorn")
    print("=" * 60)
    
    # Run using Gunicorn - the proper way for production Django
    # This is much better than execute_from_command_line
    from gunicorn.app.base import BaseApplication
    
    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()
        
        def load_config(self):
            for key, value in self.options.items():
                if key in self.cfg.settings and value is not None:
                    self.cfg.set(key.lower(), value)
        
        def load(self):
            return self.application
    
    options = {
        'bind': '0.0.0.0:443',
        'workers': 4,
        'worker_class': 'sync',
        'certfile': ssl_certfile,
        'keyfile': ssl_keyfile,
        'accesslog': '-',
        'errorlog': '-',
        'loglevel': 'info',
    }
    
    StandaloneApplication(application, options).run()


if __name__ == '__main__':
    main()
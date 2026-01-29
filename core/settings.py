INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',      # For the API
    'corsheaders',         # For Cross-Origin communication
    'api',                 # Your app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # MUST be at the top
    'django.middleware.common.CommonMiddleware',
    # ... other middlewares ...
]

CORS_ALLOW_ALL_ORIGINS = True # Necessary for testing locally

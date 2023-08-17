from .default import *

# Enable Log query count
# MIDDLEWARE = MIDDLEWARE + ['base.middleware.QueryCountDebugMiddleware',]

APP_MOD = APP_MOD_FULL

ALLOWED_HOSTS = ["localhost", "127.0.0.1",]

ENVIRONMENT_NAME = 'develop'

try:
    from .local_settings import *
except:
    print('Develop local setting not found')
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILE_DIRS = (
	os.path.join(PROJECT_ROOT, 'static'),
)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'whispering-retreat-50919']
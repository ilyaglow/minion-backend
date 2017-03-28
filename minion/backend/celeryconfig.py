from minion.backend.utils import backend_config

cfg = backend_config()

CELERY_ACCEPT_CONTENT = ["json", "pickle"]
CELERY_MONGODB_SCHEDULER_DB = "minion"
CELERY_MONGODB_SCHEDULER_COLLECTION = "scanschedule"
CELERY_MONGODB_SCHEDULER_URL = "mongodb://{}:{}".format(cfg['mongodb']['host'],
                                                        cfg['mongodb']['port'])

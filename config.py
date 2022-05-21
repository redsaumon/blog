from datetime import timedelta

DB_HOST           = "localhost"
DB_PORT           = 3306
DB_NAME           = "board"
DB_USER           = "root"
DB_PASSWORD       = "0830"
DB_CONNECTION_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

SECRET_KEY = 'django-insecure-0gmkn4j&pr&5^7ls$v#l!cvu2m&ps=g6^^u$qb%1#g1_$&2z+v'
PAGE_SIZE = 3
ALGORITHM = 'HS256'
ACCESS_TOKEN_LIFETIME = timedelta(days=15)
REFRESH_TOKEN_LIFETIME = timedelta(days=7)
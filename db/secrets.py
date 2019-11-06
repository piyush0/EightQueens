# These are the default variables to connect to the DB. We can change these in docker-compose.yml
# by providing an environment tag to postgres image.

DB_USER = 'postgres'
DB_PASS = ''  # Should ideally be encrypted or not put in version control
DB_HOST = 'db'
DB_NAME = 'postgres'

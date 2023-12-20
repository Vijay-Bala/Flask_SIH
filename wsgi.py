# import sys
# import logging
# sys.path.insert(0, '/var/www/html/server')
# logging.basicConfig(stream=sys.stderr)
# from server import app as application
# application.secret_key = 'qwertyuiop'
from server import app
if __name__=="__main__":
    app.run()

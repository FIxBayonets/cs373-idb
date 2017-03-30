# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://swegot:gameofthrones@swegot.c427phsrxocc.us-west-2.rds.amazonaws.com:3306/swegot'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

#SQLALCHEMY_POOL_RECYCLE = 3600

#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'

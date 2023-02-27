import json
import os
from alembic import op

def bulk_upload(table_name):
    with open(os.path.join(os.path.dirname(__file__), "../bulkDataUpload/users.json")) as f:
        user_data = f.read()

    op.bulk_insert(table_name, json.loads(user_data)) # inserting data in bulk to users table
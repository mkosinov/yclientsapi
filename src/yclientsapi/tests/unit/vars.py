import os

from dotenv import load_dotenv

load_dotenv()


company_id = os.getenv("YCLIENTS_COMPANY_ID")
partner_token = os.getenv("YCLIENTS_PARTNER_TOKEN")
user_login = os.getenv("YCLIENTS_USER_LOGIN")
user_password = os.getenv("YCLIENTS_USER_PASSWORD")
user_token = os.getenv("YCLIENTS_USER_TOKEN")

activity_id = os.getenv("YCLIENTS_ACTIVITY_ID")
staff_id = os.getenv("YCLIENTS_STAFF_ID")
service_id = os.getenv("YCLIENTS_SERVICE_ID")
service_category_id = os.getenv("YCLIENTS_SERVICE_CATEGORY_ID")

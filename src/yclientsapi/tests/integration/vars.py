import os

from dotenv import load_dotenv

load_dotenv()


partner_token = os.getenv("YCLIENTS_PARTNER_TOKEN")
user_login = os.getenv("YCLIENTS_USER_LOGIN")
user_password = os.getenv("YCLIENTS_USER_PASSWORD")
user_token = os.getenv("YCLIENTS_USER_TOKEN")

company_id = os.getenv("YCLIENTS_COMPANY_ID")
staff_id = os.getenv("YCLIENTS_STAFF_ID")
service_id = os.getenv("YCLIENTS_SERVICE_ID")
service_category_id = os.getenv("YCLIENTS_SERVICE_CATEGORY_ID")
resource_id = os.getenv("YCLIENTS_RESOURCE_ID")
calculation_id = os.getenv("YCLIENTS_CALCULATION_ID")

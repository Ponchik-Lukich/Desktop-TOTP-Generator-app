from dotenv import load_dotenv
import os


load_dotenv()

service_id = os.environ['SERVICE_ID']
secret_key = os.environ['SECRET_KEY_FOR_ENCRYPTION']
pos1 = os.environ['SECRET_KEY_POSITION']
pos2 = os.environ['PASSWORD_POSITION']
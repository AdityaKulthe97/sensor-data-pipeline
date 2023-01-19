
import os


SECURITY_PROTOCOL = "SASL_SSL"
SSL_MACHENISM = "PLAIN"
API_KEY = "6OFS7S5P2YKAB7OK"
API_SECRET_KEY = "IZDitcFXLTU+S+lTjbYAIcTEF/KrpH9sm6sHvgg9Lz19zdvTckGddiFWYqX1k5aE"
BOOTSTRAP_SERVER = "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092"
ENDPOINT_SCHEMA_URL  = "https://psrc-10wgj.ap-southeast-2.aws.confluent.cloud"
SCHEMA_REGISTRY_API_KEY = "UBEP7SRATFVI4KWQ"
SCHEMA_REGISTRY_API_SECRET = "UBNEvNhzbCjW46SqDH/yCmuN5Ju+22Ar5V0GM6Ff20xvxt0hwnFmPx0h2IXbZuNC"


# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
# API_KEY = os.getenv('API_KEY',None)
# API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
# BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
# ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
# SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
# SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()


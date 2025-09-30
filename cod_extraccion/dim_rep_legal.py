# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")


query = """
SELECT DISTINCT identificaci_n_representante_legal, nombre_representante_legal,tipo_de_identificaci_n_representante_legal, g_nero_representante_legal, nacionalidad_representante_legal, domicilio_representante_legal
"""

results = client.get("jbjy-vk9h", query=query)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

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
SELECT DISTINCT id_contrato,descripcion_del_proceso,estado_contrato,el_contrato_puede_ser_prorrogado,duraci_n_del_contrato,dias_adicionados,fecha_inicio_liquidacion,fecha_fin_liquidacion
"""

results = client.get("jbjy-vk9h", query=query)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

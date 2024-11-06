from datetime import datetime
import pandas as pd

fecha = datetime.now()

fecha = str(datetime.now())[:19]

print(pd.DataFrame({"fecha": [fecha]}))


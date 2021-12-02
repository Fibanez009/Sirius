try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass

# Carga de librerias
import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import time
# from datetime import datetime, timedelta
# from datetime import datetime, date
# import re
import scipy.stats as stats

print("Version: ", pd .__version__)
print("Version: ", sns .__version__)
# tf.keras.__version__
plt.style.use('ggplot')
plt.close('all')

import tensorflow as tf

# Versiones
print("Version: ", tf.__version__)
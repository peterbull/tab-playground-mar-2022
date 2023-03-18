# AUTOGENERATED! DO NOT EDIT! File to edit: ../traffic-flow.ipynb.

# %% auto 0
__all__ = ['comp', 'path', 'train_df', 'test_df', 'sample_df', 'comb_df']

# %% ../traffic-flow.ipynb 3
from fastai.tabular.all import *

from sklearn.ensemble import RandomForestRegressor

# %% ../traffic-flow.ipynb 4
try: import fastkaggle
except ModuleNotFoundError:
    !pip install -Uq fastkaggle

from fastkaggle import *

# %% ../traffic-flow.ipynb 5
comp = 'tabular-playground-series-mar-2022'
path = setup_comp(comp, install='fastai')

# %% ../traffic-flow.ipynb 7
train_df = pd.read_csv(path/"train.csv")
test_df = pd.read_csv(path/"test.csv")
sample_df = pd.read_csv(path/"sample_submission.csv")

# %% ../traffic-flow.ipynb 9
comb_df = pd.concat([train_df, test_df])

# %% ../traffic-flow.ipynb 11
comb_df['date'] = pd.to_datetime(comb_df.time)

# %% ../traffic-flow.ipynb 12
comb_df['time_of_day'] = comb_df.date.dt.time
comb_df['date'] = comb_df.date.dt.date

# %% ../traffic-flow.ipynb 13
comb_df['time_of_day'] = pd.to_timedelta(comb_df.time_of_day.astype(str))
comb_df['date'] = pd.to_datetime(comb_df.date)


from os import walk
import pandas as pd
DATAPATH = "data/"

def data_preprocessing():
    # find all files
    files = []
    for (_, _, filenames) in walk(DATAPATH):
        files.extend(filenames)
        break

    # iterate through files and count workers
    df_all_data = None
    for file in files:
        xl = pd.ExcelFile(DATAPATH+file)
        df_file = pd.DataFrame()
        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name)
            dfc = (df
            .groupby("Подразделение")
            .count()
            .drop(["Компания", "Фио"], axis=1)
            .T
            .reset_index()
            .rename(columns={"index":"date"})
            )
            # concatenate all month together
            df_file = pd.concat([df_file, dfc])
        # column with unit name and change column names
        df_file.reset_index(inplace=True, drop=True)
        unit_name = df_file.columns[-1]
        df_file['name'] = pd.Series([unit_name] * len(df_file), index=df_file.index)
        df_file = df_file.rename(columns={unit_name: 'workers'})
        # concatenate all units
        if df_all_data is None:
            df_all_data = df_file.copy(deep=True)
        else:
            df_all_data = pd.concat([df_all_data, df_file])
            df_all_data.reset_index(inplace=True, drop=True)
    # save to csv
    df_all_data.to_csv("preprocessed_data/all.csv")
    
def function_test():
    r"""Fills the input `Tensor` with values according to the method
    described in `Understanding the difficulty of training deep feedforward
    neural networks` - Glorot, X. & Bengio, Y. (2010), using a uniform
    distribution. The resulting tensor will have values sampled from
    :math:`\mathcal{U}(-a, a)` where

    .. math::
        a = \text{gain} \times \sqrt{\frac{6}{\text{fan\_in} + \text{fan\_out}}}

    Also known as Glorot initialization.

    Args:
        tensor: an n-dimensional `torch.Tensor`
        gain: an optional scaling factor

    Examples:
        >>> w = torch.empty(3, 5)
        >>> nn.init.xavier_uniform_(w, gain=nn.init.calculate_gain('relu'))
    """
    pass

if __name__=="__main__":
    data_preprocessing()
    function_test()
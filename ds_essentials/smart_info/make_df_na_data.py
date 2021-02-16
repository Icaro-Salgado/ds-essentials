import pandas as pd


def make_df_na_data(df, name):
    """
    Create the DataFrame for smart info
    
    ...
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to display the informations
    
    name : str or int
        name or position of the DataFrame.
    
    Returns
    -------
    pandas.DataFrame
        DataFrame with requested info
    """
    
    df_na_data = df.isnull().sum() / df.shape[0] * 100
        
    df_na_data = pd.DataFrame({(name, "missing_ratio"): df_na_data})
    
    return df_na_data
from .make_df_na_data import make_df_na_data

import pandas as pd

def smart_info(
    data, 
    join_axis=1, 
    sort_method=0, 
    sort_key=None
):
    
    
    """
    Create a DataFrame that contains info about the passed DataFrame
    
    ...
    
    Parameters
    ----------
    data : dict or list or pandas.DataFrame
         dict with DataFrame name as key and DataFrame as value 
         or a single DataFrame
    
    join_axis : {0 or "index", 1 or "columns"}, default 1
        axis to join the output
    
    sort_method : {0 or "no_sort", 1 or "descending", 2 or "ascending"}, default=1
        method to sort the final DataFrame
        
    sort_key : {None, str}, default=None
        DataFrame in which to sort the entire return DataFrame, 
        if sort_key is None and sort method is not 0, it will sort by the first 
        DataFrame of  the passed data,
        else if not None and sort method is 0, it will have no effect
    
    
    Returns
    -------
    pandas.DataFrame
        DataFrame with requested info
    """
    
    
    # Default configs
    df_na_data = pd.DataFrame({})
    
    sort = False if sort_method == 0 or sort_method == 'no_sort' else True
    
    
    # Making return DataFrame
    if str(type(data)) == "<class 'dict'>":
        
        for name, df in reversed(data.items()):
                na_data = make_df_na_data(df, name)
                
                df_na_data = pd.concat([na_data, df_na_data], axis=join_axis)
                
    elif str(type(data)) == "<class 'list'>":
        print('É uma lista')
    
    
    elif str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
        print('É unico')
    
    
    if sort:
        
        sort_key = df_na_data.columns[0][0] if not sort_key else sort_key
        sort_ascending = True if sort_method == (2 or "ascending") else False
        
        
        df_na_data.sort_values(
            by=(f'{sort_key}', 'missing_ratio'), 
            ascending=sort_ascending, 
            inplace=True)
    
    
    return df_na_data
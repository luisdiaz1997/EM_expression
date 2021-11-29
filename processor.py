def get_attributes(df, prefix):
    df['Parent'] = df.attributes.str.split(';').str[1].str.split('=').str[1]
    df[prefix+'ID'] = df.attributes.str.split(';').str[0].str.split('=').str[1]
    return df
    
def get_feature(df, feature):
    new_df = df[df.feature == feature].copy().reset_index(drop=True)
    new_df = get_attributes(new_df, prefix=feature[0])
    return new_df
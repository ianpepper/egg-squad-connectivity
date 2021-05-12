import pandas as pd

#urls https://wiki.cybera.ca/display/shareit/45613613/QAO9bc379dd5a4a49eea9a9e3d1d81be04bOFU
cira_url = 'https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/RMA-CIRA-Data-DSFA2020/RMADataForHackathon21-04-23.csv'

mlab = []
mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2020-07-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2020-08-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2020-09-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2020-10-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2020-11-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2020-12-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2021-01-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2021-02-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2021-03-01_Mlab_data_start.csv')

mlab.append('https://swift-yyc.cloud.cybera.ca:8080/v1/AUTH_233e84cd313945c992b4b585f7b9125d/MLabDat/2021-04-01_Mlab_data_start.csv')


def internetdata():
    """fuction to generate data for contest

    retuns:
        df_cira: pd of cira data provided
        df_mlab: pd of mlab data provided
        df_ookla: pd of ookla data and shape file
    """
    df_cira = pd.read_csv(cira_url)

    df_mlab = pd.concat([pd.read_csv(x) for x in mlab])

    df_ookla = 'TODO Placehoolder' # placeholder

    return(df_cira,df_mlab,df_ookla)



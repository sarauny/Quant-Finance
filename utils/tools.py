import pandas_datareader.data as web

# Retrieving ticker's data
def data_reader(ticker, start, end):  
    try:
        print('Retriving data for', ticker, 'from iex')
        data = web.DataReader(ticker, 'iex', start, end)
    except:
        print('iex failed, trying Google Finance...')
        try:
            data = web.DataReader(ticker, 'google', start, end)
        except:
            print('Google Finance failed, trying moningstar...')
            try:
                data = web.DataReader(ticker, 'morningstar', start, end)
            except:
                print('iex failed, trying quandl...')
                try:
                    data = web.DataReader(ticker, 'quandl', start, end)
                except:
                    print('iex quandl, trying fred...')
                    try:
                        data = web.DataReader(ticker, 'fred', start, end)
                    except:
                        print('fred quandl, trying MOEX...')
                        try:
                            data = web.DataReader(ticker, 'MOEX', start, end)
                        except:
                            print('all database failed.')
                            pass
    return data

# reference: https://pydata.github.io/pandas-datareader/stable/remote_data.html#google-finance
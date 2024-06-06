import os
import requests
import zipfile
import io

def get_meteo_idaweb():
    """
    Download the Meteo IDAWEB datasets from the web.
    """
    if (not os.path.exists('meteo_idaweb.csv') or
            not os.path.exists('meteo_idaweb_train.csv') or
            not os.path.exists('meteo_idaweb_test.csv')):
        url = ('https://www.dropbox.com/scl/fi/7se6kpjvn78kln8vped8l/meteo_idaweb.zip?rlkey=q7ldrk529k08c47gzl0r4je2t'
               '&dl=1')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall()
            print('Meteo IDAWEB datasets downloaded.')
        else:
            print(f'Failed to download data: {r.status_code}')
    else:
        print('Meteo IDAWEB datasets already exist.')

# Call the function to download the data
get_meteo_idaweb()

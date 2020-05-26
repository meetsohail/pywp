import requests
import os
import sys
import random


def main():
    if os.access(os.getcwd(), os.W_OK):
        pass
    else:
        sys.exit('Your current path have no write permission!')

    if os.path.exists('wp-content') or os.path.exists('wp-config.php'):

        file_check = input(
            'WordPress setup already exists, Do you want to overwrite? (Y or N) ')

        if file_check == 'Y' or file_check == 'y':
            try:
                os.rmdir('wp-content')
                os.remove('wp-config.php')
            except OSError as e:
                sys.exit('Error: {}'.format(e.strerror))
        else:
            sys.exit('Remove existing wordpress setup or overwrite before proceed!')

    try:
        print('Started Downloading WordPress..')
        wordpress = requests.get('https://wordpress.org/latest.zip')
    except ConnectionError as e:
        sys.exit('Error {}'.format(e))

    file_name = ''.join(
        str('wordpress-'+str(random.getrandbits(30)))+str('.zip'))

    with open(file_name, 'wb') as f:
        f.write(wordpress.content)

    sys.exit('Successfull installed website, Now visit your URL.')
    # unzip('wordpress.zip')`

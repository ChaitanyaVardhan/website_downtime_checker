#utils.py

import time
import logging
import requests

class WebsiteDownException(Exception):
    pass

def ping_website(address, timeout=20):
    """
    check if a website is down. Status code>=400
    implies website down. Throw WebsiteDownException
    error when website down
    """
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning('website {} returned status code {}'.format(address, 
                                                                        response.status_code))
            raise WebsiteDownException
    except requests.exceptions.RequestException:
        logging.warning('Timing expired for website {}'.format(address))

def notify_owner(address):
    """
    send the owner of the address notification
    that website is down
    """
    logging.info('Notifying the owner of the website {}'.format(address))

def check_website(address):
    """Check if website is down, notify user"""
    try:
        ping_website(address)
    except WebsiteDownException:
        notify_owner(address)




        
                

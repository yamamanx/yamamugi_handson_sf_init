import logging
import traceback
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO')

logger = logging.getLogger()

if log_level == 'ERROR':
    logger.setLevel(logging.ERROR)
elif log_level == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    try:
        logger.debug(event)

        phone_number = event.get('phone_number', '')
        logger.debug(phone_number)

        if phone_number:
            icon = ':telephone_receiver:'
        else:
            icon = ':iphone:'
        logger.debug(icon)

        to_slack_first = {
            'icon': icon
        }
        output = {
            'to_kintone': event,
            'to_slack_first': to_slack_first
        }
        logger.debug(output)

        return output

    except Exception as e:
        logger.error(traceback.format_exc())
        raise(traceback.format_exc())

import logging
import traceback


def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        phone_number = event.get('phone_number', '')

        if phone_number:
            icon = ':telephone_receiver:'
        else:
            icon = ':iphone:'

        to_slack_first = {
            'icon': icon
        }
        output = {
            'to_kintone': event,
            'to_slack_first': to_slack_first
        }
        return output


    except Exception as e:
        logger.error(traceback.format_exc())
        raise(traceback.format_exc())

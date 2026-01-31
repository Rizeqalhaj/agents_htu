from twilio.rest import Client
from django.conf import settings


def send_whatsapp_message(message: str, media_url: str = None) -> dict:
    """
    Send a WhatsApp message using Twilio.

    Args:
        message: The text message to send
        media_url: Optional URL of an image to send

    Returns:
        dict with status and message sid
    """
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    from_number = f"whatsapp:{settings.TWILIO_AUTH_NUMBER}"
    to_number = f"whatsapp:{settings.TWILIO_WHATSAPP_TO}"

    try:
        if media_url:
            msg = client.messages.create(
                body=message,
                from_=from_number,
                to=to_number,
                media_url=[media_url]
            )
        else:
            msg = client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )

        return {
            "success": True,
            "sid": msg.sid,
            "status": msg.status
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

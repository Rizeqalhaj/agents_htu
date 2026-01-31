import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.crews.image_generation.crew import ImageGenerationCrew
from core.crews.text_generation.crew import TextGenerationCrew
from core.tools.whatsapp_sender import send_whatsapp_message


def run_image_generation(prompt: str):
    """Run image generation"""
    crew = ImageGenerationCrew()
    result = crew.crew().kickoff(inputs={"user_prompt": prompt})
    return result


def run_text_generation(query: str):
    """Run text generation"""
    crew = TextGenerationCrew()
    result = crew.crew().kickoff(inputs={"user_query": query})
    return result


def main():
    print("\n" + "=" * 60)
    print("WHAT DO YOU WANT TO SEND TO WHATSAPP?")
    print("1. Generate and send TEXT")
    print("2. Generate and send IMAGE")
    print("=" * 60)

    mode = input("Enter choice (1/2): ").strip()

    if mode == "1":
        query = input("\nWhat should the text be about? ")
        print("\nGenerating text...")

        result = run_text_generation(query)

        print("\n" + "=" * 60)
        print("GENERATED TEXT:")
        print("=" * 60)
        print(result.raw)

        # Extract text from result
        try:
            result_json = json.loads(result.raw)
            blogs = result_json.get("blogs", [])
            if blogs:
                message = blogs[0].get("content_of_blog", result.raw)
            else:
                message = result.raw
        except json.JSONDecodeError:
            message = result.raw

        # Send to WhatsApp
        print("\nSending to WhatsApp...")
        wa_result = send_whatsapp_message(message)

        if wa_result["success"]:
            print("Message sent to WhatsApp successfully!")
        else:
            print(f"Failed to send: {wa_result['error']}")

    elif mode == "2":
        prompt = input("\nDescribe the image you want: ")
        print("\nGenerating image...")

        result = run_image_generation(prompt)

        print("\n" + "=" * 60)
        print("GENERATED IMAGE:")
        print("=" * 60)
        print(result.raw)

        # Extract image URL from result
        try:
            result_json = json.loads(result.raw)
            image_url = result_json.get("image_url", "")
            caption = result_json.get("enhanced_prompt", prompt)
        except json.JSONDecodeError:
            image_url = result.raw.strip()
            caption = prompt

        if image_url:
            # Send to WhatsApp
            print("\nSending image to WhatsApp...")
            wa_result = send_whatsapp_message(
                message=caption,
                media_url=image_url
            )

            if wa_result["success"]:
                print("Image sent to WhatsApp successfully!")
            else:
                print(f"Failed to send: {wa_result['error']}")
        else:
            print("No image URL found.")

    else:
        print("Invalid choice.")

    print("=" * 60)


if __name__ == "__main__":
    main()

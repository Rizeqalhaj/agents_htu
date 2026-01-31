import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.crews.text_generation.crew import TextGenerationCrew


def run_text_generation(query: str):
    """Run the text generation agent"""
    crew = TextGenerationCrew()
    result = crew.crew().kickoff(inputs={
        'user_query': query
    })
    return result


def run_image_generation(prompt: str):
    """Run the image generation agent"""
    crew = TextGenerationCrew()
    result = crew.crew().kickoff(inputs={
        'user_prompt': prompt
    })
    return result


if __name__ == "__main__":
    # Example: Text Generation
    # result = run_text_generation("Write about the benefits of AI in education")

    # Example: Image Generation
    result = run_image_generation("A futuristic city at sunset with flying cars")

    print(result)

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import urllib.parse


class ImageGeneratorInput(BaseModel):
    prompt: str = Field(..., description="The prompt describing the image to generate")


class ImageGeneratorTool(BaseTool):
    name: str = "Image Generator"
    description: str = (
        "Generates an image based on a text prompt using Pollinations.ai (free). "
        "Input should be a detailed description of the image you want to create."
    )
    args_schema: Type[BaseModel] = ImageGeneratorInput

    def _run(self, prompt: str) -> str:
        encoded_prompt = urllib.parse.quote(prompt)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
        return image_url

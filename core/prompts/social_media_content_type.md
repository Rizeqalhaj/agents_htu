"""
user input = {{user_query}}
Extract the social media platform(s) from the user prompt.
If no platform is specified, use 'Facebook' as default platform.

Determine the content type based on the user prompt:
- If the user explicitly requests to generate/create an image, assign 'image' to content_type.
- If the user requests a text post, blog, or written content, assign 'text_only' to content_type.
- Default to 'text_only' if unclear.

The JSON object output must be in the following format (please don't write json in the response):
{
    "social_media_platform": "",
    "content_type": ""
}
"""
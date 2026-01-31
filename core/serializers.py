from rest_framework import serializers


class TextGenerationSerializer(serializers.Serializer):
    query = serializers.CharField(required=True, help_text="The text generation query")


class ImageGenerationSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True, help_text="The image generation prompt")


class FlowSerializer(serializers.Serializer):
    query = serializers.CharField(required=True, help_text="The query for auto-routing flow")

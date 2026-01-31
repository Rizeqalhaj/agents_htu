from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import logging

from .serializers import TextGenerationSerializer, ImageGenerationSerializer, FlowSerializer
from .crews.text_generation.crew import TextGenerationCrew
from .crews.image_generation.crew import ImageGenerationCrew
from .flows.content_generation.flow import ContentGenerationFlow

logger = logging.getLogger(__name__)


class TextGenerationView(APIView):
    """API endpoint for text generation"""

    def post(self, request):
        serializer = TextGenerationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        query = serializer.validated_data['query']

        try:
            crew = TextGenerationCrew()
            result = crew.crew().kickoff(inputs={"user_query": query})

            try:
                result_json = json.loads(result.raw)
            except json.JSONDecodeError:
                result_json = {"raw": result.raw}

            return Response({
                "success": True,
                "result": result_json
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Text generation error: {e}")
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ImageGenerationView(APIView):
    """API endpoint for image generation"""

    def post(self, request):
        serializer = ImageGenerationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        prompt = serializer.validated_data['prompt']

        try:
            crew = ImageGenerationCrew()
            result = crew.crew().kickoff(inputs={"user_prompt": prompt})

            try:
                result_json = json.loads(result.raw)
            except json.JSONDecodeError:
                result_json = {"raw": result.raw}

            return Response({
                "success": True,
                "result": result_json
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Image generation error: {e}")
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FlowView(APIView):
    """API endpoint for auto-routing flow (text or image based on query)"""

    def post(self, request):
        serializer = FlowSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        query = serializer.validated_data['query']

        try:
            flow = ContentGenerationFlow()
            result = flow.kickoff(user_query=query)

            return Response({
                "success": True,
                "result": result
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Flow error: {e}")
            return Response({
                "success": False,
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

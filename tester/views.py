import json

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import CommentReactionSerializer



# The reaction API view
class CommentReactionView(APIView):
    def post(self, request):
        serializer = CommentReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "data": serializer.data,
                "message": "Reaction Posted!!!"
            })
        return Response({
            "success": False,
            "data": serializer.data,
            "message": "Reaction could not be posted"
        })

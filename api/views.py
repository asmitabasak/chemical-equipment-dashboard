from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd

class FileUploadView(APIView):
    # Allows the API to handle file uploads
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
        
        if not file_obj:
            return Response({"error": "No file provided"}, status=400)

        # Read the chemical equipment data
        try:
            df = pd.read_csv(file_obj)
            
            # Convert the dataframe to JSON so Chart.js can read it
            data = df.to_dict(orient='records')
            return Response(data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

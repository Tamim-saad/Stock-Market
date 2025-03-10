import os
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

# Root API message
def index(request):
    return JsonResponse({"message": "Welcome to Stock API", "endpoints": ["/api/stock-data/"]})

# Fetch stock data from CSV
@csrf_exempt
def get_stock_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'data', 'stock_market_data.csv')

    if not os.path.exists(file_path):
        return JsonResponse({'error': 'CSV file not found'}, status=404)

    try:
        df = pd.read_csv(file_path)
        df.insert(0, 'id', df.index)  # Add an "id" column to track updates
        data = df.to_dict(orient='records')
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Update specific stock data in CSV
@csrf_exempt
def update_stock_data(request, id):
    if request.method == "PUT":
        file_path = os.path.join(settings.BASE_DIR, 'data', 'stock_market_data.csv')

        if not os.path.exists(file_path):
            return JsonResponse({'error': 'CSV file not found'}, status=404)

        try:
            df = pd.read_csv(file_path)

            if id < 0 or id >= len(df):
                return JsonResponse({'error': 'Invalid ID'}, status=400)

            data = json.loads(request.body)

            for key, value in data.items():
                if key in df.columns:
                    df.at[id, key] = value

            df.to_csv(file_path, index=False)
            return JsonResponse({"message": "Data updated successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)

import pandas as pd
from django.http import HttpResponse, JsonResponse
import random
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from playground.Clustring_model import clustrng
from PIL import Image, ImageEnhance
import os
import io


def Hello_world(request):
    return render(request, "hello.html", {"name": None})
    # return HttpResponse("HELLO WORLD")


def greetings(request):
    return HttpResponse("How are you?")


def sum(request):
    sum = 124 + 123
    return HttpResponse(str(sum))


def List(request):
    try:
        numbers = list()
        for i in range(100):
            numbers.append(i + random.randint(1, str(1000)))
        return HttpResponse(str(numbers))

    except Exception as e:
        return HttpResponse(str(e))


@csrf_exempt
def sum_post(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            number = data.get("number")
            sum = number + 13
            response = {
                "Sum": sum,
            }
            return JsonResponse(response, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "GET Method Called For POST"}, status=500)


@csrf_exempt
def name_con(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            s = f"{name} how are u?"
            response = {
                "Sentence": s,
            }
            return JsonResponse(response, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "GET Method Called For POST"}, status=500)


@csrf_exempt
def sum_list(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            numbers = data.get("numbers")
            new = list()
            for i in numbers:
                new.append(i + 1)
            response = {
                "updated_list": new
            }
            return JsonResponse(response, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "GET Method Called For POST"}, status=500)


@csrf_exempt
def clustering_Algo(request):
    if request.method == "POST":
        try:
            data = request.FILES["data"]
            clusters, score, labels, df = clustrng(file_path=data, max_clusters=10)
            name = data.name
            file_save_path = f"Static/data/Results_{name}"
            df.to_csv(file_save_path)

            file_name = {file_save_path.split('/')[-1]}

            with open(file_save_path, "rb") as f:
                response = HttpResponse(f.read(), content_type="text/csv")
                response["Content-Disposition"] = f'attachment;filename={file_name}'
                response["Clusters"] = str(clusters)
                response["Score"] = str(score)
                return response

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=405)
    else:
        return JsonResponse({"error": "GET Method Called For POST"}, status=500)

@csrf_exempt
def sending_img(request):
    if request.method == "POST":
        try:

            img = request.FILES["image"]

            # IMAGE PROCESSING
            image = Image.open(img)

            image = image.convert("RGB")

            enhancer = ImageEnhance.Contrast(image)
            contras_image = enhancer.enhance(2.0)
            enhancer = ImageEnhance.Brightness(contras_image)
            darkened_image = enhancer.enhance(0.5)

            file_save_path = "Static/data/New_image.jpg"
            darkened_image.save(file_save_path)

            new_image = Image.open(file_save_path)

            name = file_save_path.split("/")[-1]

            response = HttpResponse(new_image, content_type="image/jpg")
            response["Content-Disposition"] = f'attachment;filename={name}'

            return response

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=405)
    else:
        return JsonResponse({"error": "GET Method Called For POST"}, status=500)


if __name__ == "__main__":
    pass
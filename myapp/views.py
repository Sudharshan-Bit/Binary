from django.shortcuts import render, redirect
from .forms import UploadedImageForm
from .models import UploadedImage
import base64
from PIL import Image
import io

def upload_image(request):
    if request.method == 'POST':
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  # Save without committing
            instance.binary = request.FILES['image'].read()  # Read binary data
            instance.save()  # Save the instance to the database
            return redirect('upload_success')  # Redirect to success page
    else:
        form = UploadedImageForm()
    return render(request, 'upload_image.html', {'form': form})


def upload_success(request):
    return render(request, 'upload_success.html')


def image_list(request):
    images = UploadedImage.objects.all()  # Fetch all uploaded images
    image_data = []

    for image in images:
        if image.binary:
            try:
                # Convert the binary data to a base64 string
                image_base64 = base64.b64encode(image.binary).decode('utf-8')
                image_data.append(f"data:image/png;base64,{image_base64}")
            except Exception as e:
                print(f"Error processing image: {e}")
                image_data.append(None)  # Append None if there's an error
        else:
            image_data.append(None)  # In case there's no binary data

    # Combine images and their corresponding data
    combined_data = zip(images, image_data)
    print(images)

    return render(request, 'image_list.html', {'combined_data': combined_data})

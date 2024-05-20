from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from .utils.image_processing import process_image_file, preprocess_images, predict_images

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def base(request):
    return render(request, 'home/base.html')

def demo(request):
    return render(request, 'home/demo.html')

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_file_url = fs.url(filename)

            # Process and preprocess the image
            image_path = fs.path(filename)
            processed_image = process_image_file(image_path)
            preprocessed_image = preprocess_images([processed_image])

            # Predict using the preprocessed image
            prediction = predict_images(preprocessed_image)
            result = prediction[0]

            return render(request, 'home/demo.html', {
                'form': form,
                'uploaded_file_url': uploaded_file_url,
                'result': result,
            })
    else:
        form = ImageUploadForm()
    return render(request, 'home/demo.html', {'form': form})
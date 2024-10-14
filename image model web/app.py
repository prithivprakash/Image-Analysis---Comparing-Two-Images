from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

app = Flask(__name__)

# Create 'static' directory if it does not exist
if not os.path.exists('static'):
    os.makedirs('static')

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Resize to match input size of CNN
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image / 255.0  # Normalize the image
    return image

def calculate_difference(original_image_path, modified_image_path):
    original_image = preprocess_image(original_image_path)
    modified_image = preprocess_image(modified_image_path)

    original_gray = cv2.cvtColor((original_image * 255).astype('uint8'), cv2.COLOR_RGB2GRAY)
    modified_gray = cv2.cvtColor((modified_image * 255).astype('uint8'), cv2.COLOR_RGB2GRAY)

    score, diff = ssim(original_gray, modified_gray, full=True)
    diff = (diff * 255).astype('uint8')
    diff_percentage = (1 - score) * 100
    
    return diff_percentage, diff

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'original_image' not in request.files or 'modified_image' not in request.files:
            return redirect(request.url)

        original_file = request.files['original_image']
        modified_file = request.files['modified_image']
        
        if original_file.filename == '' or modified_file.filename == '':
            return redirect(request.url)
        
        original_path = os.path.join('static', 'original.jpg')
        modified_path = os.path.join('static', 'modified.jpg')
        
        original_file.save(original_path)
        modified_file.save(modified_path)
        
        diff_percentage, diff_image = calculate_difference(original_path, modified_path)
        diff_path = os.path.join('static', 'diff.jpg')
        cv2.imwrite(diff_path, diff_image)

        return render_template('index.html', diff_percentage=diff_percentage, original_image=original_path, modified_image=modified_path, diff_image=diff_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

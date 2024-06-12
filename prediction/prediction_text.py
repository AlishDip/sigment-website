from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
from PIL import Image, ImageOps, ImageEnhance
import matplotlib.pyplot as plt
import logging
import io

# модель және препроцессордың жолы
model_path = 'C:\\diplom_a\\HelloDjango\\prediction\\model'
processor_path = 'C:\\diplom_a\\HelloDjango\\prediction\\model'

# Модель мен процессорды жүктеу
processor = TrOCRProcessor.from_pretrained(processor_path)
model = VisionEncoderDecoderModel.from_pretrained(model_path)

# девайс таңдау
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Текстті анықтау үшін функция
def predict_text(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

    
    image = preprocess_image(image)

    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    
    model.eval()
    with torch.no_grad():
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    return generated_text

# суретті өңдеу үшін функция
def preprocess_image(image):
    # черно белый суретке айналдыру
    image = ImageOps.grayscale(image)
    
    # Контрастты көтеру
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    
    # Суреттің көлемін ауыстыру
    image = image.resize((190, 50), Image.LANCZOS)
    
    # RGB форматына ауыстыру
    image = image.convert('RGB')
    
    return image


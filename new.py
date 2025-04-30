import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

def caption_image(image):
    """
    Takes a PIL image and returns a caption for it.
    """
    try:
        caption = generate_caption(image)
        return caption
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
inface = gr.Interface(
    fn=caption_image,
    inputs=gr.inputs.Image(type="pil"),
    outputs="text",
    title="Image Captioning with BLIP",
    description="Upload an image to get a caption."

)

def greet(name, lname, intensity):
    return "Hello " + name + lname + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "text", "slider"],
    outputs=["text"]
)

inface.launch(server_name="127.0.0.1", server_port=7860)
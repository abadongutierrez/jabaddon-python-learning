import gradio as gr
from image_captioning_ai import caption_image_array

iface = gr.Interface(
    fn=caption_image_array, 
    inputs=gr.Image(), 
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)

iface.launch()
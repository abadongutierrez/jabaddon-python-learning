from pathlib import Path
from typing import Union
import numpy as np
import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

class ImageCaptioner:
    """A class for generating captions for images using the BLIP model."""

    def __init__(self, model_name: str = "Salesforce/blip-image-captioning-base"):
        """
        Initialize the ImageCaptioner with a pretrained model.

        Args:
            model_name: Name of the pretrained model to use
        """
        self.model_name = model_name
        self.processor = AutoProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def _generate_caption(self, image: Image.Image, max_length: int = 50) -> str:
        """
        Generate a caption for a PIL Image.

        Args:
            image: PIL Image object
            max_length: Maximum length of generated caption

        Returns:
            Generated caption text
        """
        text = "the image of"
        inputs = self.processor(images=image, text=text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        caption = self.processor.decode(outputs[0], skip_special_tokens=True)
        return caption

    def caption_from_file(self, img_path: Union[str, Path]) -> str:
        """
        Generate a caption for an image file.

        Args:
            img_path: Path to the image file

        Returns:
            Generated caption for the image
        """
        image = Image.open(img_path).convert('RGB')
        return self._generate_caption(image)

    def caption_from_array(self, input_image: np.ndarray) -> str:
        """
        Generate a caption for an image provided as a numpy array.

        Args:
            input_image: Input image as a numpy array

        Returns:
            Generated caption for the image
        """
        image = Image.fromarray(input_image)
        return self._generate_caption(image)

    def caption_from_url(self, url: str) -> str:
        """
        Generate a caption for an image from a URL.

        Args:
            url: URL of the image

        Returns:
            Generated caption for the image
        """
        response = requests.get(url, stream=True)
        response.raise_for_status()
        image = Image.open(response.raw).convert('RGB')
        return self._generate_caption(image)


# Global instance for backward compatibility
_default_captioner = None

def get_default_captioner() -> ImageCaptioner:
    """Get or create the default ImageCaptioner instance."""
    # Singleton pattern to ensure only one instance
    global _default_captioner # Tells Python we mean the global variable
    if _default_captioner is None:
        _default_captioner = ImageCaptioner()
    return _default_captioner


def caption_image_file(img_path: Union[str, Path] = "imgs/image-01.jpg") -> str:
    """
    Generate captions for an image using BLIP model.

    Args:
        img_path: Path to the image file

    Returns:
        Generated caption for the image
    """
    return get_default_captioner().caption_from_file(img_path)


def caption_image_array(input_image: np.ndarray) -> str:
    """
    Generate captions for an image provided as a numpy array.

    Args:
        input_image: Input image as a numpy array

    Returns:
        Generated caption for the image
    """
    return get_default_captioner().caption_from_array(input_image)


def caption_image_url(url: str) -> str:
    """
    Generate captions for an image from a URL.

    Args:
        url: URL of the image

    Returns:
        Generated caption for the image
    """
    return get_default_captioner().caption_from_url(url)
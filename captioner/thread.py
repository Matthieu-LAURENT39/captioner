from PIL import Image
from PySide6.QtCore import QMutex, QThread, Signal

from .caption_generator import CaptionGenerator


class ImageGeneratorThread(QThread):
    imageGenerated = Signal(Image.Image)
    """Called whenever the thread finishes generating an image"""

    def __init__(self, generator: CaptionGenerator):
        super().__init__()
        self.generator = generator
        self.mutex = QMutex()
        self.generation_needed = False

    def refresh_image(self):
        """Makes the thread regenerate an image"""
        self.mutex.lock()
        self.generation_needed = True
        self.mutex.unlock()

    def run(self) -> None:
        while True:
            if self.isInterruptionRequested():
                return

            self.mutex.lock()
            generation_needed = self.generation_needed
            self.mutex.unlock()

            if generation_needed:
                self.mutex.lock()
                self.generation_needed = False
                self.mutex.unlock()

                im = self.generator.make_image()
                self.imageGenerated.emit(im)

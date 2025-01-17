from .images import fetch_images
from .metadata import Dataset

visualizations = Dataset(
    name="visualizations",
    url="https://raw.githubusercontent.com/oldvis/dataset/main/dataset/output/visualizations.json",
    format="json",
)
authors = Dataset(
    name="authors",
    url="https://raw.githubusercontent.com/oldvis/dataset/main/dataset/output/authors.json",
    format="json",
)

__all__ = [
    "Dataset",
    "visualizations",
    "authors",
    "fetch_images",
]

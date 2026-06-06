import json
from io import BytesIO
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image, ImageOps

from car.models import Car


TARGET_SIZE = (1200, 800)
API_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CarMartBot/1.0; +https://example.com)",
}

MODEL_ALIASES = {
    ("Mercedes-Benz", "G-Wagon"): "Mercedes-Benz G-Class",
    ("Ferrari", "296 GTB"): "Ferrari 296",
    ("Ferrari", "F8 Tributo"): "Ferrari F8",
    ("Audi", "RS7"): "Audi A7",
    ("Lamborghini", "Huracan"): "Lamborghini Huracán",
}


def fetch_summary(title: str) -> dict:
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + quote(title.replace(" ", "_"))
    request = Request(url, headers=API_HEADERS)
    with urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def download_image(url: str) -> Image.Image:
    request = Request(url, headers=API_HEADERS)
    with urlopen(request) as response:
        return Image.open(BytesIO(response.read()))


class Command(BaseCommand):
    help = "Assign exact model images from Wikipedia and store same-size copies in media."

    def handle(self, *args, **options):
        saved = 0
        media_dir = Path(settings.MEDIA_ROOT) / "cars"
        media_dir.mkdir(parents=True, exist_ok=True)

        for car in Car.objects.select_related("brand").all():
            query = MODEL_ALIASES.get((car.brand.name, car.model_name), f"{car.brand.name} {car.model_name}")
            summary = fetch_summary(query)
            image_url = (summary.get("originalimage") or summary.get("thumbnail") or {}).get("source")

            if not image_url:
                self.stdout.write(self.style.WARNING(f"No image found for {car.brand.name} {car.model_name}"))
                continue

            image = download_image(image_url)
            if image.mode != "RGB":
                image = image.convert("RGB")

            fitted = ImageOps.fit(image, TARGET_SIZE, method=Image.Resampling.LANCZOS)
            buffer = BytesIO()
            fitted.save(buffer, format="JPEG", quality=92, optimize=True)

            filename = f"{car.brand.name.lower().replace(' ', '-')}-{car.model_name.lower().replace(' ', '-').replace('/', '-')}.jpg"
            car.image.save(filename, ContentFile(buffer.getvalue()), save=True)
            saved += 1

        self.stdout.write(self.style.SUCCESS(f"Assigned exact Wikipedia images to {saved} car records."))
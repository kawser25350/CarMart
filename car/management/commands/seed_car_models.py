from django.core.management.base import BaseCommand

from brand.models import Brand
from car.models import Car


CAR_CATALOG = {
    "Toyota": [
        {"model_name": "Corolla", "cc": 1800, "release_year": 2024, "quantity": 1, "price": 32000},
        {"model_name": "Camry", "cc": 2500, "release_year": 2024, "quantity": 1, "price": 42000},
        {"model_name": "RAV4", "cc": 2500, "release_year": 2024, "quantity": 1, "price": 45000},
        {"model_name": "Hilux", "cc": 2800, "release_year": 2024, "quantity": 1, "price": 47000},
        {"model_name": "Land Cruiser", "cc": 3300, "release_year": 2024, "quantity": 1, "price": 85000},
    ],
    "Ford": [
        {"model_name": "Fiesta", "cc": 1500, "release_year": 2023, "quantity": 1, "price": 22000},
        {"model_name": "Focus", "cc": 1600, "release_year": 2024, "quantity": 1, "price": 28000},
        {"model_name": "Mustang", "cc": 5000, "release_year": 2024, "quantity": 1, "price": 65000},
        {"model_name": "Ranger", "cc": 3200, "release_year": 2024, "quantity": 1, "price": 48000},
        {"model_name": "Explorer", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 56000},
    ],
    "Honda": [
        {"model_name": "Civic", "cc": 1800, "release_year": 2024, "quantity": 1, "price": 30000},
        {"model_name": "Accord", "cc": 2400, "release_year": 2024, "quantity": 1, "price": 36000},
        {"model_name": "CR-V", "cc": 1500, "release_year": 2024, "quantity": 1, "price": 41000},
        {"model_name": "City", "cc": 1500, "release_year": 2024, "quantity": 1, "price": 26000},
        {"model_name": "Pilot", "cc": 3500, "release_year": 2024, "quantity": 1, "price": 59000},
    ],
    "Mercedes-Benz": [
        {"model_name": "C-Class", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 65000},
        {"model_name": "E-Class", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 78000},
        {"model_name": "S-Class", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 120000},
        {"model_name": "GLA", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 58000},
        {"model_name": "G-Wagon", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 170000},
    ],
    "Ferrari": [
        {"model_name": "Roma", "cc": 3900, "release_year": 2024, "quantity": 1, "price": 220000},
        {"model_name": "296 GTB", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 320000},
        {"model_name": "F8 Tributo", "cc": 3900, "release_year": 2023, "quantity": 1, "price": 290000},
        {"model_name": "SF90 Stradale", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 500000},
        {"model_name": "Purosangue", "cc": 6500, "release_year": 2024, "quantity": 1, "price": 450000},
    ],
    "Porsche": [
        {"model_name": "911", "cc": 3800, "release_year": 2024, "quantity": 1, "price": 140000},
        {"model_name": "Cayenne", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 95000},
        {"model_name": "Panamera", "cc": 2900, "release_year": 2024, "quantity": 1, "price": 110000},
        {"model_name": "Macan", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 70000},
        {"model_name": "Taycan", "cc": 0, "release_year": 2024, "quantity": 1, "price": 150000},
    ],
    "BMW": [
        {"model_name": "3 Series", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 55000},
        {"model_name": "5 Series", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 70000},
        {"model_name": "7 Series", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 110000},
        {"model_name": "X5", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 95000},
        {"model_name": "X7", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 125000},
    ],
    "Volkswagen": [
        {"model_name": "Golf", "cc": 1600, "release_year": 2024, "quantity": 1, "price": 28000},
        {"model_name": "Polo", "cc": 1400, "release_year": 2024, "quantity": 1, "price": 22000},
        {"model_name": "Passat", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 34000},
        {"model_name": "Tiguan", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 42000},
        {"model_name": "Touareg", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 60000},
    ],
    "Chevrolet": [
        {"model_name": "Spark", "cc": 1200, "release_year": 2024, "quantity": 1, "price": 18000},
        {"model_name": "Cruze", "cc": 1600, "release_year": 2024, "quantity": 1, "price": 25000},
        {"model_name": "Malibu", "cc": 2400, "release_year": 2024, "quantity": 1, "price": 32000},
        {"model_name": "Camaro", "cc": 6200, "release_year": 2024, "quantity": 1, "price": 65000},
        {"model_name": "Tahoe", "cc": 5300, "release_year": 2024, "quantity": 1, "price": 75000},
    ],
    "Nissan": [
        {"model_name": "Sunny", "cc": 1500, "release_year": 2024, "quantity": 1, "price": 21000},
        {"model_name": "Altima", "cc": 2500, "release_year": 2024, "quantity": 1, "price": 32000},
        {"model_name": "X-Trail", "cc": 2500, "release_year": 2024, "quantity": 1, "price": 38000},
        {"model_name": "Patrol", "cc": 5600, "release_year": 2024, "quantity": 1, "price": 80000},
        {"model_name": "GT-R", "cc": 3800, "release_year": 2024, "quantity": 1, "price": 115000},
    ],
    "Hyundai": [
        {"model_name": "Elantra", "cc": 1600, "release_year": 2024, "quantity": 1, "price": 24000},
        {"model_name": "Sonata", "cc": 2500, "release_year": 2024, "quantity": 1, "price": 30000},
        {"model_name": "Tucson", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 35000},
        {"model_name": "Santa Fe", "cc": 2500, "release_year": 2024, "quantity": 1, "price": 42000},
        {"model_name": "Palisade", "cc": 3800, "release_year": 2024, "quantity": 1, "price": 50000},
    ],
    "Lamborghini": [
        {"model_name": "Huracan", "cc": 5200, "release_year": 2024, "quantity": 1, "price": 250000},
        {"model_name": "Aventador", "cc": 6500, "release_year": 2024, "quantity": 1, "price": 450000},
        {"model_name": "Revuelto", "cc": 6500, "release_year": 2024, "quantity": 1, "price": 600000},
        {"model_name": "Urus", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 300000},
        {"model_name": "Gallardo", "cc": 5200, "release_year": 2023, "quantity": 1, "price": 180000},
    ],
    "Audi": [
        {"model_name": "A3", "cc": 1600, "release_year": 2024, "quantity": 1, "price": 35000},
        {"model_name": "A6", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 65000},
        {"model_name": "Q5", "cc": 2000, "release_year": 2024, "quantity": 1, "price": 55000},
        {"model_name": "Q7", "cc": 3000, "release_year": 2024, "quantity": 1, "price": 80000},
        {"model_name": "RS7", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 140000},
    ],
    "Aston Martin": [
        {"model_name": "DB11", "cc": 5200, "release_year": 2024, "quantity": 1, "price": 220000},
        {"model_name": "Vantage", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 180000},
        {"model_name": "DBX", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 210000},
        {"model_name": "DBS", "cc": 5200, "release_year": 2024, "quantity": 1, "price": 300000},
        {"model_name": "Valhalla", "cc": 4000, "release_year": 2024, "quantity": 1, "price": 800000},
    ],
}


class Command(BaseCommand):
    help = "Seed the Car table with models for every existing brand."

    def handle(self, *args, **options):
        brands = {brand.name: brand for brand in Brand.objects.all()}
        existing = set(Car.objects.values_list("brand__name", "model_name"))
        pending = []

        for brand_name, models in CAR_CATALOG.items():
            brand = brands.get(brand_name)
            if brand is None:
                self.stdout.write(self.style.WARNING(f"Skipping missing brand: {brand_name}"))
                continue

            for model_data in models:
                if (brand_name, model_data["model_name"]) in existing:
                    continue

                pending.append(Car(brand=brand, **model_data))

        if pending:
            Car.objects.bulk_create(pending)

        self.stdout.write(
            self.style.SUCCESS(
                f"Added {len(pending)} car models across {len(CAR_CATALOG)} brands."
            )
        )
"""
Idempotent deploy bootstrap:
  1. Create an admin superuser from DJANGO_SUPERUSER_* environment variables.
  2. Seed the default "Down Syndrome Awareness" flyer (only when media is
     persisted via Cloudinary, so the image doesn't 404 on Render).

Safe to run on every startup/deploy.
"""
import os
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.management.base import BaseCommand

from main.models import Flyer

FLYER_TITLE = "Down Syndrome Awareness"
FLYER_CAPTION = (
    "The colours of Down syndrome: Blue symbolises acceptance and awareness; "
    "Yellow symbolises happiness, sunshine and the extra chromosome that makes "
    "individuals shine brighter. Wear blue and yellow to show your support!"
)
SEED_ASSET = Path(settings.BASE_DIR) / "main" / "seed_assets" / "down-syndrome-awareness.jpg"


class Command(BaseCommand):
    help = "Create the admin user and seed starter content (idempotent)."

    def handle(self, *args, **options):
        self._create_superuser()
        self._seed_flyer()

    def _create_superuser(self):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "")

        if not username or not password:
            self.stdout.write("Superuser env vars not set; skipping superuser creation.")
            return
        if User.objects.filter(username=username).exists():
            self.stdout.write(f"Superuser '{username}' already exists.")
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Created superuser '{username}'."))

    def _seed_flyer(self):
        # Only seed when uploads persist (Cloudinary). Otherwise the record would
        # point at an ephemeral/unserved file and show as a broken image.
        if not os.getenv("CLOUDINARY_URL"):
            self.stdout.write("CLOUDINARY_URL not set; skipping flyer seed.")
            return
        if Flyer.objects.filter(title=FLYER_TITLE).exists():
            self.stdout.write("Default flyer already exists.")
            return
        if not SEED_ASSET.exists():
            self.stdout.write(f"Seed asset missing at {SEED_ASSET}; skipping flyer seed.")
            return

        flyer = Flyer(title=FLYER_TITLE, caption=FLYER_CAPTION, order=0)
        with open(SEED_ASSET, "rb") as fh:
            flyer.image.save("down-syndrome-awareness.jpg", File(fh), save=True)
        self.stdout.write(self.style.SUCCESS("Seeded default awareness flyer."))

# CarMart

## Seed car models

Populate the `car_car` table without adding rows manually:

```bash
python manage.py seed_car_models
```

The command is idempotent, so rerunning it will not duplicate existing brand/model pairs.

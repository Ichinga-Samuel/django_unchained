# Evironment Variables

Place an environment file e.g *.env* file at root of a project or any other desired place.

## Djang Environs

Use environs package to handle environment variables

```bash
pip install environs['django']
```

```python
# settings.py
from environs import env
env = Env()
env.read_env()
```

## Using Environment Variables in multiple environments

Create different files for different environments e.g. *.env.environment*. Point the *read_env* method to the desired path as shown in the code below.

```python
# settings.py
from environs import env
env = Env()
env.read_env(BASE_DIR / '.env.development')
```

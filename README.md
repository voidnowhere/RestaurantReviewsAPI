# Restaurant Reviews API & [Restaurant Reviews WEB](https://github.com/voidnowhere/RestaurantReviewsWEB)

## `Architecture`

![architecture](https://user-images.githubusercontent.com/79842485/236669654-f579c87c-83f5-4655-948f-a0e437a426d6.png)

<hr>

## `Clone repository`
```bash
git clone https://github.com/voidnowhere/RestaurantReviewsAPI.git
```

<hr>

## `Set up environment`
### Install `virtualenv`
```bash
pip install virtualenv
```
### Change current directory to `RestaurantReviewsAPI`
```bash
cd RestaurantReviewsAPI
```
### Create python `virtual environment`
```bash
python -m venv venv
```
### Activate it
- `Windows`
```bash
venv\Scripts\activate
```
- `Linux`
```bash
source venv/Scripts/activate
```
- `PowerShell`
no scripts like the activate script are allowed to be executed so you need to run PowerShell as `admin` and change `ExecutionPolicy` to `AllSigned` then type `A` to `Always run` `the command is under` in the end use `the command above` to activate virtual environment
```bash
Set-ExecutionPolicy AllSigned
```
### Install `virtualenv requirements`
```bash
pip install -r requirements.txt
```
### Create `.env` file and fill it
```bash
copy .env.example .env
```
### Generate django `SECRET_KEY`
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
### Make `migrations`
```bash
python manage.py makemigrations
```
### Apply `migrations`
```bash
python manage.py migrate
```
### Create your `superuser` for `django admin site`
```bash
python manage.py createsuperuser
```
### Run server
```bash
python manage.py runserver
```

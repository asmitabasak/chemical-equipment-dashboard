# Command to set up the environment
echo "Setting up Chemical Equipment Dashboard..."
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver

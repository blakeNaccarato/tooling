copier gh:blakeNaccarato/copier-python . -r 665ef69
py -3.9 -m venv .venv
.venv/Scripts/activate
pip install -U pip  # throws [WinError 5], but still works on its own
pip install -r requirements_dev.txt  # packages for development
flit install -s

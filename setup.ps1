copier gh:blakeNaccarato/copier-python . -r 0.1.1-23-gcffe5a5
py -3.9 -m venv .venv
.venv/Scripts/activate
pip install -U pip  # throws [WinError 5], but still works on its own
pip install -r requirements_dev.txt  # packages for development
flit install -s

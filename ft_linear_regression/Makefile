PYTHON := .venv/bin/python

.PHONY: all setup train predict plot visualize clean fclean re

all: train

setup:
	python3 -m venv .venv
	.venv/bin/pip install matplotlib

train:
	$(PYTHON) train.py

predict:
	$(PYTHON) predict.py

plot:
	$(PYTHON) plot.py
	open regression.png

visualize: train plot

clean:
	rm -f thetas.txt regression.png
	rm -rf __pycache__

fclean: clean
	rm -rf .venv

re: fclean setup train

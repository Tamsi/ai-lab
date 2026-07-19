PYTHON := .venv/bin/python
TRAIN := datasets/dataset_train.csv
TEST := datasets/dataset_test.csv
WEIGHTS := weights.txt

.PHONY: all setup describe histogram scatter pair train predict clean fclean re

all: describe

setup:
	python3 -m venv .venv
	.venv/bin/pip install matplotlib

describe:
	$(PYTHON) describe.py $(TRAIN)

histogram:
	$(PYTHON) histogram.py $(TRAIN)

scatter:
	$(PYTHON) scatter_plot.py $(TRAIN)

pair:
	$(PYTHON) pair_plot.py $(TRAIN)

train:
	$(PYTHON) logreg_train.py $(TRAIN)

predict:
	$(PYTHON) logreg_predict.py $(TEST) $(WEIGHTS)

clean:
	rm -f weights.txt houses.csv *.png
	rm -rf __pycache__

fclean: clean
	rm -rf .venv

re: fclean setup

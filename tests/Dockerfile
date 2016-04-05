FROM tsutomu7/alpine-python-pandas
RUN pip install matplotlib
RUN pip install jupyter
ADD test.py .
CMD jupyter notebook --ip=0.0.0.0

FROM python:3.9

RUN pip install --no-cache-dir \
    dash==2.2.0 \
    pandas==1.3.5 \
    jupyter-dash==0.4.0 \
    notebook==6.4.5

CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]

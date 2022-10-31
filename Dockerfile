FROM huggingface/transformers-pytorch-gpu

WORKDIR /app
RUN python3 -m pip install Flask
COPY app/app.py /app
COPY app/templates/index.html /app/templates/

EXPOSE 5000

CMD ["python3", "app.py"]

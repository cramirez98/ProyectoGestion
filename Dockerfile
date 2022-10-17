FROM huggingface/transformers-pytorch-gpu

RUN python3 -m pip install Flask

CMD ["/bin/bash"]
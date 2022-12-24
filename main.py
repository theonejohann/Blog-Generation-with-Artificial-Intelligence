# Importing the pipeline function from the transformers library
from transformers import pipeline
# Creating a TextGenerationPipeline for text generation
generator = pipeline(task='text-generation', model='gpt2')
# Generating
print(generator("The dog runs around the boy and ", max_length=60, num_return_sequences=5))
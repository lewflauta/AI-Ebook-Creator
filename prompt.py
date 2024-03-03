import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
APIKEY = 0
genai.configure(api_key=APIKEY)
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

%%time
response = model.generate_content("What is the meaning of life?")

to_markdown(response.text)









def process_prompts(prompt, max_iterations=5):
  """
  Simulates iteratively processing prompts (replace with actual interaction with Gemini).

  Args:
      prompt: The initial prompt to start with.
      max_iterations: The maximum number of iterations to perform (optional).

  Returns:
      A list of processed individual prompts.
  """

  processed_prompts = []
  for _ in range(max_iterations):
    # Simulate processing with Gemini (replace with actual interaction)
    processed_prompt = process_prompt(prompt)  # Placeholder function, replace with real logic
    processed_prompts.append(processed_prompt)

    # Simulate splitting into subsequent prompts (replace with actual processing)
    subsequent_prompts = split_prompt(processed_prompt)  # Placeholder function, replace with logic

    # Iterate through subsequent prompts, handling potential base case
    for sub_prompt in subsequent_prompts:
      if not sub_prompt:  # Handle base case (no further processing)
        break
      processed_prompts.extend(process_prompts(sub_prompt, max_iterations - 1))

  return processed_prompts

def process_prompt(prompt):  # Placeholder function, replace with actual interaction logic
  """
  Placeholder function to simulate processing a single prompt with Gemini.

  Args:
      prompt: The prompt to process.

  Returns:
      A simulated processed prompt (replace with actual response from Gemini).
  """
  # Replace with actual interaction with Gemini and return the response
  return f"Processed prompt: {prompt}"

def split_prompt(processed_prompt):  # Placeholder function, replace with actual logic
  """
  Placeholder function to simulate splitting a processed prompt into subsequent prompts.

  Args:
      processed_prompt: The processed prompt to split.

  Returns:
      A list of simulated subsequent prompts (replace with actual splitting logic).
  """
  # Replace with logic to split the processed prompt into subsequent prompts
  return [processed_prompt + " (part 1)", processed_prompt + " (part 2)"]

# Example usage
initial_prompt = "This is the initial prompt."
processed_prompts = process_prompts(initial_prompt)

print("Processed prompts:")
for prompt in processed_prompts:
  print(prompt)

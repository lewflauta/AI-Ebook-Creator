# -*- coding: utf-8 -*-
"""ebookgenerator.ipynb




!pip install -q -U google-generativeai

"""### Import packages

Import the necessary packages.
"""

import pathlib
import textwrap
import re

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from typing import List


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
from google.colab import userdata


model = genai.GenerativeModel('gemini-pro')


outline_text = outline.text




def chunk_gemini_text(text):
  """
  This function takes a string containing the text of a Gemini response with title, chapter, and subchapters and
  chunks it into prompts, each containing a chapter and its subchapters.

  Args:
      text: The text of the Gemini response.

  Returns:
      A list of strings, where each string represents a prompt containing a chapter and its subchapters.
  """
  prompts = []
  current_chapter = None

  # Split the text into lines, handling potential empty lines
  lines = [line.strip() for line in text.splitlines() if line.strip()]
  print(lines)


  # Loop through each line
  for line in lines:

    if line.startswith("**Chapter"):
      # New chapter encountered, update current chapter and clear prompt
      current_chapter = line.split(": ")[-1]
      prompts.append(f"{line}\n")
    elif current_chapter:
      # Subchapter encountered, append to the current prompt
      prompts[-1] += f"{line}\n\n"

  return prompts



prompts = chunk_gemini_text(outline_text)

# Print the chunked prompts
for prompt in prompts:
  print (prompt)
  additional_prompt = ""
  additional_prompt = input("additional prompt or continue :")
  response_chapter = model.generate_content(f"Please create a 1000 word chapter for a book named {topic} that covers {prompt}. Also flavor it with {additional_prompt}. I don't want transition words such as finally and in conclusion")
  chapter = response_chapter.text
  print(chapter)



response.candidates


# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("What is the meaning of life?", stream=True)

for chunk in response:
  print(chunk.text)
  print("_"*80)

topic = "What is the meaning of life"
response = model.generate_content(f"test {topic}", stream=True)


response.prompt_feedback



try:
  response.text
except Exception as e:
  print(f'{type(e).__name__}: {e}')




import os
import openai

a = input("What cuisine would you like? ")
b = input("List your ingredients: ")

def GPT_Completion(texts):
  openai.api_key = "(API-Key here)"
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt =  texts,
  temperature = 0.99,
  top_p = 1,
  max_tokens = 2500,
  frequency_penalty = 0,
  presence_penalty = 0
  )
  return print(response.choices[0].text)

recipe = 'Provide a precise directions to make a' + a + 'dish based on the following ingredients:  ' + b 



GPT_Completion(recipe)

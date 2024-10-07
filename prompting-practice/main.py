import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# API_KEY=os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=API_KEY)

# prompt = """
# Please categorize this customer query:
# Email: "I ordered a phone two weeks ago but haven't received it. Can you check the status of my order?"

# Provide output in the following format:
# {
#   "Customer Issue": "Issue description",
#   "Urgency Level": "High/Medium/Low",
#   "Suggested Resolution": "Proposed action"
# }
# """

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": prompt}
#     ]
# )
# print(completion.choices[0].message.content)

# few-shot prompting
prompt = """

"""
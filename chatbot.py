from openai import OpenAI

client = OpenAI()

# accepts a preferred model and a list of messages
# makes chat completions API call
# returns the response message content
def get_api_chat_response_message(model, messages):
    # make the API call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    # return the response text
    return response_content

# prompt the user to ask a question
# user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

plot_description = """In the heart of the bustling metropolis of Astoria, the old Henderson House stands as a
silent sentinel, its imposing facade a stark contrast to the modern skyscrapers that
surround it. Once a grand mansion, it now sits abandoned, its windows broken, its
once-luxurious gardens now a tangle of weeds and ivy. The house is said to be haunted, its
halls echoing with the whispers of a tragic past.
When seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately
drawn to the mystery of the old house. Despite the warnings of her new friends, Mia
becomes determined to uncover the truth behind the rumors that surround it.
As Mia delves deeper into the history of the Henderson House, she discovers a dark and
twisted tale. The house was once the home of the wealthy and influential Henderson
family, until one fateful night when a series of mysterious disappearances rocked the city.
The family was never seen again, and the house was left abandoned, a grim reminder of
the tragedy that had befallen it.
Determined to unravel the mystery, Mia enlists the help of her friends, including the
charming and enigmatic Alex. Together, they embark on a dangerous journey into the heart
of the city's dark underbelly, where they must confront not only the malevolent spirits that
haunt the Henderson House but also the sinister forces that seek to keep its secrets buried.
As they dig deeper, Mia and her friends uncover a web of lies and deceit that stretches
back decades, and they realize that the key to solving the mystery may lie closer to home
than they ever imagined. But with each step closer to the truth, they also draw closer to
danger, and Mia must confront her own fears if she is to uncover the secrets of the
Henderson House and escape its haunting legacy."""

plot_prompt = f"""
Summarize the text below, in between < and >, in 100 words or less.

<{plot_description}>

Write this as one paragraph, making the summary exciting, enigmatic, mysterious and compelling, this will be used for an email to announce the book release.
"""

messages = [
    {"role": "system", "content": "You are an intelligent and  helpful assistant."},
    {"role": "user", "content": plot_prompt}
]

book_summary = get_api_chat_response_message(model, messages)

print("\n" + book_summary + "\n")
 
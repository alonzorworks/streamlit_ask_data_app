import seaborn as sns
import openai

def set_openai_api_key(api_key):
    openai.api_key = api_key

def generate_graph(data, prompt, style="whitegrid", size=(6, 4)):
    if not openai.api_key:
        raise ValueError("OpenAI API key not set. Please use `set_openai_api_key` function to set the API key.")
    
    # Use the OpenAI ChatGPT API to generate a response based on the prompt/question
    response = openai.Completion.create(
        engine="davinci",  # Choose the appropriate GPT-3 model
        prompt=prompt,
        max_tokens=100,  # Adjust this based on the desired response length
        n=1,  # Number of responses to generate
        stop=None,  # Stop generating responses at a custom token
    )
    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Generate a Seaborn graph based on the supplied data and the generated text
    sns.set(style=style)
    sns.set(rc={"figure.figsize": size})
    # Use Seaborn plotting functions here to create the desired graph
    # For example:
    sns.barplot(data=data, x="x_column", y="y_column")
    sns.despine()

    # Show the graph
    sns.plt.show()

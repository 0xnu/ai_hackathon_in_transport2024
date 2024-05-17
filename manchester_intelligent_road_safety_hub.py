import os
import csv
import openai
import gradio as gr

class OpenAIClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def ask_question(self, prompt):
        chat_completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return chat_completion.choices[0].message.content.strip()

# Set your OpenAI API key
api_key = os.getenv('OPENAI_KEY')
openai_client = OpenAIClient(api_key)

def load_dataset(unified_csv_file: str) -> list[dict[str, str]]:
    """Load the unified dataset from a CSV file."""
    with open(unified_csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

def ask_openai(question: str, dataset: list[dict[str, str]]) -> str:
    """Ask OpenAI a question about the dataset."""
    context = "This is a dataset containing information about traffic accidents. Each row represents an accident with various attributes such as Severity, Latitude, Longitude, RoadSurface, LightingCondition, WeatherCondition, and JunctionDetail."

    # Convert dataset to a string format suitable for the prompt
    dataset_str = "\n".join([str(row) for row in dataset[:5]])  # Limiting to the first 5 rows for brevity

    prompt = f"{context}\n\nDataset:\n{dataset_str}\n\nQuestion: {question}\nAnswer:"

    return openai_client.ask_question(prompt)

def interactive_interface(question: str, unified_csv_file: str) -> str:
    """Interactive interface to ask questions about the dataset."""
    dataset = load_dataset(unified_csv_file)
    return ask_openai(question, dataset)

def main() -> None:
    unified_dataset_file = "./data/unified_dataset.csv"

    # Gradio interface
    iface = gr.Interface(
        fn=lambda question: interactive_interface(question, unified_dataset_file),
        inputs="text",
        outputs="text",
        title="DfT Intelligent Road Safety Hub",
        description="Ask questions about the traffic accident in Manchester."
    )

    iface.launch(share=True)  # Enable public link

if __name__ == "__main__":
    main()

# IMPORTANT! - before running this script please ensure you do the following:
# 1) - download all files on https://huggingface.co/mistralai/Mistral-7B-v0.1/tree/main
# 2) - intall all missing modules such as "torch" and "transformers"
# 3) - place this file in the root directorying alongside you model and other files
# 4) - open the folder where all the files are store in you IDE (to ensure your workplace is set up to use the root directory)
# 5) - you can now run the code :)

# This code will only be executed if the script is run as the main program
if __name__ == "__main__":
    import torch
    import datetime
    from transformers import AutoModelForCausalLM, AutoTokenizer

    # Display the start time
    start_time = datetime.datetime.now()
    print("Start Time:", start_time.strftime("%Y-%m-%d %H:%M:%S"))

    model_id = "mistralai/Mistral-7B-v0.1"
    # Automatically use GPU if available, else use CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    # Load the model in full precision (remove the load_in_4bit=True argument)
    model = AutoModelForCausalLM.from_pretrained(model_id, low_cpu_mem_usage=True ).to(device)

    text = """You are a Data Science Student. 
    Your role is to provide a description of why you'd make a good fit for a coding job. 
    You should create a short elevator pitch of no more than 4 to 5 sentences 
    Here's an example:

    "I'm an expert as using python and love to code in my free time.
    Some of my passion project include creating DNA Sequence Analysis progams."
    """

    inputs = tokenizer(text, return_tensors="pt").to(device)

    # max_new_tokens will limit the number of character is the LLMs response.
    # This will also alter the time it takes to create an output.
    # Less tockens will result in faster results being displayed.
    outputs = model.generate(**inputs, max_new_tokens=30)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
    print("Test completed")

    # Display the end time
    end_time = datetime.datetime.now()
    print("End Time:", end_time.strftime("%Y-%m-%d %H:%M:%S"))

    # Calculate and display the duration
    duration = end_time - start_time
    print("Duration:", duration)

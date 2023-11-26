json_data = {
    "citations": [
        {
            "document_ids": ["doc_1"],
            "end": 266,
            "start": 88,
            "text": "advanced systems with AI that can complete tasks on its own, utilising language models to reason and make decisions. They can perform tasks on your behalf using tools and memory."
        },
        {
            "document_ids": ["doc_1"],
            "end": 349,
            "start": 305,
            "text": "type of bot with more advanced capabilities."
        },
        {
            "document_ids": ["doc_0"],
            "end": 519,
            "start": 390,
            "text": "autonomous computational systems that inhabit a complex dynamic environment and act autonomously to achieve their designed goals."
        }
    ],
    "documents": [
        {
            "id": "doc_1",
            "text": "In this blog post, we’ll take a look at how autonomous agents bring AI into the way that applications function while bringing us closer to an autonomous world.\n\nWhat are autonomous agents?\n\nIn our technological landscape, agents are advanced systems that harness the power of language models for reasoning and decision-making. What sets them apart from just another bot or framework is the fact that agents can perform tasks on your behalf using tools and memory.",
            "title": "An Introduction to Autonomous Agents",
            "url": "https://developer.salesforce.com/blogs/2023/10/an-introduction-to-autonomous-agents"
        },
        {
            "id": "doc_0",
            "text": "According to Maes (1995)\n\n\"Autonomous agents are computational systems that inhabit some complex dynamic environment, sense and act autonomously in this environment, and by doing so realize a set of goals or tasks for which they are designed.\"[2]\n\nFranklin and Graesser (1997) review different definitions and propose their definition",
            "title": "Autonomous agent",
            "url": "https://en.wikipedia.org/wiki/Autonomous_agent"
        }
    ],
    "text": "I found multiple definitions for the term \"agent\". \n\nOne definition describes agents as advanced systems with AI that can complete tasks on its own, utilising language models to reason and make decisions. They can perform tasks on your behalf using tools and memory. This definition describes agents as a type of bot with more advanced capabilities. \n\nAnother definition is that agents are autonomous computational systems that inhabit a complex dynamic environment and act autonomously to achieve their designed goals."
}

# Extract the text starting with "I found multiple definitions"
text = json_data["text"]

docs = json_data["documents"]
#print(f"Docs: {docs}")
second_text = ""
for doc in docs:
    new = f"\n{doc['title']} : {doc['url']}\n"
    second_text = second_text + new
text = text + second_text
print(text)
"""
found_definitions_text = json_data["text"][start_index:]

# List all URLs from the rest of the JSON
urls = [doc["url"] for doc in json_data["documents"]]

# Print the extracted text and list of URLs
print("Extracted Text:")
print(found_definitions_text)
print("\nList of URLs:")
for url in urls:
    print(url)
"""
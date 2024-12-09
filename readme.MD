# Conversational Mental Health Agent 


**Dataset**

The dataset used for training the agent is sourced from Huggingface datasets, specifically the "ZahrizhalAli/mental_health_conversational_dataset". This dataset consists of 3512 rows, with a total of approximately 5 million tokens for the context and response pairs.

**Approach**

Unlike traditional approaches that cache a small portion of the dataset in memory and prompt the model for a response, this agent is designed to learn from the entire semantic space available. This allows the agent to provide more comprehensive and accurate responses to user queries.

**Functionality**

The agent is integrated into a Django web application, which provides a user interface for users to interact with the agent. The application uses the OpenAI API to process user input and generate responses. The agent's responses are designed to be empathetic, informative, and supportive, providing users with resources and guidance for their mental health concerns.

**Technical Details**

The application is built using Django 5.1.3, with a PostgreSQL database for storing user interactions and agent responses. The OpenAI API is used for natural language processing and generating responses. The application is designed to be scalable and secure, with proper error handling and logging mechanisms in place.

**Future Development**

Fine-tuning on a larger dataset sample would improve performance over the base LLM. Having trained on ~300,000 tokens out the possible 5miilion

**Contributing**

Contributions to this project are welcome. If you're interested in contributing, please review the project's code and documentation, and submit a pull request with your proposed changes.

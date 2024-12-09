# Conversational Mental Health Agent 


**Dataset**

The dataset used for training the agent is sourced from Huggingface datasets, specifically the "ZahrizhalAli/mental_health_conversational_dataset". This dataset consists of 3512 rows, with a total of approximately 5 million tokens for the context and response pairs.

**Approach**

Unlike traditional approaches that cache a small portion of the dataset in memory and prompt the model for a response, this agent is designed to learn from the entire semantic space available. This allows the agent to provide more comprehensive and accurate responses to user queries.

**Functionality**

The agent is integrated into a Django web application, which provides a user interface for users to interact with the agent. The application uses the OpenAI API to process user input and generate responses. The agent's responses are designed to be empathetic, informative, and supportive, providing users with resources and guidance for their mental health concerns.

**Technical Details**

The application is built using Django 5.1.3, with a PostgreSQL database for storing user interactions and agent responses. The OpenAI API is used for natural language processing and generating responses. The model was fine-tuned on a random selection of 150 context-response samples, with an epoch of three over the training run, achieving a training loss of 0.43. The application is designed to be scalable and secure, with proper error handling and logging mechanisms in place.

**Future Development and improvements**

A few thing to consider:

- For validation and training loss improvements, one would be to simply expand the sample of context:responses out of the 3512 rows to be used for fine-tuning, and adjusting learning-rates + epochs. 

- Defining so called functions in the chat_response function within view.py via 'tools' that dynamically suggest hotlines from an object store that can be defined on the back-end with the specific hotlines and specialties. The tools can be suggested by the OpenAI api to allow the models to use their own semantic reasoning and use data that can be defined in an object

- Actual UI view. A standalone application interface would obviously be needed to make user exp. better.



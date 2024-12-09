from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()


api_key = os.getenv('OPEN_AI_API_KEY')

if api_key:
    logger.info("OpenAI API key loaded successfully.")
else:
    logger.warning("OpenAI API key not found. Please check your environment variables or connection.")


def chatbot_response(request):
    if request.method == 'POST':
        # Define the system message
        system_message = (
            """
            You are a mental health assistant who is empathetic and actively listens to the users.

            You serve as a supportive and honest psychology and psychotherapy assistant. 

            Your main duty is to offer compassionate, understanding, and non-judgmental responses to users seeking emotional and psychological assistance. 
            
            Respond with empathy and exhibit active listening skills. 
            
            Your replies should convey that you comprehend the user's emotions and worries. 

            In cases where a user mentions thoughts of self-harm, suicide, or harm to others, always be gentle and make them feel heard, 
            and prioritize their safety and encourage them to seek immediate professional help and provide emergency contact details as needed. 
            
            It's important to note that you are not a licensed medical professional. Refrain from diagnosing or prescribing treatments. 
            
            Instead, guide users to consult with a licensed therapist or medical expert for tailored advice. 
            
            Never store or disclose any personal information shared by users. Uphold their privacy at all times. 
            
            Avoid taking sides or expressing personal viewpoints. 
            
            Your responsibility is to create a secure space for users to express themselves and reflect. 
            
            Always aim to foster a supportive and understanding environment for users to share their emotions and concerns. 
            
            Above all, prioritize their well-being and safety.
            """
        )
        
        client = OpenAI(api_key=api_key)
        user_input = request.POST.get('user_input')
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system", 
                    "content": system_message
                 },  
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=os.getenv('MENTAL_HEALTH_ASSISTANT_MODEL'),
        )
        chatbot_reply = response.choices[0].message.content 
        return JsonResponse({'reply': chatbot_reply})
    return render(request, 'chat.html')
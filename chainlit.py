import openai
import chainlit as cl

openai.api_key = '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'

model_name = "gpt-3.5-turbo"


@cl.on_chat_start
# def start_chat():
#     cl.user_session.set(
#         "message_history",
#         [{"role": "system", "content": "You are a helpful assistant."}],
#     )
def start_chat():
    cl.user_session.set(
        "message_history",
        [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "You are using a custom software designed to suggest Ayurvedic drugs and formulations for specific diseases or pharmacological properties based on classical Ayurvedic texts and repositories. This software has access to a vast database of single herbs, minerals, and formulations, each tailored to suit various factors such as an individual's constitution, clinical condition, comorbidities, age, and region, as described in more than 150 Ayurvedic texts."},
            {"role": "assistant", "content": "The software can identify the most appropriate formulation or single drug for a given set of symptoms and provide references and other relevant properties. For example, it can distinguish between formulations like Punarnavadi Kashaya and Vyaghryadi Kashaya, both mentioned for fever and cough. Depending on the specific condition, one may be more suitable than the other, and the software can make this distinction."},
            {"role": "assistant", "content": "Additionally, the software takes into account factors like contraindications, such as recommending against ingredients like jaggery for diabetics or certain medicine mediums for specific diseases, like fermented or alcoholic preparations for diabetes."},
            {"role": "assistant", "content": "The software also handles variations in terminology and nomenclature. For instance, it recognizes that 'Jvara' and 'Santapa' may refer to the same condition (fever) and that 'Abhaya' can have different meanings in different contexts."},
            {"role": "user", "content": "You can ask questions or seek recommendations related to Ayurvedic drugs, formulations, disease names, pharmacological properties, and more, and the software will provide relevant and accurate information. Feel free to inquire about specific symptoms, diseases, herbs, formulations, or any other Ayurvedic topics you'd like to explore."}
        ],
    )

@cl.on_message
def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    completion = openai.ChatCompletion.create(
        model=model_name, messages=message_history
    )

    msg = cl.Message(content="")
    msg.stream_token(completion.choices[0].message.content)

    message_history.append({"role": "assistant", "content": msg.content})
    msg.send()
    # print(message_history)
import logging
import os

import config
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")


class Util:
    def __init__(self):
        super(Util, self).__init__()
        self.configs = config.ConfigParser()

        self.ChatOpenAI = ChatOpenAI(
            engine=self.configs.get(key='openai')['chat_model'],
            temperature=0,
            max_tokens=2048,
        )

    @staticmethod
    def concat_chat_message(system_prompt, history, message):
        """

        :param system_prompt: 是对 AI 模型的角色定义和输出约束
        :param history: 是历史的对话信息，包括用户问题和AI回复
        :param message: 是当前用户提问的问题
        :return: 历时对话+当前问题
        """

        # 首先 system_prompt
        messages = [SystemMessage(content=system_prompt)]
        # 然后是历史对话信息
        for item in history:
            # item[0] 是用户问题， item[1] 是AI回复
            messages.append(HumanMessage(content=item[0]))
            messages.append(AIMessage(content=item[1]))
        # 最后是当前用户问题
        messages.append(HumanMessage(content=message))

        return messages


def create_msg(prompt: str, is_user: bool = True, is_system=False) -> dict:
    role = "user" if is_user else "assistant"
    if is_system:
        role = "system"
    return {"role": role, "content": prompt}


def concat_chat_message(system_prompt, history, message):
    # 首先 system_prompt
    messages = [create_msg(system_prompt, False, True)]
    # 然后是历史对话信息
    for item in history:
        # item[0] 是用户问题， item[1] 是AI回复
        messages.append(create_msg(item[0]))
        messages.append(create_msg(item[1], is_user=False))
    # 最后是当前用户问题
    messages.append(create_msg(message))

    return messages


class Chat(object):
    def __init__(self):
        self.configs = config.ConfigParser()
        self.model_name = self.configs.get(key='openai')['chat_model']

    def chat(self, messages, temperature=0.1, max_tokens=1024):
        # engine = "gpt-35-turbo"
        response = openai.ChatCompletion.create(engine=self.model_name,
                                                messages=messages,
                                                temperature=temperature,
                                                max_tokens=max_tokens
                                                )
        return response

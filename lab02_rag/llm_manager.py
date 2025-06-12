# llm_manager.py
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
import time

class LLMManager:
    def __init__(self):
        self.providers = {
            "deepseek": {"model": "deepseek-llm", "type": "ollama"},
            "qwen": {"model": "qwen", "type": "ollama"},
            "gpt-4o": {"model": "gpt-4o", "type": "openai"},
            "llama3": {"model": "llama3", "type": "ollama"}
        }
    
    def get_llm(self, provider_name, **kwargs):
        config = self.providers.get(provider_name)
        if not config:
            raise ValueError(f"Unknown provider: {provider_name}")
        
        if config["type"] == "ollama":
            return Ollama(model=config["model"])
        elif config["type"] == "openai":
            return ChatOpenAI(model=config["model"], **kwargs)
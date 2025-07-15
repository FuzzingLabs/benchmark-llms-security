from openai import OpenAI
import os
import json
import re

OPENROUTER_API_KEY = "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"
OPENAI_API_KEY = "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"

def get_openai_llm_response(content: str, system_prompt: str = "", model: str = "gpt-4o") -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    messages.append({"role": "user", "content": content})

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=1
    )
    
    return completion.choices[0].message.content

def get_openrouter_llm_response(content: str, system_prompt: str = "", model: str = "openai/gpt-4o-2024-05-13") -> str:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    messages = []
    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })
    
    messages.append({
        "role": "user",
        "content": content
    })

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature = 0.1
    )
    return completion.choices[0].message.content

def get_llm_response(content: str, system_prompt: str = "", provider: str = "openai", model: str = None) -> str:
    """
    Dispatches to the correct LLM backend based on provider and model.
    provider: 'openai' or 'openrouter'
    model: model name string
    """
    if provider == "openrouter":
        if not model:
            model = "deepseek/deepseek-r1-distill-llama-70b:free"
        return get_openrouter_llm_response(content, system_prompt, model)
    else:
        if not model:
            model = "gpt-4o"
        return get_openai_llm_response(content, system_prompt, model)


def get_json_llm_response(content: str, system_prompt: str, provider: str = "openai", model: str = None) -> dict:
    """
    Extracts JSON from an LLM response.
    
    Args:
        content: The user prompt to send to the LLM
        system_prompt: Optional system prompt to guide the LLM
        provider: 'openai' or 'openrouter'
        model: model name string
        
    Returns:
        A dictionary parsed from the JSON in the LLM response
    """
    
    # Get the raw response from the LLM
    response = get_llm_response(content, system_prompt, provider, model)
    
    # Try to extract JSON using regex pattern matching
    json_pattern = r'```(?:json)?\s*([\s\S]*?)\s*```'
    match = re.search(json_pattern, response)
    
    if match:
        # Extract the JSON content from the code block
        json_str = match.group(1)
    else:
        # If no code block is found, try to use the entire response
        json_str = response
    
    try:
        # Parse the JSON string into a Python dictionary
        return json.loads(json_str)
    except json.JSONDecodeError:
        # If parsing fails, return an empty dictionary
        return {} 
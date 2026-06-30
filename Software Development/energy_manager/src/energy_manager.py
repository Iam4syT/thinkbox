import json
import asyncio
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv

from semantic_kernel import Kernel, OpenAIChatCompletion


# Load environment variables from .env
load_dotenv()

# -----------------------------
# AI Kernel Setup
# -----------------------------
kernel = Kernel()

# ⚠️ Set your API key here or load from env variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Create a .env with OPENAI_API_KEY=your_key")

# Use a known model string or make it configurable: e.g. OPENAI_MODEL=gpt-4
model = os.getenv("OPENAI_MODEL", "gpt-4")
kernel.add_chat_service("openai", OpenAIChatCompletion(api_key, model))


async def ask_kernel(question: str) -> str:
    """Ask the AI Kernel a question and return the response."""
    try:
        system_message = (
            "You are a top energy management consultant. Your task is to review the user's input and results "
            "and provide accurate and helpful responses about energy consumption and cost calculations."
        )
        kernel.chat("openai").system(system_message)
        completion = await kernel.chat("openai").complete_async(question)
        return completion.message
    except Exception as e:
        return f"Error with AI request: {e}"
    
# ...existing code...
import os
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.openai import OpenAIChatCompletion  # changed import
# ...existing code...

# Load environment variables from .env
load_dotenv()

# -----------------------------
# AI Kernel Setup
# -----------------------------
kernel = Kernel()

# ⚠️ Set your API key here or load from env variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Create a .env with OPENAI_API_KEY=your_key")

# Use a known model string or make it configurable: e.g. OPENAI_MODEL=gpt-4
model = os.getenv("OPENAI_MODEL", "gpt-4")
kernel.add_chat_service("openai", OpenAIChatCompletion(api_key, model))

# reuse a single chat instance
chat = kernel.chat("openai")


async def ask_kernel(question: str) -> str:
    """Ask the AI Kernel a question and return the response."""
    try:
        system_message = (
            "You are a top energy management consultant. Your task is to review the user's input and results "
            "and provide accurate and helpful responses about energy consumption and cost calculations."
        )
        chat.system(system_message)
        completion = await chat.complete_async(question)

        # Robust extraction of assistant text from different completion shapes
        if hasattr(completion, "message"):
            msg = completion.message
            # message may be a string or an object with .content
            if isinstance(msg, str):
                return msg
            if hasattr(msg, "content"):
                return msg.content

        if isinstance(completion, dict):
            try:
                return completion["choices"][0]["message"]["content"]
            except Exception:
                pass

        return str(completion)
    except Exception as e:
        return f"Error with AI request: {e}"


async def ask_kernel_with_data(user_request: str, filename: str = "energy_data.json") -> str:
    """
    Read stored device data from JSON and ask the kernel, embedding the JSON in the prompt.
    Returns assistant text (or error message).
    """
    try:
        try:
            with open(filename, 'r') as f:
                devices_data = json.load(f)
        except FileNotFoundError:
            devices_data = []

        # include the JSON data in the prompt so the model can reason over it
        data_snippet = json.dumps(devices_data, indent=2)
        prompt = (
            f"User request:\n{user_request}\n\n"
            "Stored device data (JSON):\n"
            f"{data_snippet}\n\n"
            "Using the stored device data, answer the user's request. Be concise and reference device names and costs per second when relevant."
        )

        return await ask_kernel(prompt)
    except Exception as e:
        return f"Error preparing request: {e}"


# -----------------------------
# Energy Calculation Functions
# -----------------------------
def cost_of_power_consumption(power_rating: float, cost_per_kwh: float) -> Optional[float]:
    """
    Calculate cost per second of power consumption.
    :param power_rating: Device power in watts
    :param cost_per_kwh: Electricity cost per kWh
    :return: Cost per second
    """
    try:
        energy_consumption_per_second = power_rating / 1000  # convert watts to kWh per second
        cost_per_kwh_per_second = cost_per_kwh / 3600
        cost_per_second = energy_consumption_per_second * cost_per_kwh_per_second
        return round(cost_per_second, 10)
    except Exception as e:
        print(f"Error during calculation: {e}")
        return None


def append_to_json(data: Dict[str, Any], filename: str = "energy_data.json") -> None:
    """Append device data to a JSON file."""
    try:
        try:
            with open(filename, 'r') as file:
                devices_data = json.load(file)
        except FileNotFoundError:
            devices_data = []

        devices_data.append(data)

        with open(filename, 'w') as file:
            json.dump(devices_data, file, indent=4)

    except Exception as e:
        print(f"Error writing to JSON file: {e}")


def calculate_total_cost_from_json(filename: str = "energy_data.json") -> float:
    """Calculate total cost from stored device data."""
    total_cost = 0
    try:
        with open(filename, 'r') as file:
            devices_data = json.load(file)
            for device in devices_data:
                print(f"{device['device']} : {device['cost']} per second")
                total_cost += device["cost"]
    except FileNotFoundError:
        print("No data found. Start by adding some devices.")
    except Exception as e:
        print(f"Error reading from JSON file: {e}")
    return total_cost


# -----------------------------
# Input Helpers
# -----------------------------
def get_float_input(prompt: str) -> float:
    """Get validated float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

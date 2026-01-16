import json
import os
from typing import Any, Dict
from litellm import completion
from dotenv import load_dotenv
load_dotenv()


# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"

def get_itinerary(destination: str) -> Dict[str, Any]:
    """
    Returns a JSON-like dict with keys:
      - destination
      - price_range
      - ideal_visit_times
      - top_attractions
    """
    # implement litellm call here to generate a structured travel itinerary for the given destination

    # See https://docs.litellm.ai/docs/ for reference.

    response = completion(
    model="groq/llama-3.3-70b-versatile", 
    response_format={ "type": "json_object" },
    messages=[
            {
                "role": "system",
                "content": "You are a travel assistant."
            },
            {
                "role": "user",
                "content": (
                    f"Generate a travel itinerary for {destination}. "
                    "Return JSON with exactly these fields: "
                    "destination, price_range, ideal_visit_times (list), top_attractions (list)."
                )
            }
        ],
    )
    # print(response)

    data = json.loads(response.choices[0].message.content)

    return data

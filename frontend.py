from hindsight_client import Hindsight
import os

memory = Hindsight(
    base_url=os.getenv("HINDSIGHT_API_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY")
)

BANK_ID = "shoppulse-production"

def remember_incident(incident_text):
    memory.retain(
        bank_id=BANK_ID,
        content=incident_text,
        context="ShopPulse production incident and engineer-confirmed outcome"
    )

def find_similar_incidents(symptoms):
    result = memory.recall(
        bank_id=BANK_ID,
        query=f"""
        Find historical incidents similar to:
        {symptoms}

        Include root causes, failed fixes,
        successful fixes and confirmed outcomes.
        """
    )
    return [item.text for item in result.results]

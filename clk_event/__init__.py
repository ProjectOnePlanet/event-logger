import os
import logging
import json
from jsonschema import validate, ValidationError

from .schema import schema
import azure.functions as func
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

CONN_STR = os.environ.get("CONN_STR_CLK")
EVENTHUB_NAME = os.environ.get("EVENTHUB_NAME_CLK")


async def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Receives logging payload for PV Events
    Args:
        req: HTTP Request
    Returns:
        func.HttpResponse: JSON data regarding job status
    """
    # Receive payload
    try:
        payload = req.get_json()
        logging.info("Payload Received")
        # Validate Schema
        validate(instance=payload, schema=schema)
    except ValueError:
        logging.error("Payload Empty")
        return func.HttpResponse(
            json.dumps({"status": "failure", "message": "payload not found"}),
            status_code=400,
        )
    except ValidationError:
        logging.error("Payload failed schema validation")
        return func.HttpResponse(
            json.dumps(
                {
                    "status": "failure",
                    "message": "payload schema validation fail"
                }
            ),
            status_code=400,
        )
    # Publsh payload
    try:
        logging.info(f"Publishing to Event Hub: {EVENTHUB_NAME}")
        producer = EventHubProducerClient.from_connection_string(
            conn_str=CONN_STR, eventhub_name=EVENTHUB_NAME
        )
        async with producer:
            event_data_batch = await producer.create_batch()
            event_data_batch.add(EventData(json.dumps(payload)))
            await producer.send_batch(event_data_batch)
            logging.info("Publishing Success")
            return func.HttpResponse(
                json.dumps({"status": "success", "message": ""}),
                status_code=200
            )
    except Exception as e:
        logging.error(f"Error when publishing, Exception: {e}")
        return func.HttpResponse(
            json.dumps(
                {
                    "status": "failure",
                    "message": "error publishing to event hub"
                }
            ),
            status_code=500,
        )

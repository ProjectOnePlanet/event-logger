from pv_event_logger import main
from azure.eventhub.aio import EventHubProducerClient


class mock_http_request:
    def __init__(self):
        pass

    @staticmethod
    def get_json():
        sample_payload = {
            "log_id": "r3fkW-Rg-HRDxlvc_Vp47",
            "timestamp": "2022-03-29T12:39:27.308Z",
            "mills": 1648557567307,
            "ymd": "2022-03-29",
            "hh24miss": "12:39:27",
            "req_msg": {},
            "cookie_id": "",
            "session_id": "",
            "wallet_addr": "terra124kc8vwns6v33af4vvezcsqkukexec0vrlkwhw",
            "wallet_type": 1,
            "wallet_id": "station",
            "chain_id": "bombay-12",
            "chain_name": "testnet",
            "device": 1,
            "page_url": "/launchpad",
            "page_code": "/launchpad",
            "page_id": "/launchpad",
            "content_id": "/launchpad",
            "ref_page_url": "",
            "ref_page_code": "",
            "ref_clk_code": "",
            "ref_shc_kwd": "",
            "event": 3,
            "imp_content": None,
            "clk_content": None
        }
        return sample_payload


class mock_http_request_validation_fail:
    def __init__(self):
        pass

    @staticmethod
    def get_json():
        sample_payload = {
            "log_id": "r3fkW-Rg-HRDxlvc_Vp47",
            "timestamp": "2022-03-29T12:39:27.308Z",
            "mills": "1648557567307"
        }
        return sample_payload


class mock_http_request_empty_payload:
    def __init__(self):
        pass

    @staticmethod
    def get_json():
        raise ValueError


class MockProducer:
    def __init__(self):
        pass

    async def __enter__(self):
        pass

    def create_batch(self, *args, **kwargs):
        return self

    def add(self, *args, **kwargs):
        pass


def mock_send_batch(*args, **kwargs):
    pass


def mock_from_connection_string(*args, **kwargs):
    return EventHubProducerClient


async def test_main_validation_fail():
    response = await main(mock_http_request_validation_fail)
    assert response.status_code == 400


async def test_main_empty_payload():
    response = await main(mock_http_request_empty_payload)
    assert response.status_code == 400

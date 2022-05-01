# event-logger

## API Request

CLK Event: https://logger-oneplanet.azurewebsites.net/api/clk_event [POST]

Schema
```json
{
    "log_id": {"type": "string"},
    "timestamp": {"type": "string"},
    "mills": {"type": "number"},
    "ymd": {"type": "string"},
    "hh24miss": {"type": "string"},
    "req_msg": {},
    "cookie_id": {"type": "string"},
    "session_id": {"type": "string"},
    "wallet_addr": {"type": "string"},
    "wallet_type": {"type": "number"},
    "wallet_id": {"type": "string"},
    "chain_id": {"type": "string"},
    "chain_name": {"type": "string"},
    "device": {"type": "number"},
    "page_url": {"type": "string"},
    "page_code": {"type": "string"},
    "page_id": {"type": "string"},
    "content_id": {"type": "string"},
    "ref_page_url": {"type": "string"},
    "ref_page_code": {"type": "string"},
    "ref_clk_code": {"type": "string"},
    "ref_shc_kwd": {"type": "string"},
    "event": {"type": "number"},
    "imp_content": {},
    "clk_content": {
        "content_type": {"type": "string"},
        "content_id": {"type": "string"},
        "px": {"type": "number"},
        "py": {"type": "number"},
        "sx": {"type": "number"},
        "sy": {"type": "number"}
    }
}
```

PV Event: https://logger-oneplanet.azurewebsites.net/api/clk_event [POST]

Schema
```json
{
    "log_id": {"type": "string"},
    "timestamp": {"type": "string"},
    "mills": {"type": "number"},
    "ymd": {"type": "string"},
    "hh24miss": {"type": "string"},
    "req_msg": {},
    "cookie_id": {"type": "string"},
    "wallet_addr": {"type": "string"},
    "wallet_type": {"type": "number"},
    "wallet_id": {"type": "string"},
    "chain_id": {"type": "string"},
    "chain_name": {"type": "string"},
    "device": {"type": "number"},
    "page_url": {"type": "string"},
    "page_code": {"type": "string"},
    "page_id": {"type": "string"},
    "content_id": {"type": "string"},
    "ref_page_url": {"type": "string"},
    "ref_page_code": {"type": "string"},
    "ref_clk_code": {"type": "string"},
    "ref_shc_kwd": {"type": "string"},
    "event": {"type": "number"},
    "imp_content": {},
    "clk_content": {},
}
```
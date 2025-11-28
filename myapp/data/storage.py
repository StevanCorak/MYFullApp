import json
import os
import uuid
from datetime import datetime
from myapp.data.models import DistributionRecord

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fuel_distribution_data.json')

def _load_data() -> list[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def _save_data(records: list[dict]):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(records, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Greška prilikom spremanja podataka u {DATA_FILE}: {e}")

def get_all_records() -> list[DistributionRecord]:
    return [DistributionRecord(**r) for r in _load_data()]

def add_record(location: str, fuel_type: str, quantity: float) -> DistributionRecord:
    new_record = DistributionRecord(
        record_id=str(uuid.uuid4()),
        location=location,
        fuel_type=fuel_type,
        quantity_liters=quantity,
        timestamp=datetime.now().isoformat()
    )

    raw_records = _load_data()
    raw_records.append(new_record.__dict__)
    _save_data(raw_records)

    return new_record

def delete_record(record_id: str) -> bool:
    raw_records = _load_data()
    initial_count = len(raw_records)
    
    updated_records = [r for r in raw_records if r.get('record_id') != record_id]
    
    if len(updated_records) < initial_count:
        _save_data(updated_records)
        return True
    return False

import json
import os
import uuid
from datetime import datetime
from myapp.data.models import DistributionRecord

# Fiksni naziv datoteke za pohranu podataka unutar myapp/data direktorija
# Apsolutna putanja osigurava da aplikacija radi bez obzira na radni direktorij
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fuel_distribution_data.json')

def _load_data() -> list[dict]:
    """Učitava sve zapise iz JSON datoteke."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Ako datoteka postoji, ali je prazna ili neispravna, vraćamo praznu listu
        return []

def _save_data(records: list[dict]):
    """Sprema listu zapisa u JSON datoteku."""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            # Koristimo indentaciju za lakšu čitljivost
            json.dump(records, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Greška prilikom spremanja podataka u {DATA_FILE}: {e}")

def get_all_records() -> list[DistributionRecord]:
    """Dohvaća sve zapise i vraća ih kao listu DistributionRecord objekata."""
    raw_records = _load_data()
    return [DistributionRecord(**r) for r in raw_records]

def add_record(location: str, fuel_type: str, quantity: float) -> DistributionRecord:
    """Dodaje novi zapis u pohranu."""
    # Stvaranje novog ID-a i vremena
    new_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    new_record = DistributionRecord(
        record_id=new_id,
        location=location,
        fuel_type=fuel_type,
        quantity_liters=quantity,
        timestamp=timestamp
    )

    # Učitavanje, dodavanje i spremanje
    raw_records = _load_data()
    raw_records.append(new_record.__dict__)
    _save_data(raw_records)

    return new_record

def delete_record(record_id: str) -> bool:
    """Briše zapis po ID-u."""
    raw_records = _load_data()
    initial_count = len(raw_records)
    
    # Filtriranje liste, zadržavamo samo one zapise čiji ID ne odgovara
    updated_records = [r for r in raw_records if r.get('record_id') != record_id]
    
    if len(updated_records) < initial_count:
        # Zapis je pronađen i obrisan
        _save_data(updated_records)
        return True
    return False # Zapis nije pronađen
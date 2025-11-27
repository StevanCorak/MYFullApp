from myapp.data import storage
from myapp.data.models import DistributionRecord
from collections import defaultdict
from typing import Dict, Any

def get_distribution_data() -> list[DistributionRecord]:
    """Dohvaća sve zapise o distribuciji."""
    return storage.get_all_records()

def record_distribution(location: str, fuel_type: str, quantity: float) -> DistributionRecord:
    """Bilježi novi događaj distribucije."""
    if quantity <= 0:
        raise ValueError("Količina goriva mora biti pozitivna.")
    return storage.add_record(location, fuel_type, quantity)

def get_summary_statistics() -> Dict[str, Any]:
    """Izračunava sažetu statistiku o raspodjeli goriva."""
    records = get_distribution_data()
    
    total_quantity = sum(r.quantity_liters for r in records)
    
    # Ukupna količina po vrsti goriva
    quantity_by_type = defaultdict(float)
    # Broj zapisa po vrsti goriva
    count_by_type = defaultdict(int)
    
    for r in records:
        quantity_by_type[r.fuel_type] += r.quantity_liters
        count_by_type[r.fuel_type] += 1

    # Formatiranje za lakši prikaz
    formatted_quantities = {
        k: f"{v:.2f} L" 
        for k, v in dict(quantity_by_type).items()
    }
    
    return {
        "total_records": len(records),
        "total_distributed_liters": f"{total_quantity:.2f} L",
        "quantity_by_type": formatted_quantities,
        "count_by_type": dict(count_by_type),
        "last_update": storage.get_all_records()[-1].timestamp if records else "Nema zapisa"
    }

def remove_distribution_record(record_id: str) -> bool:
    """Briše zapis po ID-u."""
    return storage.delete_record(record_id)
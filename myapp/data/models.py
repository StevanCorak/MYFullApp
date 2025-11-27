
from dataclasses import dataclass
from typing import Literal

# Definicija dozvoljenih tipova goriva
FuelType = Literal["Benzin", "Dizel", "Autoplin", "Električno"]

@dataclass
class DistributionRecord:
    """
    Model za jedan zapis o distribuciji goriva.
    """
    record_id: str
    location: str          # Lokacija distribucije (npr. 'Zagreb', 'Postaja A')
    fuel_type: FuelType    # Vrsta goriva
    quantity_liters: float # Količina u litrama
    timestamp: str         # Vrijeme zapisa (ISO format)
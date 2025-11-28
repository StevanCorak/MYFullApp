
from dataclasses import dataclass
from typing import Literal

FuelType = Literal["Benzin", "Dizel", "Autoplin", "Električno"]

@dataclass
class DistributionRecord:
  
    record_id: str
    location: str          
    fuel_type: FuelType     
    quantity_liters: float 
    timestamp: str         
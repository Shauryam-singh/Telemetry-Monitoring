from dataclasses import dataclass
from datetime import datetime

@dataclass
class TelemetryPoint:
    timestamp: datetime
    voltage: float
    load: float
    temperature: float

@dataclass
class SubStation:
    id: str
    name: str
    data: list
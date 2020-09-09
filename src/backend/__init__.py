from src.backend.cpu_query import CPUQuery
from src.backend.gpu_query import GPUQuery
from src.backend.hardware_query import HardwareQuery
from src.backend.mock_query import MockQuery
from src.backend.ram_query import RAMQuery
from src.backend.sensors_query import SensorsQuery

__all__ = [CPUQuery, GPUQuery, HardwareQuery, MockQuery, RAMQuery,
           SensorsQuery]

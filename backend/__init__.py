from backend.cpu_query import CPUQuery
from backend.gpu_query import GPUQuery
from backend.hardware_query import HardwareQuery
from backend.mock_query import MockQuery
from backend.ram_query import RAMQuery
from backend.sensors_query import SensorsQuery

__all__ = [CPUQuery, GPUQuery, HardwareQuery, MockQuery, RAMQuery,
           SensorsQuery]

# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from typing import Optional, Tuple, Union, Dict, Any
import ctypes
from .. import device as _device

def is_available() -> bool: ...
def init() -> None: ...
def _lazy_call(callable) -> None: ...

class cudaStatus:
    SUCCESS: int
    ERROR_NOT_READY: int

class CudaError:
    def __init__(self, code: int) -> None: ...

class _CudaDeviceProperties:
    name: str
    major: int
    minor: int
    multi_processor_count: int
    total_memory: int
    is_integrated: int
    is_multi_gpu_board: int

_device_t = Union[_device, int, str]

def check_error(res: int) -> None: ...
def device_count() -> int: ...
def empty_cache() -> None: ...
def synchronize(device: _device_t) -> None: ...
def set_device(device: _device_t) -> None: ...
def get_device_capability(device: Optional[_device_t]=...) -> Tuple[int, int]: ...
def get_device_name(device: Optional[_device_t]=...) -> str: ...
def get_device_properties(device: _device_t) -> _CudaDeviceProperties: ...
def current_device() -> int: ...
def manual_seed(seed: int) -> None: ...
def memory_allocated(device: Optional[_device_t]=...) -> int: ...
def max_memory_allocated(device: Optional[_device_t]=...) -> int: ...
def reset_max_memory_allocated(device: Optional[_device_t]=...) -> None: ...
def memory_cached(device: Optional[_device_t]=...) -> int: ...
def max_memory_cached(device: Optional[_device_t]=...) -> int: ...
def reset_max_memory_cached(device: Optional[_device_t]=...) -> None: ...
def cudart() -> ctypes.CDLL: ...
def find_cuda_windows_lib() -> Optional[ctypes.CDLL]: ...
#MODIFIED BY TORCHGPIPE
from .. import ByteTensor
def set_rng_state(new_state: ByteTensor, device: _device_t = ...) -> None: ...
def get_rng_state(device: _device_t = ...) -> ByteTensor: ...
#END

#MODIFIED BY TORCHGPIPE
from typing import Any
class device:
    def __init__(self, device: _device_t = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> None: ...

class Stream:
    device: _device
    def __init__(self, device: _device_t = ..., priority: int = ...) -> None: ...
    def synchronize(self) -> None: ...
    def wait_stream(self, stream: Stream) -> None: ...

class stream:
    def __init__(self, stream: Optional[Stream] = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> None: ...

def current_stream(device: Optional[_device_t]) -> Stream: ...
def default_stream(device: Optional[_device_t]) -> Stream: ...
#END
#
default_generators: Tuple[Any]

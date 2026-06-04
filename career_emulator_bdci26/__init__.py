"""Career Emulator BDCI 2026 competition dataset package."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("career_emulator_bdci26")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["__version__"]

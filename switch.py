from dataclasses import dataclass

@dataclass(repr=True, init=True)
class Switch:
    switch_name: str
    switch_ip: str
    port: int = 22


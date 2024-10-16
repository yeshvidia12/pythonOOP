import module_base
from typing import Union

class _B:
    def __init__(self, base:module_base.Base):
        self.base = base
    
    def foob(self):
        print(f"foob on {self.base.name }")


class B:
    b:_B

def add_b(base:module_base.Base) -> Union[B, module_base.Base]:
    base.b = _B(base)
    return base


        

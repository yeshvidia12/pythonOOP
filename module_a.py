import module_base
from typing import Union

class _A:
    def __init__(self, base:module_base.Base):
        self.base = base
    
    def fooa(self):
        print(f"fooa on {self.base.name }")


class A:
    a:_A

def add_a(base:module_base.Base) -> Union[A, module_base.Base]:
    base.a = _A(base)
    return base


        

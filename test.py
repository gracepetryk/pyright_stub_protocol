from .typings.stub import SupportsSomething as SupportsSomething_stub
from .something_protocol import SupportsSomething as SupportsSomething_py


# no error raised
class ImplementsSomethingFromStub(SupportsSomething_stub):
    pass


# error raised as expected
class ImplementsSomethingFromPy(SupportsSomething_py):
    pass

from hik_app.models.base.table import Table, AutoFiledName
from hik_app.models.base.fields import *

class SystemResource(Table):
    __metaclass__ = AutoFiledName

    rowname = 'sysResourceInfo'
    Chassis = UintField()
    Slot = UintField()
    CPUID = UintField()
    BoardType = UintField()
    CPUUsage = UintField()
    Last1mCPUUsage = UintField()
    Last5mCPUUsage = UintField()
    TotalMem = UintField()
    UsedMem = UintField()
    FreeMem = UintField()
    FreeMemRatio = UintField()
    MemUsage = UintField()

if __name__ == "__main__":
    s = SystemResource()
    print(type(s.Chassis))
    s.Chassis = 1
    print(type(s.Chassis))
    s.buildFromXml('xxx')
    s.toXml()


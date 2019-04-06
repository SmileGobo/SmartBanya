import enum
from typing import List


class Base:

    class Type(enum.IntEnum):
        ShowFrame  = 0x1
        ShowColumn = 0x2
        LoadColumn = 0x3
        LoadFrame  = 0x4
        SetBrghtnss= 0x5
    
    Code:       int = 0
    Length:     int = 0
    Marker:     int = 0x55
    Broadcast:  bool = False

    def __init__(self, addr: int = 0, data:List[int] = []):
        """
            Создание команды, адрес может отсуствовать(команды: показ кадра и показ столбца)
        """
        if addr > 0x70:
            raise RuntimeError('addr not in range 0 <= addr <= 0x70')
        
        self._addr = addr
        self._data = data


    def pack(self):
        rslt = [self.Marker, secondByte( self.Code, self._addr)] #TODO адрес 5 бит 3 код
        #длинна не добалвятся к широковещательным коммандам
        if self.Broadcast:
            rslt.append(self.Length)
            rslt += self._data
        return bytes(rslt)
    
def secondByte(code, addr):
    if 0 == addr: 
        return code
    return code |(addr << 3)   

def defineCommand(code, size = 0, broadcast: bool = False):
    class Impl(Base):
        Code = code
        Size = size
        BroadCast = broadcast
    return Impl

class LoadFrame(defineCommand(Base.Type.LoadFrame, size = 35)):
    pass

class LoadColumn(defineCommand(Base.Type.LoadColumn, size = 4)):
    pass

'''    
class ShowFrame(Base):
    Code = Base.ShowFrame
    def __init__ (self):
        super().__init__()

class ShowColumn(Base):
    Code = 

'''

ShowFrame = defineCommand(Base.Type.ShowFrame, 2, True)
ShowColumn = defineCommand(Base.Type.ShowColumn, 2, True)
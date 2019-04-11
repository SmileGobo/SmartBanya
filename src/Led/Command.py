import enum
from typing import List


class Base:

    class Type(enum.IntEnum):
        ShowFrame  = 0x1
        ShowColumn = 0x2
        LoadColumn = 0x3
        LoadFrame  = 0x4
        SetBrghtnss= 0x5
    
    _сode:       int = 0
    _length:     int = 0
    _broadcast:  bool = False    

    def __init__(self, addr: int = 0, data:List[int] = []):
        """
            Создание команды, адрес может отсуствовать(команды: показ кадра и показ столбца)
        """
        if addr > 0x70:
            raise RuntimeError('addr not in range 0 <= addr <= 0x70')
        
        self._addr = addr
        self._data = data

    def _checkData(self):
        pass
    
    def pack(self):
        rslt = [self.Marker(), secondByte( self.Code, self._addr)] #TODO адрес 5 бит 3 код
        #длинна не добалвятся к широковещательным коммандам
        if not self.Broadcast:
            rslt.append(self.Length)
            self._checkData()
            rslt += self._data
        
        assert self.Length == len(rslt), 'invalid size defined'
        return bytes(rslt)
    
    @property
    def Code(self) -> int:
        return self._code
    
    @staticmethod
    def Marker() -> int:
        return 0x55

    @property
    def Broadcast(self):
        return self._broadcast

    @property
    def Length(self):
        return self._length

def secondByte(code, addr):
    if 0 == addr: 
        return code
    return code |(addr << 3)   

def defineCommand(code: int, length: int = 0, broadcast: bool = False):
    class Impl(Base):
        _code = code
        _length = length
        _broadcast = broadcast
    return Impl

class LoadFrame(defineCommand(Base.Type.LoadFrame, length = 35)):
    pass

class LoadColumn(defineCommand(Base.Type.LoadColumn, length = 4)):
    def __init__(self, addr):
        super().__init__(addr)

    def _checkData(self):
        if len(self._data) == 0:
            raise RuntimeError('LoadColumn need setup col')
    
    def setColumn(self, val: int):
        self._data = [val]

ShowFrame  = defineCommand(Base.Type.ShowFrame,   length = 2, broadcast = True)
ShowColumn = defineCommand(Base.Type.ShowColumn,  length = 2, broadcast = True)
import enum

class Base:

    class Type(enum.IntEnum):
        ShowFrame  = 0x1
        ShowColumn = 0x2
        LoadColumn = 0x3
        LoadFrame  = 0x4
        SetBrghtnss= 0x5
    
    Code = 0
    Length = 0
    Marker = 0x55

    def __init__(self, addr = 0, data = []):
        if addr > 0x70:
            raise RuntimeError('addr not in range 0 <= addr <= 0x70')
        
        self._addr = addr
        self._data = data


    def pack(self):
        rslt = [self.Marker, secondByte( self.Code, self._addr)] #TODO адрес 5 бит 3 код
        if 0 != self.Length and 0 != self._addr:
            rslt.append(self.Length)
            rslt += self._data
        return bytes(rslt)
    
def secondByte(code, addr):
    if 0 == addr: 
        return code
    return code |(addr << 3)   

def defineCommand(code, len = 0):
    class Impl(Base):
        Code = code
        Length = len
    return Impl

class LoadFrame(defineCommand(Base.Type.LoadFrame, len = 35)):
    pass

class LoadColumn(defineCommand(Base.Type.LoadColumn, len = 4)):
    pass

'''    
class ShowFrame(Base):
    Code = Base.ShowFrame
    def __init__ (self):
        super().__init__()

class ShowColumn(Base):
    Code = 

'''

ShowFrame = defineCommand(Base.Type.ShowFrame)
ShowColumn = defineCommand(Base.Type.ShowColumn)
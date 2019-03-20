import Command

def ShowFrame ():
    return [Command.Base.Marker, Command.Base.ShowFrame]

def ShowColumn():
    return [Command.Base.Marker, Command.Base.ShowColumn]

def LoadFrame(addr, data):
    return [
        Command.Base.Marker,
        Command.secondByte(Command.Base.LoadFrame, addr),
        Command.LoadFrame.Length
    ] + data

def LoadColumn(addr, col, val):
    return [
        Command.Base.Marker, 
        Command.secondByte(Command.Base.LoadColumn, addr),
        Command.LoadColumn.Length,
        val
    ]



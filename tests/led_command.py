import unittest
import Led.Command as Commands
class Command(unittest.TestCase):
    _addr: int = 0
    def setUp(self):
        self._addr = 3

    def test_LoadColumn(self):
        cmd = Commands.LoadColumn(self._addr)
        self.assertEqual(cmd.Code, Commands.Base.Type.LoadColumn)
        with self.assertRaises(RuntimeError):
            cmd.pack()

        cmd.setColumn(8)   
        rslt = cmd.pack()
        self.assertEqual(len(rslt), cmd.Length)
        self.assertEqual(rslt[0], Commands.Base.Marker())
        self.assertEqual(rslt[1] & 0x3, cmd.Code)
        

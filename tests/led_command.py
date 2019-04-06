import unittest
import Led.Command as Commands
class Command(unittest.TestCase):
    def test_LoadColumn(self):
        cmd = Commands.LoadColumn()
        self.assertEqual(cmd.Code, Commands.Base.Type.LoadColumn)

        rslt = cmd.pack()
        self.assertEqual(len(rslt), cmd.Size)
        self.assertEqual(rslt[0], Commands.Base.Marker)
        self.assertEqual(rslt[1], cmd.Code)
        

import importlib.util,pathlib,unittest
p=pathlib.Path(__file__).resolve().parents[1]/"portfoliokit.py"
s=importlib.util.spec_from_file_location("tool",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def test_main_exists(self): self.assertTrue(callable(m.main))
if __name__=="__main__":unittest.main()

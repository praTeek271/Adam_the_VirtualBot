# create a file which will setup the phinex program to be ready to run on a single click.

import os
import importlib.util
import sys
class setup_invr:

    def __init__(self):
        self.modules_to_be_used=['pyttsx3','sockets','SpeechRecognition','PyAudio']

    def install(self):

        for module in self.modules_to_be_used:
            name=module
            if name in sys.modules:
                print(f"{name!r} already in sys.modules")
            elif (spec := importlib.util.find_spec(name)) is not None:
                module = importlib.util.module_from_spec(spec)
                sys.modules[name] = module
                spec.loader.exec_module(module)
                print(f"------------------>     {name!r} has been installed")
            else:
                print(f"can't find the {name!r} module")

                try:
                    print(f"Trying to install the {name} module.")
                    os.system(f'pip install {name}')
                except:
                    print("------------------>     Try installing {name} module manually.")



# obj=setup_invr()
# obj.install()
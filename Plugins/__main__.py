import glob
from pathlib import Path
from Plugins.utils import load_mahoaga
import logging
from Plugins import Meyit47

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Plugins/mahoaga/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_mahoaga(plugin_name.replace(".py", ""))
    
print("Bot başarıyla başlatıldı!")
print("Kanal ziyareti @MytGrupBotLog")

if __name__ == "__main__":
    Meyit47.run_until_disconnected()

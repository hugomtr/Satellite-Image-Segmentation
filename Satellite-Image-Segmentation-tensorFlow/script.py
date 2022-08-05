import shutil
import random

for i in range(267):
    if i in [196,97,98,199]:
        continue

    if random.uniform(0,1) < 0.8:
        shutil.move("Input/images/{}".format(str(i)),"Synthese/Train/images/{}".format(str(i)))
        shutil.move("synthese/masks/{}".format(str(i)),"Synthese/Train/masks/{}".format(str(i)))
    else:
        shutil.move("synthese/images/{}".format(str(i)),"Synthese/Valid/images/{}

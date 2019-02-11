from .rocket import Rocket
from .yellow_laser import YellowLaser

# добавляем лазер в список 3 раза, чтобы увеличить шанс спавна именно этого объекта
OBSTACLES = [Rocket, YellowLaser, YellowLaser, YellowLaser]

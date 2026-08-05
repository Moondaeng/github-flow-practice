from work import Work
from homecoming import HomeComing

man = Work(20)

energy = man.working(15)

man = HomeComing(energy)

man.go_home()

print(man.energy)
def G(t):
   Table=""

   for i in range (1,11):
      Table+=(f"{t} X {i} = {t*i}\n")

   with open(f"Tables/Table_{t}.txt","w") as f:
      f.write(Table)

for i in range (2,11):
   G(i)

    
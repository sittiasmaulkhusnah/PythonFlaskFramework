import numpy
import pandas
import matplotlib.pyplot as plt

# contoh numpy
array = numpy.array([1,2,3,4,5])
print(array, type(array))

# contoh pandas
df = pandas.DataFrame({'nama': ['usna','asmaul','nana'], 'nilai': [100,90,85]})
print(df, type(df))

# contoh matplotlib
nama = ['usna','asmaul','nana']
nilai = [100,90,85]
plt.bar(x=nama, height=nilai)
plt.show()

print('\n'.join
 ([''.join
   ([('Engineer'[(x-y)%8 ]
     if((x*0.05)**2+(y*0.1)**2-1)
      **3-(x*0.05)**2*(y*0.1)
       **3<=0 else' ')
        for x in range(-37,37)])
         for y in range(25,-25,1)]))
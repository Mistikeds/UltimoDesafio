from App_Desafio.models import familiar



familiar(nombre="Rosario",apellido="mendez", direccion="Rio Parana 358", documento=123123, fecha_nacimiento="1999-12-26",email="johan_romero@hotmail.com",).save()
familiar(nombre="Alberto",apellido="quiste", direccion="Rio Uruguay 75",  documento=890890, fecha_nacimiento="1912-12-10",email="johan@hotmail.com",).save()
familiar(nombre="Samuel",apellido="criet", direccion="Rio Parana 745", documento=345345, fecha_nacimiento="1925-12-26",email="nahuel@hotmail.com",).save()
familiar(nombre="Florencia",apellido="balon", direccion="Rio Parana 1582", documento=567567, fecha_nacimiento="1932-12-16",email="romero@hotmail.com",).save()

print("Se cargo con éxito los usuarios de pruebas")
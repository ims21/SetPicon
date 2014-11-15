from distutils.core import setup
import setup_translate

<<<<<<< HEAD
pkg = 'Extensions.AnalogClock'
setup (name = 'enigma2-plugin-extensions-analogclock',
       version = '1.08',
       description = 'analog clock on the screen',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*.png', 'locale/*/LC_MESSAGES/*.mo']},
=======
pkg = 'Extensions.SetPicon'
setup (name = 'enigma2-plugin-extensions-setpicon',
       version = '0.44',
       description = 'work with services picons',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*.xml', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
>>>>>>> 4de93d21503aeac6b4512dc517af824ff73e5db1
       cmdclass = setup_translate.cmdclass, # for translation
      )

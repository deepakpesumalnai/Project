from TopMod import Function_top as top
from DownMod import Function_down
from Directory.directorymodule import Function_dir
from Directory.directorymodule2 import Function_dir2
from Directory.sub_directory.sub_script import Function_subdir
from Directory.sub_package.sub_package import Function_subpackage
from Directory.MyPackage import package_file1 as p1
from Directory.MyPackage.package_file2 import package2
from Directory.MyPackage import package_file3 as p3
from Directory.MyPackage import multiple_function as m

from Directory.MyPackage_withoutinit.package_file1 import package1
from Directory.MyPackage_withoutinit.package_file2 import package2
from Directory.MyPackage_withoutinit.package_file3 import package1 as pw3


top()
Function_down()
Function_dir()
Function_dir2()
Function_subdir()
Function_subpackage()
p1.package1()
package2()
p3.package1()
m.multiple1()
m.multiple2()
m.multiple3()
package1()
package2()
pw3()
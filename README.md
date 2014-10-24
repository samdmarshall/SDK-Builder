#SDK Builder Script

This is a python script that will build and SDK bundle for Xcode that will appear in the drop-down under build settings. Additional resources are added by creating a SDK template directory with an SDKSettings.plist (see the included sample and [this project](https://github.com/samdmarshall/OSXPrivateSDK) to see how it is done).

###Usage:
	$ python usage: SDKBuilder.py [-h] -s SDK [-u] [-f] [-v]

		required arguments:
		  	-s SDK, --sdk SDK  path to sdk template to build
		  			
		optional arguments:
  			-h, --help         show this help message and exit
  			-u, --update       update sdk from template
 	 		-f, --force        force action
  			-v, --verbose      add verbosity

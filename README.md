[![Build Status](https://travis-ci.com/trydirect/modx.svg?branch=master)](https://travis-ci.com/trydirect/modx)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/modx.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/modx.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/modx.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/modx.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)

# MODX
The MODX Digital Experience Platform gives you complete control over your creative vision and the experiences you deliver. Have peace of mind that your sites will be easily maintained, delivered with unparalleled performance and security, and that if you need help along the way, it’s there.

# Installation

First off, download MODX and extract the files to your server. In the setup/ directory, copy the file "config.dist.new.xml" and rename it to "config.xml". MODX will automatically look for the setup/config.xml file during installation. You can move it outside of the setup/ directory (and the MODX webroot, if you choose), and specify its location with the "--config=/path/to/config.xml" argument.

Next, edit the XML file and set the appropriate database information, MODX paths, and other configuration parameters, and then in your command line prompt, browse to the MODX setup/ directory, and type:

```
$ php ./index.php --installmode=new
```
MODX will proceed to install, and when finished will display the time it took to run the installation, as well as any errors that occurred (which will also be logged in an install log file in core/cache/logs/).

Note : if your core folder is in a "non-standard" location, you might want to use:
```
$ --core_path=/path/to/core/
```
# Basic Upgrade

Follow the same steps as new installations, but this time in your XML file you need only specify the following attributes:
- inplace
- unpacked
- language
- remove_setup_directory

And any other attributes you would like to change during the upgrade. There is an example upgrade xml file named "config.dist.upgrade.xml". Then, once you are ready, browse to the MODX setup directory, and type:
```
$ php ./index.php --installmode=upgrade
```
This will upgrade your MODX installation, and when finished will display the time it took to run the installation, as well as any errors that occurred (which will also be logged in an install log file in core/cache/logs/).

# Advance Upgrade

Follow the same steps as basic upgrade, but this time in your XML file you need all the attributes included in the config.dist.upgrade-advanced.xml file, as all can be changed in an advanced upgrade.

Then, once you are ready, browse to the MODX setup directory, and type:
```
$ php ./index.php --installmode=upgrade-advanced
```
This will upgrade your MODX installation, and when finished will display the time it took to run the installation, as well as any errors that occurred (which will also be logged in an install log file in core/cache/logs/).

# Deployment
Deploy MODX with docker-compose.yml

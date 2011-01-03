#
# $Id$
# $URL$
#

PYTHON=`which python`
DESTDIR=/var/tmp/testinst
PROJECT=fbrehm-libs
BUILDIR=$(CURDIR)/debian/python-$(PROJECT)
VERSION=0.1.1

all:
	@echo "make source - Create source package"
	@echo "make install - Install on local system"
	@echo "make buildrpm - Generate a rpm package"
	@echo "make builddeb - Generate a deb package"
	@echo "make clean - Get rid of scratch and byte files"

source:
	$(PYTHON) setup.py sdist $(COMPILE)



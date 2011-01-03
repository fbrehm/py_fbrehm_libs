#
# $Id$
# $URL$
#

PYTHON=$(shell which python )
DESTDIR=/var/tmp/testinst
PROJECT=$(shell cat setup.py | grep 'name[ 	]*=' | sed -e "s/.*=[ 	]*'//" -e "s/'.*//" )
BUILDIR=$(CURDIR)/debian/python-$(PROJECT)
VERSION=$(shell cat setup.py | grep version | sed -e "s/.*=[ 	]*'//" -e "s/'.*//" )
WWW_DOCROOT=/var/www/localhost/htdocs/projects/$(PROJECT)
ARCHIVE=$(PROJECT)-$(VERSION).tar.gz

all:
	@echo "make source - Create source package"
	@echo "make install - Install on local system"
	@echo "make builddeb - Generate a deb package"
	@echo "make clean - Get rid of scratch and byte files"

source:
	$(PYTHON) setup.py sdist $(COMPILE)
	@echo "Archive: '$(ARCHIVE)'"
	cd dist && md5sum  $(ARCHIVE) >$(ARCHIVE).md5 && sha1sum  $(ARCHIVE) >$(ARCHIVE).sha1 && cd ..
	mkdir -p $(WWW_DOCROOT)
	cp -pv dist/$(ARCHIVE)* $(WWW_DOCROOT)

install:
	$(PYTHON) setup.py install --root $(DESTDIR) $(COMPILE)

builddeb:
	# build the source package in the parent directory
	# then rename it to project_version.orig.tar.gz
	$(PYTHON) setup.py sdist $(COMPILE) --dist-dir=../ --prune
	mv -v ../$(PROJECT)-$(VERSION).tar.gz ../python-$(PROJECT)_$(VERSION).orig.tar.gz
	# build the package
	#dpkg-buildpackage -i -I -rfakeroot

clean:
	$(PYTHON) setup.py clean
	$(MAKE) -f $(CURDIR)/debian/rules clean
	rm -rf build/ MANIFEST
	find . -name '*.pyc' -delete


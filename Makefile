SCRIPTS := $(wildcard *.sh *.py *.rb)
TARGETS := $(addprefix ~/bin/,$(basename $(notdir $(SCRIPTS))))

install: | $(TARGETS)
.PHONY: install

~/bin/%: | %.py
	ln -s $(PWD)/$| $@

~/bin/%: | %.rb
	ln -s $(PWD)/$| $@

~/bin/%: | %.sh
	ln -s $(PWD)/$| $@

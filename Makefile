SCRIPTS := $(wildcard *.sh *.py *.rb)
TARGETS := $(addprefix ~/bin/,$(basename $(notdir $(SCRIPTS))))

default: $(TARGETS)

~/bin/%: | %.py
	echo ln -s $(PWD)/$?.py $@

~/bin/%: | %.rb
	echo ln -s $(PWD).rb $@

~/bin/%: | %.sh
	echo ln -s $(PWD).sh $@

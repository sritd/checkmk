MONITORING_PLUGINS := monitoring-plugins
MONITORING_PLUGINS_VERS := 2.2
MONITORING_PLUGINS_DIR := $(MONITORING_PLUGINS)-$(MONITORING_PLUGINS_VERS)

MONITORING_PLUGINS_BUILD := $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS_DIR)-build
MONITORING_PLUGINS_INSTALL := $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS_DIR)-install
MONITORING_PLUGINS_PATCHING := $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS_DIR)-patching

.PHONY: $(MONITORING_PLUGINS) $(MONITORING_PLUGINS)-install $(MONITORING_PLUGINS)-skel $(MONITORING_PLUGINS)-build

$(MONITORING_PLUGINS): $(MONITORING_PLUGINS_BUILD)

$(MONITORING_PLUGINS)-install: $(MONITORING_PLUGINS_INSTALL)

MONITORING_PLUGINS_CONFIGUREOPTS := \
    --prefix=$(OMD_ROOT) \
    --libexecdir=$(OMD_ROOT)/lib/nagios/plugins

$(MONITORING_PLUGINS_BUILD): $(MONITORING_PLUGINS_PATCHING)
	cd $(MONITORING_PLUGINS_DIR) ; ./configure $(MONITORING_PLUGINS_CONFIGUREOPTS)
	$(MAKE) -C $(MONITORING_PLUGINS_DIR) all
	$(TOUCH) $@

$(MONITORING_PLUGINS_INSTALL): $(MONITORING_PLUGINS_BUILD)
	$(MAKE) DESTDIR=$(DESTDIR) -C $(MONITORING_PLUGINS_DIR) install
	# FIXME: pack these with SUID root
	install -m 755 $(MONITORING_PLUGINS_DIR)/plugins-root/check_icmp $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	install -m 755 $(MONITORING_PLUGINS_DIR)/plugins-root/check_dhcp $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	ln -s check_icmp $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins/check_host

	# Copy package documentations to have these information in the binary packages
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/doc/$(MONITORING_PLUGINS)
	for file in ACKNOWLEDGEMENTS AUTHORS CODING COPYING FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS ; do \
	   install -m 644 $(MONITORING_PLUGINS_DIR)/$$file $(DESTDIR)$(OMD_ROOT)/share/doc/$(MONITORING_PLUGINS); \
	done
	$(TOUCH) $@

$(MONITORING_PLUGINS)-skel:

$(MONITORING_PLUGINS)-clean:
	$(RM) -r $(MONITORING_PLUGINS_DIR) $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS)*

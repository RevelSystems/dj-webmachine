# -*- coding: utf-8 -
#
# This file is part of dj-apipoint released under the Apache 2 license. 
# See the NOTICE for more information.


import os

if os.environ.get('release') != "true":

    minor_tag = ""
    try:
        from apipoint.util import popen3

        stdin, stdout, stderr = popen3("git rev-parse --short HEAD --")
        error = stderr.read()
        if not error:
            git_tag = stdout.read()[:-1]
            minor_tag = ".%s-git" % git_tag
    except OSError:        
        pass
else:
    minor_tag = ""
    

version_info = (0, 1, "0%s" % minor_tag)
__version__ = ".".join(map(str, version_info))


try:
    from apipoint.sites import ApiSite, api_site
except ImportError:
    import traceback
    traceback.print_exc()

def autodiscover():
    """
    Auto-discover INSTALLED_APPS resource.py modules and fail silently when
    not present. This forces an import on them to register any resource bits they
    may want.
    """

    import copy
    from django.conf import settings
    from django.utils.importlib import import_module
    from django.utils.module_loading import module_has_submodule

    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        # Attempt to import the app's resource module.
        try:
            before_import_registry = copy.copy(api_site._registry)
            import_module('%s.resource' % app)
        except:
            api_site._registry = before_import_registry
            if module_has_submodule(mod, 'resource'):
                raise
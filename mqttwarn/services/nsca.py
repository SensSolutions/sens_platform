#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = 'Jan-Piet Mens <jpmens()gmail.com>'
__copyright__ = 'Copyright 2014 Jan-Piet Mens'
__license__   = """Eclipse Public License - v 1.0 (http://www.eclipse.org/legal/epl-v10.html)"""

HAVE_NSCA = True
try:
    import pynsca                     # https://pypi.python.org/pypi/pynsca
    from pynsca import NSCANotifier
except ImportError:
    HAVE_NSCA = False

def plugin(srv, item):

    srv.logging.debug("*** MODULE=%s: service=%s, target=%s", __file__, item.service, item.target)

    if HAVE_NSCA == False:
        return False

    config   = item.config

    statii = [ pynsca.OK, pynsca.WARNING, pynsca.CRITICAL, pynsca.UNKNOWN ]
    status = pynsca.OK
    try:
        prio = item.priority
        status = statii[prio]
    except:
        pass

    nsca_host = config['nsca_host']

    host_name = item.addrs[0]
    service_description = item.addrs[1]

    # If the incoming payload has been transformed, use that,
    # else the original payload
    text = item.message

    try:
        notif = NSCANotifier(nsca_host)
        notif.svc_result(host_name, service_description, status, text)
    except Exception, e:
        srv.logging.warning("Cannot notify to NSCA host `%s': %s" % (nsca_host, str(e)))
        return False

    return True

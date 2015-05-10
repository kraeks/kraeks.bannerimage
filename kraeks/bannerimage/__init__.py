import logging
from zope.i18nmessageid import MessageFactory

logger = logging.getLogger('uvcsite.kraeks.bannerimage')
bannerimageMessageFactory = MessageFactory('kraeks.bannerimage')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

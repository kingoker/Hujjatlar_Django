from typing import Iterable, Union, List, Tuple
import logging

logger = logging.getLogger(__name__)

def broadcast_notification(
	message : str,
	relevant_user_emails : Union[List[str], Tuple[str]]
):
	for email in relevant_user_emails:
		logger.debug("Sending %r to %r", message, email)


broadcast_notification("welcome", ["test@gmail.com"])		
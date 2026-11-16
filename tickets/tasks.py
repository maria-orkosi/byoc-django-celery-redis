from celery import shared_task


@shared_task
def notify(ticket_id: int) -> str:
    return f"notified {ticket_id}"

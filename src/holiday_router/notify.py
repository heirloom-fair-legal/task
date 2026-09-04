from holiday_router.models import Channel, Notification, Role


def send_slack(role: Role) -> None:
    print(f"sending approval request via Slack to {role.value}")


def send_email(role: Role) -> None:
    print(f"sending approval request via Email to {role.value}")


def notify(notification: Notification) -> None:
    if notification.channel is Channel.SLACK:
        send_slack(notification.role)
    elif notification.channel is Channel.EMAIL:
        send_email(notification.role)
    else:
        raise ValueError(f"unknown channel: {notification.channel}")

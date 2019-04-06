from app.actions import Actions
from app.utils.slackhelper import SlackHelper


def main():
    slack_helper = SlackHelper()
    actions = Actions(slack_helper)
    actions.notify_channel()


if __name__ == '__main__':
    main()

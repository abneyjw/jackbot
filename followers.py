from twitchAPI.twitch import Twitch

class TwitchCount():
    twitch = Twitch('d2xt6xdmf8ke5b2bikl5r6jmmrqzlc', 'xh5ubqj1k8f8rlfj8i9gbyfp87vv4u')

    user = 'itisjacktime'

    stuff = (twitch.get_users(logins=[user]))

    def count(self):
        return self.twitch.get_users_follows(to_id=self.stuff['data'][0]['id'])['total']

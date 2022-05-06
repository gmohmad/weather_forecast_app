from transitions import Machine


class ChatBot():
    states = [
        'asleep',
        'get city',
        'get comfortable temperature',
        'confirm'
    ]

    transitions = [
        {
            'trigger': 'start',
            'source': 'asleep',
            'dest': 'get city'
        },
        {
            'trigger': 'get_comfortable_temperature',
            'source': 'get city',
            'dest': 'get comfortable temperature'
        },
        {
            'trigger': 'confirm',
            'source': 'get comfortable temperature',
            'dest': 'confirm'
        },
        {
            'trigger': 'end',
            'source': 'confirm',
            'dest': 'asleep'
        },
        {
            'trigger': 'stop',
            'source': '*',
            'dest': 'asleep'
        },
    ]

    def __init__(self):
        self.city = None
        self.comfortable_temperature = None
        self.weather_api_response = None

        self.machine = Machine(
            model=self,
            states=self.states,
            transitions=self.transitions,
            initial='asleep',
            ignore_invalid_triggers=True
        )

## Ponchi

Ponchi is a microframework for creating single-user Telegram bots based on [aiogram](https://github.com/aiogram/aiogram).

## Application Example

Implementation of the simplest bot on Ponchi

    async def start(message: Message, session: SessionController) -> Callable | str:
        await message.answer(message.text)
        return start




## Setup

#### There is currently no PyPi download available at this time ([issuse #1](https://github.com/ommatotritonophryticus/ponchi/issues/1)).

Download the project:

    $ git clone https://github.com/ommatotritonophryticus/ponchi.git

Go to the directory:

    $ cd ponchi

Install with pip:

    $ pip install .

 ## Project Initialization


#### First step
The initial initialization is performed by executing the command in the project folder:

    $ python -m ponchi createapp

After that the files application.py, config.py will be created in the folder.

#### Second step 

You need to insert telegram-token into the config.py file:

    TOKEN = '{YOUR TOKEN}'


#### Third step

You need to select and configure the database. 
By default, fake_db is used, DO NOT USE IT FOR PRODUCTION. 
There is also a setting to connect to the Redis database. 
To use it, change the DATABASE parameter:

    DATABASE = DATABASES['redis']

#### Fourth step

The application is launched with the command.

    $ python -m ponchi start

